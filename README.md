# SimpleChat

A lightweight multi-client chat application built with Python.

The server can handle multiple client connections simultaneously, forwarding messages from one client to all others in real-time.

## Features

- Support for multiple clients
- Real-time message broadcasting
- Simple and lightweight architecture
- Threaded client handling for scalability

## Requirements

- Python 3.10 or higher

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Weisjan/SimpleChat.git
    cd SimpleChat
    ```
2. Start the server:
    ```bash
    python server.py
    ```
3. Launch one or more clients:
    ```bash
    python client_1.py
    python client_2.py
    ```
4. When prompted, enter your name.
5. Start sending messages — all connected clients will receive them!

## Usage

- **Server** (`server.py`):
  - Uses Python's built-in `socket` library to manage TCP connections.
  - Listens on `localhost` at port `8885`.
  - Spawns a new thread for each connected client to handle communication independently.
  - The `handle_client` function reads incoming messages and broadcasts them to all other connected clients.

- **Client** (`client_1.py` and `client_2.py`):
  - Connects to the server at `localhost:8885`.
  - Prompts the user for a username upon connection.
  - Sends user messages to the server (`handle_input` thread).
  - Listens for incoming messages from the server (`handle_output` thread).

> **Note:**  
> `client_1.py` and `client_2.py` are functionally identical and serve to simulate multiple clients in testing.

## Screenshots

*(Optional: you could add some terminal screenshots here showing the chat in action!)*

## Author

- [Jan Weis](https://github.com/Weisjan)
