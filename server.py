import socket 
def Main():
    host = '0.0.0.0'
    port = 5000

    s = socket.socket()
    s.bind((host, port))
    s.listen(1)
    print("Server is running on 5000")
    c,addr = s.accept()
    print("Connction from " + str(addr))

    while True:
        data = c.recv(1024).decode('utf-8')
        if not data:
            break
        print("The connected user says "+ data)
        data = data.upper()
        print("Sending back in upper case!: " + data)
        c.send(data.encode('utf-8'))
    c.close()
if __name__=='__main__':
    Main()




