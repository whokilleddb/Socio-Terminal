#!/bin/python3
from subprocess import check_output
import logging
from os import remove, path
# This file shall contain miscellaneous functions and data structures :
# 1. Function to calculate md5sums of Images/Files/Gifs
# 2. Dictionaries of Important hashes
# 3. Move Media to /tmp
# 4. More

# Colours/Format Options For Terminal
class fmt :
    NONE='\033[00m'
    BLACK='\033[01;30m'
    RED='\033[01;31m'
    GREEN='\033[01;32m'
    YELLOW='\033[01;33m'
    BLUE='\033[0;34m'
    PURPLE='\033[01;35m'
    CYAN='\033[01;36m'
    WHITE='\033[01;37m'
    BOLD='\033[1m'
    BLINK='\033[5m'
    UNDERLINE='\033[4m'

# Wrapper Around logging module 
class logthis :
    def __init__(self):
        logging.basicConfig(level=logging.DEBUG,filename="socio-terminal.log",format="%(asctime)s [%(levelname)s] - [%(filename)s > %(funcName)s() > %(lineno)s] - %(message)s",datefmt="%H:%M:%S")
    def debug(self,msg):
        logging.debug(msg)
    def info(self,msg):
           logging.info(msg)
    def warning(self,msg):
           logging.warning(msg)
    def error(self,msg):
           logging.error(msg)
    def critical(self,msg):
           logging.critical(msg)

# Delete A File
def rm(filename):
    logger=logthis()
    try :
        if(path.isfile(filename)):
            remove(filename)
            logger.info(f"Removed {filename}")
            return 0 # Signifies Successful Deletion
        else :
            logger.error(f"{filename} Not Found")
            return -1 # Signifies that file does not exist in Path
    except Exception as e :
        logger.error(f"Error Occured While Deleteing : {filename}")
        logger.error(f"Error : {e}")
        return -99 # Signifies error in deleteinf=g

# Function to calculate md5sum of Files and return a list of the format {MD5SUM, FILENAME}
def md5sum(filename):
    logger=logthis()
    output=list()
    if(path.isfile(filename)):
        output = check_output(f"md5sum {filename}", shell=True).decode().strip().split("  ")
        logger.info(f"Calculated MD5SUM of {output[1]} as {output[0]}")
        return output
    else :
        logger.error(f"{filename} Not Found")
        return output

# Return Logs Created By The Program
def readlog() :
    logger=logthis()
    logfile="socio-terminal.log"
    if(path.isfile(logfile)):
        logger.info(f"Reading Log-File : {logfile}")
        f = open(logfile, "r")
        return f.read()
    else :
        logger.error(f"{logfile} Not Found")
        return ""
    
