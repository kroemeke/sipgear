#!/usr/bin/python

###############################################
# track2aprs                                  #
# TK-110 -> aprs                              #
# Marek Kroemeke 2012                         #
# License: GPL2                               #
###############################################

import SocketServer
from socket import *
import sys, time
import sipgear
import logging
from pprint import pprint

serverHost = 'euro.aprs2.net'
serverPort = 14580
password = 'YOURPASSWORD'
address = 'YOURCALLSIGN-9>APRS,qAR,YOURCALLSIGN-VS:'
comment = 'TX only'
packet = ''
SocketServer.TCPServer.allow_reuse_address = True

logging.basicConfig(filename='track2aprs.log',format='%(asctime)s %(message)s',datefmt='%a, %d %b %Y %H:%M:%S',level=logging.DEBUG)

class aprs:
  def __init__(self,longtitude,latitude,speed,direction):
      self.longtitude = longtitude
      self.latitude   = latitude
      self.speed      = str(int(float(speed) / 0.53)).zfill(3)
      if direction == '':
        self.direction = '000'
      else:
        self.direction  = direction.split('.')[1].zfill(3)
      self.address    = address
      self.comment    = comment
  def position(self):
    pkt =   self.address + \
            '=' + \
            self.latitude + \
            '/' + \
            self.longtitude + \
            '>' + \
            self.direction + \
            '/' + \
            self.speed + \
            self.comment
    return pkt
            


# This is aprs side.
def send_packet(position):
        sSock = socket(AF_INET, SOCK_STREAM)
        sSock.connect((serverHost, serverPort))
        sSock.send('user YOURCALLSIGN pass ' + password + ' vers track2aprs 0.1b\n')
        sSock.send(position + '\n')
        time.sleep(3) # 15 sec. delay
        sSock.shutdown(0)
        sSock.close()

# Tracker handler 
class MyTCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
      while(1):
        self.pkt = sipgear.message(self.request.recv(1024))
        if not self.pkt : break
        self.aprsm = aprs(self.pkt.longtitude,self.pkt.latitude,self.pkt.speed,self.pkt.direction)
        logging.info(self.aprsm.position())
        logging.info(self.request.recv(1024))
        send_packet(self.aprsm.position())

if __name__ == "__main__":
    HOST, PORT = "", 6081 
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()

