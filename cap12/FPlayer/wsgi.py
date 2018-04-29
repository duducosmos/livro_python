import sys
activate_this = "/var/www/FPlayer/env/bin/activate_this.py"

execfile(activate_this, dict(__file__=activate_this))

PROJECT_DIR = "/var/www/FPlayer"

sys.path.insert(0, PROJECT_DIR)

from fplayer import app as application
