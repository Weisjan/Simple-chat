import socket
import threading

clients = []

def handle_client(client_socket, client_address):
    while True:
        try:
            data = client_socket.recv(1024).decode()
            if not data:
                break
            print(f"Received message from {client_address}: {data}")
            broadcast(data, client_socket)
        except Exception as e:
            print(f"Error handling message from {client_address}: {e}")
            break

    print(f"Connection with {client_address} closed")
    try:
        client_socket.close()
    except Exception as e:
        print(f"Error closing client socket: {e}")
    finally:
        if client_socket in clients:
            clients.remove(client_socket)


def broadcast(message, sender_socket):
    for client_socket in clients:
        if client_socket != sender_socket:
            try:
                client_socket.send(message.encode())
            except Exception as e:
                print(f"Error broadcasting to client: {e}")
                try:
                    client_socket.close()
                except:
                    pass
                if client_socket in clients:
                    clients.remove(client_socket)


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server_socket.bind(('localhost', 8885))
        server_socket.listen(5)
        print("Server started, waiting for connections...")
    except Exception as e:
        print(f"Error setting up server: {e}")
        return

    while True:
        try:
            client_socket, client_address = server_socket.accept()
            print(f"Connection established with {client_address}")
            clients.append(client_socket)
            client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
            client_thread.start()
        except Exception as e:
            print(f"Error accepting new connection: {e}")


def main():
    start_server()


if __name__ == "__main__":
    main()
