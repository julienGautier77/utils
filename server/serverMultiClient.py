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
import select
import numpy as np
import pickle
import struct
#for send and receive numpy  
# more details : https://github.com/ekbanasolutions/numpy-using-socket
        

class SERVER(QtCore.QThread):
    '''Server class with multi clients

    '''
    newDataRun=QtCore.Signal(object)
    def __init__(self,parent=None):
        
        super(SERVER, self).__init__()
        self.serverHost = ''
        self.serverPort = 5009
        self.image=np.random.rand(10,10)
        self.serversocket= _socket.socket(_socket.AF_INET, _socket.SOCK_STREAM)      # create socket
        try :
            self.serversocket.bind((self.serverHost,self.serverPort))
            self.isConnected = True
            print('server ready')
        except :
            print('error connection server')
            self.isConnected = False
        
        self.clientsConnectedSocket = []
    
    def disconnect(self):
        self.serversocketclose()                             # close socket
        self.isConnected = False
    
    def startServer(self):#run
        print('start lisenning')
        
        while self.isConnected==True:
            self.serversocket.listen(5)
            # On va vérifier que de nouveaux clients ne demandent pas à se connecter
            connexions_demandees, wlist, xlist = select.select([self.serversocket],[], [], 0.05)
           
            for connexion in connexions_demandees:
                # on accepte les connexions
                connexion_avec_client, infos_connexion = connexion.accept()
                # On ajoute le socket connecté à la liste des clients
                
                self.clientsConnectedSocket.append(connexion_avec_client)
            
            # Maintenant, on écoute la liste des clients connectés
            # Les clients renvoyés par select sont ceux devant être lus (recv)
            # On attend là encore 50ms maximum
            # On enferme l'appel à select.select dans un bloc try
            # En effet, si la liste de clients connectés est vide, une exception
            # Peut être levée
            
            clientsToRead = []
            try:
                clientsToRead, wlist, xlist = select.select(self.clientsConnectedSocket,[], [], 0.05)
            except select.error:
                pass
            else:
                # On parcourt la liste des clients à lire
                for client in clientsToRead:
                    # Client est de type socket
                    msgReceived= client.recv(1024)
                    msgReceived=msgReceived.decode()
                    
                    if msgReceived=='close server':
                        print('close server')
                        for client in self.clientsConnectedSocket:
                            client.close()
                        time.sleep(0.5) 
                        self.serversocket.Client.Disconnect(True)
                        self.serversocket.close()
                        self.isConnected=False
                        
                        
                    elif msgReceived=='data?':
                        
                        self.sendNumpy(client,self.image)
                    
                    elif msgReceived  : 
                        
                        print('message received: ',msgReceived)
                        messageSend='mess received:  '+msgReceived
                        
                        client.sendall(messageSend.encode())
                        
    

    
    def sendNumpy(self,client, np_array):
        time.sleep(10)
        if not isinstance(np_array, np.ndarray):
            print( 'not a valid numpy image')
            return
        data = pickle.dumps(np_array)

        # Send message length first
        message_size = struct.pack("=L", len(data))  ### L for linux, =L for PC "CHANGED"

        # Then data
        client.sendall(message_size + data)
        print('sent')
    
    
if __name__ == "__main__":       
    
    s =  SERVER() 
    s.startServer()#start()
             
    
