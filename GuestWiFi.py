from os import path
import threading

from flask import Flask, request, render_template

from settings import *
from flic_client import client, got_info
from functions import generate_pwd, ssh_pwd_change, pwdPrint, writePwd, readPwd

app = Flask(__name__)

#Create handler for the / main route un Flask accepting get and post requests
@app.route("/", methods=['GET', 'POST'])
def main():
    #overwrite global wifi password pwd ADD persistence
    global pwd

    #Handle post data from the form
    if request.method == 'POST' and 'generate' in request.form:
        pwd = generate_pwd(pwdLength)
        ssh_pwd_change(sshUser, sshIp, radio, pwd)
        writePwd(pwd)

        if 'print' in request.form:
            pwdPrint(printerIp, radioSSID, pwd)

    content = {'wifiPwd': readPwd()}
    return render_template('main.html', **content)

#Subthread class for handling flic button requests
class T(threading.Thread):
    def run(self):
        client.get_info(got_info)
        client.handle_events()

T().start()
