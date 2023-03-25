import sys
import gitlab
import private
from astropy.io import ascii
from astropy.table import Table

gl = gitlab.Gitlab(private.GITLAB_URL, private_token=private.GITLAB_TOKEN)
gl.auth()

tbl = Table(names=('username', 'name', 'state'), dtype=('U', 'U', 'U'))
for user in gl.users.list(get_all=True):
    tbl.add_row((user.username, user.name, user.state))
tbl.sort(keys='username')
ascii.write(tbl, sys.stdout, format='mrt')
