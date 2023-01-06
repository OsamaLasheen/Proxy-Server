from socket import *
import sys

# Create a TCP/IP socket
sock = socket(AF_INET, SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 8080)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(4096)
            print('received {!r}'.format(data))
            if data:
                print('sending data back to the client')
                # connection.sendall(data)

                # Create a TCP/IP socket
                external_sock = socket(AF_INET, SOCK_STREAM)

                # Bind the socket to the port
                server_address = (data.split()[1][5:].decode("utf-8"), 8080)
                print('starting up on {} port {}'.format(*server_address))
                external_sock.connect(server_address)
                external_sock.sendall(data)

                print(external_sock.recv(4096))
            else:
                print('no data from', client_address)
                break

    finally:
        # Clean up the connection
        connection.close()
