# Program 1 Binary Decoder
DEBUG=False


inp = input()
if (len(inp) % 7 == 0):
    bitLength = 7
elif (len(inp) % 8 == 0):
    bitLength = 8
else:
    bitLength = 9

#force bitlength if known value
forcebitLength = False
if (forcebitLength == True):
    bitLength = 7

strBinOut = [inp[i:i+bitLength] for i in range(0, len(inp), bitLength)] # I found the idea for this line on stackoverflow
binOut = [int(strBinOut[i], 2) for i in range(0, len(strBinOut))]
output = ''.join(chr(binOut[i]) for i in range(0, len(binOut)))
print(output)

if DEBUG:
    print(f"Input: {inp}")
    print(f"Split binary output: {strBinOut}")
    print(f"Output: {output}")
