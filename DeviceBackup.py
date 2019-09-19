# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 10:54:29 2019

@author: 301986
"""

import getpass
import telnetlib

user = input('Enter your telnet username: ')
password = getpass.getpass()

f = open('textfile.txt')

for IP in f:
    IP=IP.strip()
    print ('Get running config from Switch ' + (IP))
    HOST = IP
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"ACS username: ")
    tn.write(user.encode('ascii') + b'\n')
    if password:
        tn.read_until(b"ACS password: ")
        tn.write(password.encode('ascii') + b'\n')  
    tn.write(b"terminal length 0\n")
    tn.write(b"show run\n")
    tn.write(b'exit\n')

    readoutput = tn.read_all()
    saveoutput =  open("switch" + HOST +".txt", "w")
    saveoutput.write(readoutput.decode('ascii'))
    saveoutput.write("\n")
    saveoutput.close
