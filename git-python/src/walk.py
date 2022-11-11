from pathlib import Path
from git import Repo
from typing import Tuple


def walk_repos(root_path: str) -> Tuple[str, Repo]:
    root_dir = Path(root_path)
    for git_dir in root_dir.glob('**/.git'):
        repo_dir = git_dir.parent.resolve()
        rel_dir = str(repo_dir).removeprefix(root_path)
        yield rel_dir, Repo(repo_dir)
