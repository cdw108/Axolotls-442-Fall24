import string
import sys
import os

#obtain the alphabets to go through
alph = string.ascii_lowercase
ALPH = string.ascii_uppercase

DEBUG = False

if DEBUG:
    print(sys.argv[1])
    print(sys.argv[2])

def decode(text):
#iterate through each letter in the word and correct the position 

    #this is the key that we can iterate through
    iteration = list(text)
    K = list(sys.argv[2].upper())
    position_key = 0
    result = []

    for letter in iteration:
        #there is a space so ignore it
        if K[position_key] == ' ':
            position_key += 1

        #the letter is uppercase
        if letter.isupper():
            #adjust the letter in the text by the key
            result.append(ALPH[ALPH.index(letter) - ALPH.index(K[position_key])])
            #iterate through the key 
            position_key = (position_key + 1) % len(K)

        #the letter is lowercase and repeats the if statement above
        elif letter.islower():
            result.append(alph[alph.index(letter) - ALPH.index(K[position_key])])
            position_key = (position_key + 1) % len(K)
        
        #this is not a letter so just add it
        else:
            result.append(letter)

    #combine the list into a string and output it
    String = ''.join(result)
    print(String)
    return String

def encode(text):
    #iterate through each letter in the word and correct the position 
        #this is the key that we can iterate through
    iteration = list(text)
    K = list(sys.argv[2].upper())
    position_key = 0
    result = []

    for letter in iteration:
        if K[position_key] == ' ':
            position_key += 1
            
        #the letter is uppercase
        if letter.isupper():

            if DEBUG:
                print(ALPH.index(letter))
                print(ALPH.index(K[position_key]))

            #adjust the letter in the text by the key
            result.append(ALPH[(ALPH.index(letter) + ALPH.index(K[position_key])) % 26])
            #iterate through the key 
            position_key = (position_key + 1) % len(K)

        #the letter is lowercase and repeats the if statement above
        elif letter.islower():

            if DEBUG:
                print(alph.index(letter))
                print(ALPH.index(K[position_key]))

            result.append(alph[(alph.index(letter) + ALPH.index(K[position_key])) % 26])
            position_key = (position_key + 1) % len(K)
        
        #this is not a letter so just add it
        else:
            result.append(letter)

    #combine the list into a string and output it
    String = ''.join(result)
    print(String)
    return String

while 1:
    text = input("")
    output = ''

    if len(sys.argv) > 2:   
        #decode the cipher
        if sys.argv[1] == '-d':
            output = decode(text)

        #encode the text
        if sys.argv[1] == '-e':
            output = encode(text)
    
    else:
        #decode the cipher
        if sys.argv[1] == '-d' and sys.argv[3] == '>':
            output = decode(text)
            with open(sys.argv[4],'w') as file:
                file.write(output)
        #read the file and decrypt it
        else:
            with open(sys.argv[4],'w') as file:
                content = file.read()
                output = decode(content)
        #encode the text
        if sys.argv[1] == '-e' and sys.argv[3] == '>':
            output = encode(text)
            with open(sys.argv[4],'w') as file:
                file.write(output)
        else:
            with open(sys.argv[4],'w') as file:
                content = file.read()
                output = decode(content)
