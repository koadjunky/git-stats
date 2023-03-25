import os.path
import gitlab
import private
from astropy.io import ascii
from astropy.table import Table

gl = gitlab.Gitlab(private.GITLAB_URL, private_token=private.GITLAB_TOKEN)
gl.auth()

for project in gl.projects.list(get_all=True):
    path = project.path_with_namespace
    url = project.ssh_url_to_repo
    local_path = private.GIT_ROOT + '/' + path
    if (os.path.exists(local_path)): continue
    if not any([path.startswith(prefix) for prefix in private.GIT_PREFIXES]): continue
    dir_name = os.path.dirname(local_path)
    if (not os.path.exists(dir_name)):
        print(f"mkdir -p {dir_name}")
    print(f"cd {dir_name}")
    print(f"git clone {url}")
