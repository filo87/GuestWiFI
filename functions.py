import os, sys, datetime, shelve
from strgen import StringGenerator as SG
from escpos.printer import Network
from settings import dbName

class wifiPwdManager(object):
    """Python class for managing the wifi password"""

    def read(self):
        "Reads password from shelve db"
        db = shelve.open(self.dbName)
        if 'currentPwd' in db:
            self.pwd = db['currentPwd']
        else:
            self.pwd=''
        db.close()
        return self.pwd

    def write(self):
        "Writes password to shelve db"
        db = shelve.open(self.dbName)
        db['currentPwd'] = self.pwd
        db.close()
        return self.pwd

    def generate(self, length=10):
        "Creates a readable password of length characters"
        self.pwd = SG("[a-kl-np-z0-9]{" + str(length) + "}").render()
        return self.pwd

    def sshChange(self):
        "Connects over SSH and change radio password"
        return os.system("ssh %s@%s 'nvram set %s_wpa_psk=%s && nvram commit && rc restart'" % (self.sshUser, self.sshIp, self.radioId, self.pwd))


    def thermalPrint(self):
        "Prints the pwd on the thermal printer at the specified ip"
        if self.printerIp:
            p = Network(self.printerIp)
            p.set(align='center', text_type='bold', width=2, height=2)
            p.text("fZone Guest WiFI\n\n")
            p.set()
            p.text('\tDate:\t' + datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y") + '\n')
            p.text('\tSSID:\t' + self.radioSSID + '\n')
            p.text('\tPwd:\t' + self.pwd + '\n')
            p.text('\n')
            p.set(align='center')
            p.qr('WIFI:T:WPA;S:' + self.radioSSID +';P:' + self.pwd + ';;', size=6, native=False)
            p.text('Scan me to login!')
            p.cut()
            p.close()
        pass

    def __init__(self, sshIp, **kwargs):
        self.sshIp = sshIp
        self.sshUser =  kwargs.get('sshUser',"root")
        self.radioSSID =  kwargs.get('radioSSID',"Guest")
        self.radioId = kwargs.get('radioId', 'wl0')
        self.printerIp = kwargs.get('printerIp', None)
        self.dbName = kwargs.get('dbName', 'pwd.db')
        super(wifiPwdManager, self).__init__()
        self.read()
