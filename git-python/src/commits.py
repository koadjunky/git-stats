import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.resolve()))

import re
import datetime
import logging
import pandas as pd

from walk import walk_repos


header_re = re.compile("^(\d+) (\S+) (.*)$")
numstat_re = re.compile("^(\d+)\s+(\d+)\s+(.*)$")
binary_re = re.compile("^-\s+-\s+(.*)$")


def get_all_commits(root_dir: str, prefix: str) -> pd.DataFrame:
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
                table.append([date, email, insertions, deletions, prefix + repo_dir, path])
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
    prefix = sys.argv[2]
    commits = get_all_commits(root_path, prefix)
    write_to_csv(commits, f'jupyter/commits-{prefix}.csv')
