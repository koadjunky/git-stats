from typing import List, Union

from git import Repo
import pandas as pd

from walk import walk_repos


def xrange2bnd(xrng):
    start = stop = next(iter(xrng))
    for i in xrng:
        stop = i
    return start, (stop - start + 1)

class BlameFile:
    def __init__(self, fname):
        self.filename = fname
        self.total = 0
        self.authors = {}

    def add_author(self, author, lines):
        if not author in self.authors:
            self.authors[author] = 0
        self.authors[author] += lines

    def add_blame(self, entry):
        author = entry.commit.author.email
        _, count = xrange2bnd(entry.linenos)
        self.add_author(author, count)
        self.total += count


def survived_in_repo(repo_dir:str, repo: Repo) -> List[List[Union[str, int]]]:
    # Should be -CCC but it is impossible in current GitPython
    table = []
    for entry in repo.commit().tree.traverse():
        fpath = entry.path
        if entry.type == 'blob':
            bfile = BlameFile(fpath)
            for entry in repo.blame_incremental(None, fpath, M=True, C=True, w=True):
                bfile.add_blame(entry)
            for author in bfile.authors.keys():
                table.append([repo_dir, fpath, author, bfile.authors[author], bfile.total])
    return table


def main(root_dir: str, prefix: str) -> pd.DataFrame:
    table = []
    for repo_dir, repo in walk_repos(root_dir):
        table.extend(survived_in_repo(prefix + repo_dir, repo))
    return pd.DataFrame(table, columns=['dir', 'path', 'email', 'survived', 'total'])


if __name__ == '__main__':
    import sys
    root_dir = sys.argv[1]
    prefix = sys.argv[2]
    df = main(root_dir, prefix)
    df.to_csv(f'jupyter/survived-{prefix}.csv')
