import os, sys
from strgen import StringGenerator as SG
from escpos.printer import Network
import datetime

def generate_pwd(length):
        "Creates a readable password of X characters"
        pwd = SG("[a-kl-np-z0-9]{" + str(length) + "}").render()

        return pwd

def ssh_pwd_change(user, ip, radio, newPwd):
    "Connect over SSH and change radio password"
    return os.system("ssh %s@%s 'nvram set %s_wpa_psk=%s && nvram commit && rc restart'" % (user, ip, radio, newPwd))

def pwdPrint(ip, ssid, pwd):
    "Prints the pwd on the thermal printer at the specified ip"
    p = Network(ip)
    p.set(align='center', text_type='bold', width=2, height=2)
    p.text("fZone Guest WiFI\n\n")
    p.set()
    p.text('\tDate:\t' + datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y") + '\n')
    p.text('\tSSID:\t' + ssid + '\n')
    p.text('\tPwd:\t' + pwd + '\n')
    p.text('\n')
    p.set(align='center')
    p.qr('WIFI:T:WPA;S:' + ssid +';P:' + pwd + ';;', size=6, native=False)
    p.text('Scan me to login!')
    p.cut()
