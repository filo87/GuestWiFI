import sys
sys.path.insert(0, '/var/www/GuestWiFi/GuestWiFi')

from GuestWiFi import app as application

activate_this = '/var/www/GuestWiFi/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))
