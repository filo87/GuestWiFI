from flask_script import Server, Manager
from GuestWiFi import app

manager = Manager(app)
manager.add_command("runserver", Server(host="0.0.0.0", port=5000))

if __name__ == "__main__":
    manager.run()
