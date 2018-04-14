import os
import sys

# Install venv by `virtualenv --distribute venv`
# Then install depedencies: `source venv/bin/active`
# `pip install -r requirements.txt`
activate_this = '/var/www/GuestWiFi/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

path = os.path.join(os.path.dirname(__file__), os.pardir)
if path not in sys.path:
    sys.path.append(path)

# The application object is used by any WSGI server configured to use this
# file.

# Ensure there is an app.py script in the current folder
from GuestWiFi import app as application
