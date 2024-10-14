import socket
import time

# Global variables for server configuration
SERVER_IP = 'localhost'
SERVER_PORT = 12345
SHORT_DELAY = 0.2  # Short delay for binary '0'
LONG_DELAY = 1.0   # Long delay for binary '1'

def chat_server():
    server_address = (SERVER_IP, SERVER_PORT)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(server_address)
    server_socket.listen(1)

    print(f"Chat server is waiting for a connection on {SERVER_IP}:{SERVER_PORT}...")

    conn, addr = server_socket.accept()
    print(f"Connected to {addr}")

    # Overt message to send to the client
    overt_message = "The garden blooms brightly in spring, a colorful sight to seeEOF"
    
    # Covert binary message (e.g., binary for "I am low")
    covert_binary = "0100100100100000011000010110110100100000011011000110111101110111"

    print(f"Covert binary message: {covert_binary}")

    # Send each character of the overt message with timing delays based on covert binary
    for i, char in enumerate(overt_message):
        # Send one character at a time with conn.send
        if i < len(covert_binary) and covert_binary[i] == '0':
            time.sleep(SHORT_DELAY)  # Send short delay for binary '0'
            conn.send(char.encode('utf-8'))
            print(f"Sent char '{char}' with short delay ({SHORT_DELAY} seconds) for binary '0'")
        else:
            time.sleep(LONG_DELAY)  # Send long delay for binary '1'
            conn.send(char.encode('utf-8'))
            print(f"Sent char '{char}' with long delay ({LONG_DELAY} seconds) for binary '1'")

    print("Overt message sent. Waiting to send additional timing data...")

    # Ensure remaining bits are sent
    if len(covert_binary) > len(overt_message):
        remaining_bits = covert_binary[len(overt_message):]
        for bit in remaining_bits:
            if bit == '0':
                time.sleep(SHORT_DELAY)
                print(f"Sent extra delay for binary '0'")
            else:
                time.sleep(LONG_DELAY)
                print(f"Sent extra delay for binary '1'")

    print("All timing data sent. Closing connection.")
    conn.close()

if __name__ == "__main__":
    chat_server()
