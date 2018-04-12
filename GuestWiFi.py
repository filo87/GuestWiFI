#!/usr/bin/python
from os import path
from functions import generate_pwd, ssh_pwd_change, pwdPrint
from flask import Flask, request, render_template
import shelve



sshUser =   'root'
sshIp   =   '10.0.0.10'
printerIp = '10.0.0.21'

radioSSID = 'fZone.ch_guest'
radio =     'wl0.2'
pwdLength = 10


pwd = generate_pwd(pwdLength)

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def main():
    global pwd
    if request.method == 'POST' and 'generate' in request.form:
        pwd = generate_pwd(pwdLength)
        #ssh_pwd_change(sshUser, sshIp, radio, pwd)

        if 'print' in request.form:
            pwdPrint(printerIp, radioSSID, pwd)

    content = {'wifiPwd': pwd}
    return render_template('main.html', **content)
