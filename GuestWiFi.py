#!/usr/bin/python
from functions import generate_pwd, ssh_pwd_change
from flask import Flask, request

pwdLength = 10

sshUser = 'root'
sshIp   = '10.0.0.10'
radio   = 'wl0.2'
pwd = generate_pwd(pwdLength)

# print ssh_pwd_change(sshUser,sshIp, radio, pwd)
# print pwd


app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def main():
    return 'Hello World!'
