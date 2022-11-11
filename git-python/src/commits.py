import re
import sys
import datetime
import logging
import pandas as pd
from git import Repo
from pathlib import Path


header_re = re.compile("^(\d+) (\S+) (.*)$")
numstat_re = re.compile("^(\d+)\s+(\d+)\s+(.*)$")
binary_re = re.compile("^-\s+-\s+(.*)$")


# TODO: Move to separate directory
def walk_repos(root_path: str):
    root_dir = Path(root_path)
    for git_dir in root_dir.glob('**/.git'):
        repo_dir = git_dir.parent.resolve()
        rel_dir = str(repo_dir).removeprefix(root_path)
        yield rel_dir, Repo(repo_dir)


def get_all_commits(root_dir: str) -> pd.DataFrame:
    table = []
    for repo_dir, repo in walk_repos(root_dir):
        for line in repo.git.log("--format=%at %ae %s", "--numstat").split('\n'):
            if line == "":
                continue
            m = header_re.match(line)
            if m is not None:
                date = datetime.datetime.fromtimestamp(int(m.group(1)))
                email = m.group(2)
                subject = m.group(3)
                continue
            m = numstat_re.match(line)
            if m is not None:
                insertions = int(m.group(1) or 0)
                deletions = int(m.group(2) or 0)
                path = m.group(3)
                table.append([date, email, insertions, deletions, repo_dir, path])
                continue
            m = binary_re.match(line)
            if m is not None:
                continue
            logging.error("Unrecognized line: %s" % line)
    return pd.DataFrame(table, columns=['date', 'email', 'ins', 'del', 'dir', 'path'])


def write_to_csv(df: pd.DataFrame, fname: str) -> None:
    df.to_csv(fname)


if __name__ == '__main__':
    root_path = sys.argv[1]
    commits = get_all_commits(root_path)
    write_to_csv(commits, 'jupyter/commits.csv')
