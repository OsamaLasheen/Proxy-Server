import socket
import error_pages


class ErrorHandler:

    @staticmethod
    def forbidden(connection: socket):
        forbidden_url = bytes('HTTP/1.1 403 Forbidden\r\n' '\n' + error_pages.forbidden_page + '\r\n', 'utf-8')

        # Send the forbidden page to the client via his socket
        connection.sendall(forbidden_url)

    @staticmethod
    def not_found(connection: socket):
        not_found_url = bytes('HTTP/1.1 404 Not Found\r\n' '\n' + error_pages.not_found_page + '\r\n', 'utf-8')

        # Send the not found page to the client via his socket
        connection.sendall(not_found_url)
