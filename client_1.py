import socket
import threading

def set_client_name():
    name = input("Enter your name: ")
    return name


def handle_input(client_socket, client_name):
    while True:
        try:
            message = input()
            client_socket.send((client_name + ": " + message).encode())
        except Exception as e:
            print(f"Error sending message: {e}")
            break


def handle_output(client_socket):
    while True:
        try:
            data = client_socket.recv(1024).decode()
            if not data:
                break
            print(data)
        except Exception as e:
            print(f"Error receiving message: {e}")
            break

    print("Connection closed by server")
    try:
        client_socket.close()
    except Exception as e:
        print(f"Error closing client socket: {e}")


def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect(('localhost', 8885))
    except Exception as e:
        print(f"Error connecting to server: {e}")
        return

    client_name = set_client_name()
    input_thread = threading.Thread(target=handle_input, args=(client_socket, client_name))
    output_thread = threading.Thread(target=handle_output, args=(client_socket,))

    input_thread.start()
    output_thread.start()

    input_thread.join()
    output_thread.join()


def main():
    start_client()


if __name__ == "__main__":
    main()
