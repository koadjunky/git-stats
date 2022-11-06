import sys
import json
import datetime
from collections.abc import Generator
from typing import List
import pandas as pd

from repos import walk_repos
from users import map_user


def get_all_commits(root_path: str) -> Generator[datetime.datetime, str]:
    for repo in walk_repos(root_path):
        for line in repo.git.log("--format=%at %ae").split('\n'):
            tstamp, email = line.split()
            yield datetime.datetime.fromtimestamp(int(tstamp)), map_user(email)


def get_all_commits_df(root_path: str) -> pd.DataFrame:
    table = []
    for date, email in get_all_commits(root_path):
        table.append([date, email])
    return pd.DataFrame(table, columns=['date', 'email'])


def aggregate_hours_df(df: pd.DataFrame) -> pd.DataFrame:
    hours = df['date'].dt.hour.to_frame(name='hour')
    weekdays = df['date'].dt.weekday.to_frame(name='weekday')
    df = pd.concat([df, hours, weekdays], axis=1)
    return pd.crosstab(df['weekday'], df['hour'])


def write_to_csv(df: pd.DataFrame, fname: str) -> None:
    df.to_csv(fname)


if __name__ == '__main__':
    root_path = sys.argv[1]
    commits = get_all_commits_df(root_path)
    aggr_hours = aggregate_hours_df(commits)
    write_to_csv(aggr_hours, 'commits_heatmap.csv')
