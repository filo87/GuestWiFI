from GuestWiFi import app as application

activate_this = '../bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))
