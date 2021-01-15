import socket
import time
import random

def Main():
    host = "37.120.249.45" #asignare adresa
    port = 8210 #asignare port
    mainSocket = socket.socket() #creare socket
    mainSocket.bind((host,port)) #bind socket
    jokes = ["\nWhat’s the best thing about Switzerland? \nI don’t know, but the flag is a big plus.",
             "\nI invented a new word! \nPlagiarism",
             "\nWhy don’t scientists trust atoms? \nBecause they make up everything.",
             "\nHow do you drown a hipster?\nThrow him in the mainstream.",
             "\nHow does Moses make tea?\nHe brews.",
             "\nWhy don’t Calculus majors throw house parties?\nBecause you should never drink and derive."]

    mainSocket.listen(1) #listen pe socket
    conn, addr = mainSocket.accept() #accepta conexiunea
    print ("Connection from: " + str(addr))

    while True: #bucla infinita pentru transmiterea mesajelor
        data = conn.recv(1024).decode() #primire mesaj
        if not data:
            break

        data = str(data)
        print ("User>> " + str(data)) #functionalitati
        if data == 'time':
            data = str(time.strftime("%H:%M:%S %d/%m/%y",time.localtime()))
        elif data=='joke':
            data = jokes[random.randint(0,len(jokes)-1)]
        elif data=='rando':
            data = str(random.randint(0,10));
        else:
            data = input("> ")
        conn.send(data.encode()) #trimite mesaj pe socket

    conn.close() #inchide conexiunea

if __name__ == '__main__':
    Main() #apel main
