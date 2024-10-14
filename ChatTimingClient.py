import socket
import time

# Global variables for client configuration
SERVER_IP = 'localhost'
SERVER_PORT = 12345
SHORT_THRESHOLD = 0.5  # Delays shorter than this will be binary '0'
LONG_THRESHOLD = 1.0   # Delays longer than this will be binary '1'
TIMEOUT = 10.0         # Timeout for the socket connection

EXPECTED_BINARY_LENGTH = 64 # We expect 56 bits (7 characters * 8 bits)

def chat_client():
    server_address = (SERVER_IP, SERVER_PORT)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(server_address)

    print(f"Connected to chat server on {SERVER_IP}:{SERVER_PORT}")

    overt_message = ''
    timings = []

    try:
        sock.settimeout(TIMEOUT)
        prev_time = time.time()  # Start tracking the time before receiving the first character

        # Loop to receive data and measure timings
        while len(timings) < EXPECTED_BINARY_LENGTH:
            data = sock.recv(1)  # Receive 1 byte (1 character)
            if not data:
                break

            char = data.decode('utf-8')
            overt_message += char
            print(char, end='', flush=True)

            # Measure the time difference between characters
            curr_time = time.time()
            delay = curr_time - prev_time
            prev_time = curr_time

            # Record the timing
            timings.append(delay)
            if delay < SHORT_THRESHOLD:
                print(f"Timing: {delay:.3f}s -> Interpreted as binary '0'")
            elif delay > LONG_THRESHOLD:
                print(f"Timing: {delay:.3f}s -> Interpreted as binary '1'")

            # Stop when the overt message ends
            if overt_message.endswith("EOF"):
                print("\nOvert message completed.")
                break

        # Ensure enough timings are captured
        while len(timings) < EXPECTED_BINARY_LENGTH:
            # Continue to capture remaining timing data
            curr_time = time.time()
            delay = curr_time - prev_time
            prev_time = curr_time
            timings.append(delay)

            if delay < SHORT_THRESHOLD:
                print(f"Additional timing: {delay:.3f}s -> Interpreted as binary '0'")
            elif delay > LONG_THRESHOLD:
                print(f"Additional timing: {delay:.3f}s -> Interpreted as binary '1'")

        print(f"\nSuccessfully captured {len(timings)} bits.")

    finally:
        sock.close()
        print("\nConnection closed.")

    # Convert timings to binary message
    binary_message = ''.join(['0' if t < SHORT_THRESHOLD else '1' for t in timings[:EXPECTED_BINARY_LENGTH]])
    print(f"\nGenerated binary message: {binary_message}")

    # Convert binary to ASCII
    covert_message = ''
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        if len(byte) == 8:
            covert_message += chr(int(byte, 2))

    print(f"\nCovert message: {covert_message}")

if __name__ == "__main__":
    chat_client()
