import sys

buffer_size = 4096

#xor the whole thing
def xor(data, key):
    result = bytearray()
    for data, key in zip(data, key):
        result.append(data ^ key)
    return result


#read the key
with open("key2-1", "rb") as key_file:
    key = bytearray(key_file.read())

#read the text
binary_data = sys.stdin.buffer.read()
if(len(binary_data) != len(key)):
    sys.exit()
#xorthem
result = xor(binary_data, key)


#print the result
sys.stdout.buffer.write(result)