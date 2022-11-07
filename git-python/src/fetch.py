from repos import walk_repos


def main(root_path: str):
    for repo in walk_repos(root_path):
        repo.remote().fetch()


if __name__ == '__main__':
    import sys
    root_path = sys.argv[1]
    main(root_path)
