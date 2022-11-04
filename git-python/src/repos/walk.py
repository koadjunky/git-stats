from pathlib import Path
from git import Repo


def walk_repos(root_path: str):
    root_dir = Path(root_path)
    for git_dir in root_dir.glob('**/.git'):
        repo_dir = git_dir.parent
        yield Repo(repo_dir.resolve())


if __name__ == '__main__':
    import sys
    for i in walk_repos(sys.argv[1]):
        print(i.active_branch)
