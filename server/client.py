#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 10:30:50 2020

@author: juliengautier
"""

#########################################################################
# 
#     TCP Client Script
# 
# 
# 
#########################################################################

import socket as _socket
from PyQt5.QtWidgets import QWidget
from pyqtgraph.Qt import QtCore
import time
import pickle
import struct


class CLIENT():
    
    def __init__(self):
        
        super(CLIENT, self).__init__()
        self.serverHost = _socket.gethostname()
        self.serverPort = 5009
        self.clientSocket= _socket.socket(_socket.AF_INET, _socket.SOCK_STREAM)      # create socket
        try :
            self.clientSocket.connect((self.serverHost,self.serverPort))
            self.isConnected = True
        except:
            self.isConnected = False
                
    def disconnect(self):
        self.clientSocket.close()                         # close socket
        self.isConnected = False
        
    def sendCommand(self,cmd=''):
        if cmd=='data?':
            self.clientSocket.send(cmd.encode())
            data=self.receive_array()
            
            return data
        
        else:   
            self.clientSocket.send(cmd.encode())
            receiv=self.clientSocket.recv(64500)
            return receiv.decode()
    
    
    
    def receive_array(self):
        self.payload_size = struct.calcsize("L")  ### CHANGED
        self.data = b''
        while len(self.data) < self.payload_size:
            self.data += self.clientSocket.recv(4096)
            
        packed_msg_size = self.data[:self.payload_size]
        
        self.data = self.data[self.payload_size:]
        msg_size = struct.unpack("L", packed_msg_size)[0]

        # Retrieve all data based on message size
        while len(self.data) < msg_size:
            self.data +=self.clientSocket.recv(4096)

        frame_data = self.data[:msg_size]
        self.data = self.data[msg_size:]

        # Extract frame
        frame = pickle.loads(frame_data)
        return frame
    
    
    
    
    
    
    
    