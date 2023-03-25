import sys
import gitlab
import private
from astropy.io import ascii
from astropy.table import Table

gl = gitlab.Gitlab(private.GITLAB_URL, private_token=private.GITLAB_TOKEN)
gl.auth()

tbl = Table(names=('path', 'url'), dtype=('S', 'S'))
for project in gl.projects.list(get_all=True):
    tbl.add_row((project.path_with_namespace, project.ssh_url_to_repo))
tbl.sort(keys='path')
ascii.write(tbl, sys.stdout, format='mrt')
