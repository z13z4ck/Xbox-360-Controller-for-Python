import socket
import threading


class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            # client.settimeout(60)
            # threading.Thread(target = self.listenToClient,args = (client,address)).start()
            # return client, address
            self.listenToClient(client, address)

    def listenToClient(self, client, address):
        size = 1024
        while True:
            try:
                data = client.recv(size)

                try:
                    if data:
                        # Set the response to echo back the recieved data
                        response = data
                        print(data)
                        # client.send(response)
                    else:
                        raise socket.error('Client disconnected')

                except KeyboardInterrupt:
                    print("[!] Exiting..!")
                    client.close()
                    raise socket.error('Client disconnected')

            except KeyboardInterrupt:
                client.close()
                return False

    def close_socket(self):
        self.sock.close()

if __name__ == "__main__":
    while True:
        port_num = input("Port? ")
        try:
            port_num = int(port_num)
            break
        except ValueError:
            pass

    try:
        ThreadedServer('', port_num).listen()
    except KeyboardInterrupt:
        print("Exiting!")
