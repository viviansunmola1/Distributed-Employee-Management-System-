# Distributed Employee Management System - Vivian and Jabed

This project is a distributed employee management system that allows users to input employee details on one machine and display the information on another machine. It utilizes a client-server architecture and communicates using JSON data.

## Requirements

To run this project, you need to have Python installed on your machine.

## Usage

1. Clone the repository to your local machine.

2. Run the server script:

`$ python server.py`


The server will start running on port 5000 and wait for incoming connections.

3. Run the client script on a separate machine:

`$ python server.py`


The client will prompt you to enter the employee details, such as first name, last name, age, and employment status. Once entered, the client will send the data to the server for processing.

4. The server will receive the employee details, process them, and send a response back to the client.

5. The client will display the response received from the server.

6. You can continue entering employee details or enter 'q' to quit.

## Functionality

The project consists of two main components: the server and the client.

### Server

The server script (`server.py`) listens for incoming connections on port 5000 and receives employee details in JSON format. It provides the following endpoints:

- `GET /` - Returns a simple "Hello, World!" message to verify the server is running.
- `POST /data` - Accepts employee details in JSON format, processes them, and sends a response back to the client.

### Client

The client script (`client.py`) prompts the user to enter employee details and sends them to the server for processing. It provides the following features:

- User-friendly CLI interface for entering employee details.
- Conversion of entered details to JSON format.
- Sending the JSON data to the server using a POST request.
- Displaying the response received from the server.





