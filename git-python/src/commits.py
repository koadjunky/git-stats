import sys
import json
import datetime

from repos import walk_repos
from users import map_user


# TODO: Fix nesting

def get_all_commits(root_path):
    for repo in walk_repos(root_path):
        for line in repo.git.log("--format=%at %ae").split('\n'):
            tstamp, email = line.split()
            yield datetime.datetime.fromtimestamp(int(tstamp)), map_user(email)


def aggregate_hours(root_path):
    result = [0] * (24 * 7)
    for date, email in get_all_commits(root_path):
        index = date.weekday() * 24 + date.hour
        result[index] += 1
    return result


def aggregate_to_data(root_path):
    aggr = aggregate_hours(root_path)
    result = []
    for hour in range(24):
        for day in range(7):
            result.append([hour, day, aggr[day * 24 + hour]])
    return result


def write_to_json(root_path):
    with open('commits.json', 'w') as outfile:
        json.dump(aggregate_to_data(root_path), outfile)


if __name__ == '__main__':
    write_to_json(sys.argv[1])

