import os, sys
from strgen import StringGenerator as SG

def generate_pwd(length):
        "Creates a readable password of X characters"
        pwd = SG("[a-kl-np-z0-9]{" + str(length) + "}").render()

        return pwd

def ssh_pwd_change(user, ip, radio, newPwd):
    "Connect over SSH and change radio password"
    return os.system("ssh %s@%s 'nvram set %s_wpa_psk=%s && nvram commit && rc restart'" % (user, ip, radio, newPwd))
