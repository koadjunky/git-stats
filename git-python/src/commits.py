import sys
import json
import datetime
from collections.abc import Generator
from typing import List

from repos import walk_repos
from users import map_user


def get_all_commits(root_path: str) -> Generator[datetime.datetime, str]:
    for repo in walk_repos(root_path):
        for line in repo.git.log("--format=%at %ae").split('\n'):
            tstamp, email = line.split()
            yield datetime.datetime.fromtimestamp(int(tstamp)), map_user(email)


def aggregate_hours(root_path: str) -> List[int]:
    result = [0] * (24 * 7)
    for date, email in get_all_commits(root_path):
        index = date.weekday() * 24 + date.hour
        result[index] += 1
    return result


def aggregate_to_data(aggr_hours: List[int]) -> List[List[int]]:
    result = []
    for hour in range(24):
        for day in range(7):
            result.append([hour, day, aggr_hours[day * 24 + hour]])
    return result


def write_to_json(data: List[List[int]]) -> None:
    with open('commits.json', 'w') as outfile:
        json.dump(data, outfile)


if __name__ == '__main__':
    root_path = sys.argv[1]
    aggr_hours = aggregate_hours(root_path)
    data_hours = aggregate_to_data(aggr_hours)
    write_to_json(data_hours)

