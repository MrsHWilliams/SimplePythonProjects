#!/usr/bin/env python3
"""
Created on Wed Jan 29 02:19:24 2020

@author: suleman
"""
def encrypt_message(message, key):
    msg = ''
    for char in message:
        if char != ' ':
            if ord(char) + key > 122:
                new_key = ord(char) + key - 122
                msg = msg + chr(96 + new_key)
            else:
                msg = msg + chr(ord(char)+key)
        else:
            msg = msg + ' '
            
    return msg

def decrypt_message(message, key):
    msg = ''
    for char in message:
        if char != ' ':
            if ord(char) - key < 97:
                new_key = 96 - (ord(char) - key)
                msg = msg + chr(122 - new_key)
            else:
                msg = msg + chr(ord(char)-key)
        else:
            msg = msg + ' '
    return msg

while 1:
    i = input("Press 1 for encrypting a message\nPress 2 for decrypting a message \nYour choice: ")
    
    if i =='1':
        msg = input("Enter a message to encrypt: ")
        key = int(input("Enter the key: "))
        print("Here's the encrpyed message: ",encrypt_message(msg.lower(), key))
    elif i=='2':
        msg = input("Enter a message to decrypt: ")
        key = int(input("Enter the key you used: "))
        print("Here's the decrypted message: ",decrypt_message(msg.lower(), key))
    else:
        print("Wrong choice, program exiting...")
        break

"""Output:
roy@roy:~/Desktop/work$ python3 caesar.py
Press 1 for encrypting a message
Press 2 for decrypting a message 
Your choice: 1
Enter a message to encrypt: suleman
Enter the key: 5
Here's the encrpyed message:  xzqjrfs
Press 1 for encrypting a message
Press 2 for decrypting a message 
Your choice: 2
Enter a message to decrypt: xzqjrfs
Enter the key you used: 5
Here's the decrypted message:  suleman
Press 1 for encrypting a message
Press 2 for decrypting a message 
Your choice: 

"""
