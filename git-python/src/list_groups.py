import sys
import gitlab
import private
from astropy.io import ascii
from astropy.table import Table

gl = gitlab.Gitlab(private.GITLAB_URL, private_token=private.GITLAB_TOKEN)
gl.auth()

tbl = Table(names=('name', 'url'), dtype=('S', 'S'))
for group in gl.groups.list():
    tbl.add_row((group.full_name, group.web_url))
tbl.sort(keys='name')
ascii.write(tbl, sys.stdout, names=['name', 'url'], format='mrt')
