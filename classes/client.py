from socket import *
import json


# def package(_type: type, _object: object):
#     tran_pak = {"type": _type, "object": _object}
#     _json = json.dumps(tran_pak)
#     return _json


class Client:
    IP: str
    PORT: int
    BUFFLEN: int

    def __init__(self):
        self.IP = "localhost"
        self.PORT = 7896
        self.BUFFLEN = 10240

    def data_socket(self):
        data_socket = socket(AF_INET, SOCK_STREAM)
        data_socket.connect((self.IP, self.PORT))
        return data_socket

    def to_trans(self, _json):
        data_socket = socket(AF_INET, SOCK_STREAM)
        data_socket.connect((self.IP, self.PORT))

        while True:
            data_socket.send(_json)
            recved = data_socket.recv(self.BUFFLEN)
            if not recved:
                break

        data_socket.close()
