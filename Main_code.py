#math library (sqrt, cos, sin...) / random for rdn
from math import *
from random import *

#variables
Upper_alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
Lower_alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
Special_characters = ['é','è','ê','ç','à','@',' ','#']

#Dictionnary that will contain the letter and it's encrypted number 
#(One for the Upper list and one for the lower one)
Crypted_upper = {}
Crypted_lower = {}
Crypted_spchar = {}

#Create the crypting algorithm
def crypting_creation():
    #Key to letter assignement for the upper alphabet
    for letter in Upper_alphabet:
        i = False
        while i is False:
            number = randint(0,len(Upper_alphabet)-1)
            if number not in Crypted_upper:
                i = True
            else:
                number = randint(0,len(Upper_alphabet)-1)
        Crypted_upper[number] = letter
    
    #Key to letter assignement for the lower alphabet
    for letter in Lower_alphabet:
        i = False
        while i is False:
            number = randint(0,len(Lower_alphabet)-1)
            if number not in Crypted_lower:
                i = True
            else:
                number = randint(0,len(Lower_alphabet)-1)
        Crypted_lower[number] = letter

    #Key to letter assignement for the lower alphabet
    for character in Special_characters:
        i = False
        while i is False:
            number = randint(0,len(Special_characters)-1)
            if number not in Crypted_spchar:
                i = True
            else:
                number = randint(0,len(Special_characters)-1)
        Crypted_spchar[number] = character

#encrypting algorithm
def encrypt(msg):
    if bool(Crypted_upper) is True:
        if bool(Crypted_lower) is True:
            ...

#message to encode
message_to_encode = input("Message à crypter : ")

crypting_creation()
encrypt(message_to_encode)
    