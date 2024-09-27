# Program 2 Vigenere Cipher

import string
import sys

#obtain the alphabets to go through
alph = string.ascii_lowercase
ALPH = string.ascii_uppercase

DEBUG = False

if DEBUG:
    print(sys.argv[1])
    print(sys.argv[2])

while 1:
    text = input("")
    #this is the key that we can iterate through
    iteration = list(text)
    K = list(sys.argv[2].upper())
    position_key = 0
    result = []
    
    #decode the cipher
    if sys.argv[1] == '-d':
        #iterate through each letter in the word and correct the position 
        for letter in iteration:

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

    #encode the text
    if sys.argv[1] == '-e':
        #iterate through each letter in the word and correct the position 
        for letter in iteration:

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