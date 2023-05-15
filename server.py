import socket 
import json

def Main():
    host = '0.0.0.0'
    port = 5000

    s = socket.socket()
    s.bind((host, port))
    s.listen(1)
    print("Server is running on 5000")
    c, addr = s.accept()
    print("Connection from " + str(addr))

    while True:
        data = c.recv(1024).decode('utf-8')
        if not data:
            break

        # Process the received data
        employee = json.loads(data)
        employee_json = json.dumps(employee, indent=4)  # Convert the employee data back to JSON with indentation

        print("Received employee details as JSON:")
        print(employee_json)

        # Perform any required operations with the employee details

        # Convert the response to JSON format and send it back
        response = {'status': 'Success'}
        c.send(json.dumps(response).encode('utf-8'))

    c.close()

if __name__ == '__main__':
    Main()
