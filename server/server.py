#########################################################################
# 
#     TCP Server Script
# 
# 
# 
#########################################################################

import socket as _socket
from PyQt5.QtWidgets import QWidget
from pyqtgraph.Qt import QtCore
import time

class SERVER():
    
    def __init__(self):
        
        super(SERVER, self).__init__()
        self.serverHost = ''
        self.serverPort = 5008
        self.isConnected = False
        self.sockobj = None
    
     
        self.serversocket= _socket.socket(_socket.AF_INET, _socket.SOCK_STREAM)      # create socket
        self.serversocket.bind((self.serverHost,self.serverPort))

    
    def disconnect(self):
        self.sockobj.close()                             # close socket
        self.isConnected = False
    
    def startLisening(self):
        print('start')
        
        while True:
        
            if self.isConnected==False:
                time.sleep(1)
                print('lisenning..')
                self.serversocket.listen(1)
                try :
                    self.clientsocket,addr = self.serversocket.accept()
                    self.isConnected=True
                    print('connected to client',addr)
                except :  print('not yet')
                
            else : 
                try :
                    msgReceived=self.clientsocket.recv(1024)
                    msgReceived=msgReceived.decode()
                    if msgReceived:
                        print('message received: ',msgReceived)
                        messageSend='mess receiv'+msgReceived
                        self.clientsocket.sendall(messageSend.encode())
                except: pass
        
        
    
    
if __name__ == "__main__":       
    
    s =  SERVER() 
    s.startLisening()
             
    
