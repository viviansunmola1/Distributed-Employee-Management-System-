import socket

def Main():
    host = 'localhost'
    port = 5000

    s = socket.socket()
    s.connect((host,port))

    message = input("You are connected to Server 5000 Please enter message")
    while message != 'q':
        s.send(message.encode('utf-8'))

        data = s.recv(1024).decode('utf-8')
        print ("Messaged recied from server " + str(data))
        message = input("->")
    s.close()

if __name__== '__main__':
    Main()