#math library (sqrt, cos, sin...) / random for rdn
from math import *
from random import *

#variables
message_to_encode = ""
Upper_alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
Lower_alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
Special_characters = ['é','è','ê','ç','à','@',' ','#',',','.','!','?',':',';','/','(',')','{','}','&','-','_','[',']','|','°','+','=','*','$','£','€','¤','µ','%','ù','§','<','>']
Numbers = ['0','1','2','3','4','5','6','7','8','9']

#Dictionnary that will contain the letter and it's encrypted number 
#(One for the Upper list and one for the lower one)
Crypted_upper = {}
Crypted_lower = {}
Crypted_spchar = {}
Crypted_numbers = {}

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
        Crypted_upper[letter] = number
    
    #Key to letter assignement for the lower alphabet
    for letter in Lower_alphabet:
        i = False
        while i is False:
            number = randint(0,len(Lower_alphabet)-1)
            if number not in Crypted_lower:
                i = True
            else:
                number = randint(0,len(Lower_alphabet)-1)
        Crypted_lower[letter] = number

    #Key to letter assignement for the lower alphabet
    for character in Special_characters:
        i = False
        while i is False:
            number = randint(0,len(Special_characters)-1)
            if number not in Crypted_spchar:
                i = True
            else:
                number = randint(0,len(Special_characters)-1)
        Crypted_spchar[character] = number
    
        #Key to letter assignement for the lower alphabet
    for number in Numbers:
        i = False
        while i is False:
            enum_number = randint(0,len(Numbers)-1)
            if enum_number not in Crypted_numbers:
                i = True
            else:
                enum_number = randint(0,len(Numbers)-1)
        Crypted_numbers[number] = enum_number

#encrypting algorithm
def encrypt(msg):
    crypted_message = ""
    crypted_position = 0
    if bool(Crypted_upper) is True and bool(Crypted_lower) is True and bool(Crypted_spchar) is True:
        for position in range(len(message_to_encode)):
            character = message_to_encode[position]
            if character in Crypted_upper:
                crypted_position = Crypted_upper[character]
                crypted_message += Upper_alphabet[crypted_position]
            elif character in Crypted_lower:
                crypted_position = Crypted_lower[character]
                crypted_message += Lower_alphabet[crypted_position]
            elif character in Crypted_spchar:
                crypted_position = Crypted_spchar[character]
                crypted_message += Special_characters[crypted_position]
            elif character in Crypted_numbers:
                crypted_position = Crypted_numbers[character]
                crypted_message += Numbers[crypted_position]
        return crypted_message 
    else:
        return("Les paramètres de cryptages ne sont pas initialisés") 

#Fill the crypting list
crypting_creation()
#message to encode
message_to_encode = input("Message à crypter : ")
print("Votre message est : " + message_to_encode)
print("Votre message crypté est : " + encrypt(message_to_encode))

    