# Program 1 Binary Decoder

# This contains some methods to convert between binary and ascii
import binascii
# Example from geeksforgeeks.org (we do not need to use exactly this, just might be a good starting point)

# Initializing a binary string in the form of
# 0 and 1, with base of 2
binary_int = int("11000010110001001100011", 2);
 
# Getting the byte number
byte_number = binary_int.bit_length() + 7 // 8
 
# Getting an array of bytes
binary_array = binary_int.to_bytes(byte_number, "big")
 
# Converting the array into ASCII text
ascii_text = binary_array.decode()
 
# Getting the ASCII value
print(ascii_text)