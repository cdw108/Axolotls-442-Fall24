import sys

# Define the sentinel value as a bytearray for marking the end of hidden data
SENTINEL = bytearray([0x00, 0xFF, 0x00, 0x00, 0xFF, 0x00])

# Function to read a file in binary mode and return its contents as a bytearray
def read_file(filepath):
    try:
        with open(filepath, 'rb') as file:
            return bytearray(file.read())
    except FileNotFoundError:
        # Print error and exit if the file is not found
        print(f"Error: File '{filepath}' not found.")
        sys.exit(1)

# Function to write binary data directly to stdout
def write_to_stdout(data):
    sys.stdout.buffer.write(data)

# Function to store hidden data using the bit method
def store_bit(wrapper, hidden, offset):
    # Iterate over each byte in the hidden file
    for byte in hidden:
        for bit in range(8):
            if offset >= len(wrapper):
                print("Error: Offset exceeds wrapper size.")
                sys.exit(1)
            # Clear the least significant bit (LSB) of the wrapper byte
            wrapper[offset] &= 0b11111110
            # Set the LSB to the most significant bit (MSB) of the hidden byte
            wrapper[offset] |= (byte & 0b10000000) >> 7
            # Shift the hidden byte left to prepare the next bit for storage
            byte = (byte << 1) & 0xFF
            # Move to the next byte in the wrapper
            offset += 1

    # Store the sentinel value bit-by-bit in the wrapper
    for byte in SENTINEL:
        for bit in range(8):
            if offset >= len(wrapper):
                print("Error: Offset exceeds wrapper size.")
                sys.exit(1)
            wrapper[offset] &= 0b11111110
            wrapper[offset] |= (byte & 0b10000000) >> 7
            byte = (byte << 1) & 0xFF
            offset += 1

# Function to store hidden data using the byte method
def store_byte(wrapper, hidden, offset, interval):
    i = 0
    # Iterate over each byte in the hidden file
    while i < len(hidden):
        if offset >= len(wrapper):
            print("Error: Offset and interval exceed wrapper size.")
            sys.exit(1)
        # Directly replace the byte in the wrapper at the given offset
        wrapper[offset] = hidden[i]
        offset += interval
        i += 1

    # Store the sentinel value byte-by-byte in the wrapper
    i = 0
    while i < len(SENTINEL):
        if offset >= len(wrapper):
            print("Error: Offset and interval exceed wrapper size.")
            sys.exit(1)
        wrapper[offset] = SENTINEL[i]
        offset += interval
        i += 1

# Function to retrieve hidden data using the bit method
def retrieve_bit(wrapper, offset):
    hidden = bytearray()
    while offset < len(wrapper):
        byte = 0
        # Rebuild each byte from 8 bits hidden in the LSBs of 8 wrapper bytes
        for bit in range(8):
            byte |= (wrapper[offset] & 0b00000001)
            if bit < 7:
                byte <<= 1
            offset += 1

        hidden.append(byte)
        # Check if the last bytes match the sentinel; if so, stop extraction
        if hidden[-len(SENTINEL):] == SENTINEL:
            hidden = hidden[:-len(SENTINEL)]  # Remove the sentinel from the output
            break

    # Output the hidden file data to stdout
    write_to_stdout(hidden)

# Function to retrieve hidden data using the byte method
def retrieve_byte(wrapper, offset, interval):
    hidden = bytearray()
    while offset < len(wrapper):
        byte = wrapper[offset]
        hidden.append(byte)
        # Check if the last bytes match the sentinel; if so, stop extraction
        if hidden[-len(SENTINEL):] == SENTINEL:
            hidden = hidden[:-len(SENTINEL)]  # Remove the sentinel from the output
            break
        offset += interval

    # Output the hidden file data to stdout
    write_to_stdout(hidden)

# Main function to parse command-line arguments and execute the appropriate method
def main():
    # Ensure the minimum required number of arguments are present
    if len(sys.argv) < 5:
        print("Usage: python Steg.py -(sr) -(bB) -o<val> [-i<val>] -w<val> [-h<val>]")
        sys.exit(1)

    # Parse the mode (store or retrieve) and method (bit or byte)
    mode = sys.argv[1]
    method = sys.argv[2]
    offset = int(sys.argv[3][2:])
    interval = 1  # Default interval
    wrapper_file = ""
    hidden_file = ""

    # Parse additional command-line arguments for interval, wrapper, and hidden file
    for arg in sys.argv[4:]:
        if arg.startswith("-i"):
            interval = int(arg[2:])
        elif arg.startswith("-w"):
            wrapper_file = arg[2:]
        elif arg.startswith("-h"):
            hidden_file = arg[2:]

    # Read the wrapper file into a bytearray
    wrapper = read_file(wrapper_file)

    # Set a minimum offset for image files (e.g., JPEG files)
    if wrapper_file.endswith(('.jpg', '.jpeg', '.png')):
        if offset < 1024:
            print("Warning: Setting offset to 1024 to avoid corrupting image headers.")
            offset = 1024

    if mode == "-s":  # Storing data
        if not hidden_file:
            print("Error: Hidden file must be specified for storing.")
            sys.exit(1)
        hidden = read_file(hidden_file)

        if method == "-b":
            store_bit(wrapper, hidden, offset)
        elif method == "-B":
            store_byte(wrapper, hidden, offset, interval)
        else:
            print("Error: Invalid method specified. Use -b or -B.")
            sys.exit(1)

        # Output the modified wrapper with hidden data to stdout
        write_to_stdout(wrapper)

    elif mode == "-r":  # Retrieving data
        if method == "-b":
            retrieve_bit(wrapper, offset)
        elif method == "-B":
            retrieve_byte(wrapper, offset, interval)
        else:
            print("Error: Invalid method specified. Use -b or -B.")
            sys.exit(1)

    else:
        print("Error: Invalid mode specified. Use -s or -r.")
        sys.exit(1)

# Entry point for the script
if __name__ == "__main__":
    main()
