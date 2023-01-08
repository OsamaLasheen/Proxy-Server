from socket import *
from cache import Cache
from URLFilter import Filter
from error_handler import ErrorHandler

# Create a TCP/IP socket
sock = socket(AF_INET, SOCK_STREAM)

# Bind the socket to the port number 8888
server_address = ('localhost', 8888)
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
            cache = Cache()
            filter = Filter()

            if data:
                print('sending data back to the client')

                # Create a TCP/IP socket
                external_socket = socket(AF_INET, SOCK_STREAM)

                url = data.split()[1][5:].decode("utf-8")

                webUrl = filter.is_blocked(url)

                # Check if this website url is blocked or not
                if webUrl.is_blocked:
                    print('Forbidden Page 403 (Blocked URL !)')
                    # Show the forbidden page (403)
                    ErrorHandler.forbidden(connection=connection)
                    continue

                website = cache.is_cached(website_url=url)

                if website.is_cached:
                    print('The Requested Website is Cached :)')

                    # Sending the cached website to the client
                    connection.sendall(website.response)

                else:
                    server_address = (url, 80)
                    print('starting up on {} port {}'.format(*server_address))

                    try:
                        # Connecting to the destination web server
                        external_socket.connect(server_address)

                        external_socket.sendall(bytes('GET / HTTP/1.1\r\nHost: ' + url + '\r\nConnection: keep-alive\r\nCache-Control: max-age=0\r\nsec-ch-ua: "Not?A_Brand";v="8", "Chromium";v="108", "Brave";v="108"\r\nsec-ch-ua-mobile: ?0\r\nsec-ch-ua-platform: "Windows"\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8\r\nSec-GPC: 1\r\nAccept-Language: en-US,en\r\nSec-Fetch-Site: none\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-User: ?1\r\nSec-Fetch-Dest: document\r\nAccept-Encoding: gzip, deflate, br\r\n\r\n', 'utf-8'))

                        # Receiving the response from the destination web server
                        external_response = external_socket.recv(4096)

                        # Forwarding the response to the client
                        connection.sendall(external_response)

                        # Closing the external socket
                        external_socket.close()

                        # Caching the un-cached website
                        cache.add_website(website_url=url, response=external_response)
                    except gaierror:
                        print('Error 404 happened')

                        # Show the not found page (404)
                        ErrorHandler.not_found(connection=connection)

            else:
                print('no data from', client_address)
                break

    finally:
        # Clean up the connection
        connection.close()
