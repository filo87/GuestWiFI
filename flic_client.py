#!/usr/bin/env python3

# Test Client application.
#
# This program attempts to connect to all previously verified Flic buttons by this server.
# Once connected, it prints Down and Up when a button is pressed or released.
# It also monitors when new buttons are verified and connects to them as well. For example, run this program and at the same time the scan_wizard.py program.

import fliclib
from settings import *
from functions import generate_pwd, ssh_pwd_change, pwdPrint, writePwd

client = fliclib.FlicClient(flicServer)

def got_button(bd_addr):
	cc = fliclib.ButtonConnectionChannel(bd_addr)
	cc.on_button_click_or_hold = change_password_and_print
	client.add_connection_channel(cc)

def got_info(items):
	if flicId in items["bd_addr_of_verified_buttons"]:
		got_button(flicId)

def change_password_and_print(channel, click_type, was_queued, time_diff):
	global pwd
	pwd = generate_pwd(pwdLength)
	ssh_pwd_change(sshUser, sshIp, radioSSID, pwd)
	writePwd(pwd)
	pwdPrint(printerIp, radioSSID, pwd)

if __name__ == "__main__":
	client.get_info(got_info)
	client.handle_events()
