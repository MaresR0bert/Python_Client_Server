import socket
import time

def Main():
    host = "37.120.249.45" #asignare host
    port = 8210 #asignare port

    usedSocket = socket.socket() #creare socket
    usedSocket.connect((host,port)) #conectare

    print('Input command as following:\nRandom Joke - joke\nCurrent Time - time\nRandom Number - rando')
    msj = input("> ") #input mesaj

    while msj: #bucla infinita pentru transmitere 
        try:
            temp = int(msj)
            for i in range(temp):
                time.sleep(1)
                print("Server closing in", temp - i -1) #functionalitate
            break;
        except:
            usedSocket.send(msj.encode()) #trimitere mesaj pe socket
            data = usedSocket.recv(1024).decode() 
            print ('Server>> ' + data)
            msj = input("> ")

    usedSocket.close() #inchide socket

if __name__ == '__main__':
    Main() #apelare main
