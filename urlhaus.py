#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__	=	"Jason Brown"
__email__	=	"jason.brown@svarthal.io"
__version__	=	"0.3"
__license__	=	"Apache"
__date__	=	"20200211"


import urllib.request
from os import chown
from os import chmod
from os import system
from shutil import move
import subprocess

def main():

	'''
		Fetch new malware file and write it to disk
	'''

	urlhaus = urllib.request.urlopen('https://urlhaus.abuse.ch/downloads/rpz/')
	with open ('db.urlhaus', 'b+w') as malware:
		malware.write(urlhaus.read())

	'''
		Setting correct permissions on the db file and moving it to the Bind9 directory
	'''
	chown('db.urlhaus', 0, 114)
	chmod('db.urlhaus', 0o644)
	move('db.urlhaus', '/etc/bind/svarthal/db.urlhaus')
	system('systemctl restart bind9')


if __name__ == '__main__':
	main()