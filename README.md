# Vodafone-CDE - Distributed Employee Management System

This project is a distributed employee management system that allows users to input employee details on one machine and display the information on another machine. It utilizes a client-server architecture and communicates using JSON data.

## Requirements

To run this project, you need to have Python installed on your machine.

## Usage

1. Clone the repository to your local machine.

2. Run the server script:
 `$ python3 server.py`

The server will start running on port 5000 and wait for incoming connections.

3. Run the client script on a separate machine:
`$ python3 client.py`

The client will prompt you to enter the employee details, such as first name, last name, age, and employment status. Once entered, the client will send the data to the server for processing.

4. The server will receive the employee details, process them, and send a response back to the client.

5. The client will display the response received from the server.

6. You can continue entering employee details or enter 'q' to quit.

# Functionality
1. The server script (server.py) listens for incoming connections on port 5000 and receives employee details in JSON format.

2. The client script (client.py) prompts the user to enter employee details, converts them to JSON, and sends them to the server.

3. The server processes the received data, performs any necessary operations, and sends a response back to the client.

4. The client displays the response received from the server.
