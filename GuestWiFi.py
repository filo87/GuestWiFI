import threading, signal

from flask import Flask, request, render_template

from settings import *
from functions import wifiPwdManager
from flic_client import client, got_info

app = Flask(__name__)

#Create handler for the / main route un Flask accepting get and post requests
@app.route("/", methods=['GET', 'POST'])
def main():
    #Create password manager object
    p = wifiPwdManager(sshIp,
                        sshUser = sshUser,
                        radioSSID = radioSSID,
                        radioId = radioId,
                        printerIp = printerIp,
                        dbName = dbName)


    #Handle post data from the form
    if request.method == 'POST' and 'generate' in request.form:
        p.generate(pwdLength)
        p.sshChange()
        p.write()

        if 'print' in request.form:
            p.thermalPrint()

    content = {'wifiPwd': p.pwd}
    return render_template('main.html', **content)


#Subthread daemon for handling flic button requests
class flicThread(threading.Thread):
    def run(self):
        client.get_info(got_info)
        client.handle_events()

t = flicThread()
t.daemon=True
t.start()
