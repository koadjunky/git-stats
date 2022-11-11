import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.resolve()))

from walk import walk_repos


def main(root_path: str):
    for repo_path, repo in walk_repos(root_path):
        repo.remote().fetch()


if __name__ == '__main__':
    import sys
    root_path = sys.argv[1]
    main(root_path)
