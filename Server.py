import socket
from  threading import Thread
import time
import os
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

def ftp():
    global IP_ADDRESS

    authorizer=DummyAuthorizer()
    authorizer.add_user("lftpd","lftpd",".",perm="alradfmw")

    handler=FTPHandler
    handler.authorizer=authorizer

    ftp_server=FTPServer((IP_ADDRESS,21),handler)
    ftp_server.serve_forever()

setup_thread=Thread(target=setup)
setup_thread.start()

ftp_handler=Thread(target=ftp)
ftp_thread.start()



is_dir_exists=os.path.isdir('shared_files')
print(is_dir_exists)
if(not is_dir_exists):
    os.makedirs('shared_files')




def acceptConnections():
    global SERVER
    global clients

    while True:
        client,addr=SERVER.accept()
        client_name=client.recv(4096).decode().lower()
        clients[client_name]={
            "client":client,
            "address":addr,
            "connected_with":"",
            "file_name":"",
            "file_size":4096
        }
    print(f"Connection established with{client_name}:(addr)")

    thread=Thread(target=handleClient,args=(client,client_name,)) 
    thread.start()
