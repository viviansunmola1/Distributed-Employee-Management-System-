import socket
import json

def Main():
    host = 'localhost'
    port = 5000

    s = socket.socket()
    s.connect((host, port))

    employee = {}

    # Prompt user for employee details
    employee['first_name'] = input("Enter First Name: ")
    employee['last_name'] = input("Enter Last Name: ")
    employee['age'] = input("Enter Age: ")
    employee['employed'] = input("Enter Employment Status: ")

    # Convert employee details to JSON format
    data = json.dumps(employee)

    while True:
        # Send employee data to the server
        s.send(data.encode('utf-8'))

        # Receive and print response from the server
        response = s.recv(1024).decode('utf-8')
        print("Response from server:", response)

        # Optionally, handle any additional logic based on the response

        # Prompt user to quit or continue sending employee details
        message = input("Enter 'q' to quit or continue sending employee details: ")
        if message == 'q':
            break

    s.close()

if __name__ == '__main__':
    Main()
