from socket import *

# def unpackage(_json):
#     data = json.loads(_json)
#     _type = data["type"]
#     _object = data["object"]
#     return _type, _object


class Server:
    IP: str
    PORT: int
    BUFFLEN: int

    def __init__(self):
        self.IP = "localhost"
        self.PORT = 7896
        self.BUFFLEN = 1024

    def listen_socket(self):
        listen_socket = socket(AF_INET, SOCK_STREAM)
        listen_socket.bind((self.IP, self.PORT))
        listen_socket.listen(1)
        data_socket, addr = listen_socket.accept()
        return data_socket

    def to_listen(self):
        listen_socket = socket(AF_INET, SOCK_STREAM)
        listen_socket.bind((self.IP, self.PORT))
        listen_socket.listen(1)
        data_socket, addr = listen_socket.accept()
        print("Address of connect: ", addr)

        while True:
            recved = data_socket.recv(self.BUFFLEN)
            if not recved:
                break

            _json = recved

            print(f"Received message: {_json}")
            data_socket.send(f"Server received message {_json}".encode())

        data_socket.close()
        listen_socket.close()
