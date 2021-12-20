# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 14:26:52 2021

@author: hashim
"""


def encrypt(text,s):
    result = ""
 
    # traverse text
    for i in range(len(text)):
        char = text[i]
 
        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
 
        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
            
    return result
 
def decrypt(text,s):
    result = ""
 
    # traverse text
    for i in range(len(text)):
        char = text[i]
 
        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) - s-65) % 26 + 65)
 
        # Encrypt lowercase characters
        else:
            result += chr((ord(char) - s - 97) % 26 + 97)
            
    return result    
#check the above function
text1 = "DEFENDTHEFORT"
s = 7

print ("original Text  : " + text1)
print ("Shift : " + str(s))
print ("encrypted text: " + encrypt(text1,s))
text2 = encrypt(text1,s)
s = 7

print ("encrypted Text  : " + text2)
print ("Shift : " + str(s))
print ("decrypted text: " + decrypt(text2,s))