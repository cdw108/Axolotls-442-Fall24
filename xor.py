import sys

buffer_size = 4096

def xor(data, key):
    result = bytearray()
    for data, key in zip(data, key):
        result.append(data ^ key)
    return result


#read the key
with open("key", "rb") as key_file:
    key = bytearray(key_file.read())

#read the text
binary_data = sys.stdin.buffer.read()

#xorthem
result = xor(binary_data, key)



sys.stdout.buffer.write(result)