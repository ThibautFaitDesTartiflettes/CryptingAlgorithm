#math library (sqrt, cos, sin...) / random for creating alea
from math import *
from random import *

#variables
message_to_encode = ""
Upper_alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
Lower_alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
Special_characters = ['é','è','ê','ç','à','@',' ','#',',','.','!','?',':',';','/','(',')','{','}','&','-','_','[',']','|','°','+','=','*','$','£','€','¤','µ','%','ù','§','<','>',"'",'"']
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
    for maj_letter in Upper_alphabet:
        i = False
        while i is False:
            maj_number = randint(0,len(Upper_alphabet)-1)
            if maj_number not in Crypted_upper.values():
                i = True
            else:
                maj_number = randint(0,len(Upper_alphabet)-1)
        Crypted_upper[maj_letter] = maj_number
    
    #Key to letter assignement for the lower alphabet
    for min_letter in Lower_alphabet:
        i = False
        while i is False:
            min_number = randint(0,len(Lower_alphabet)-1)
            if min_number not in Crypted_lower.values():
                i = True
            else:
                min_number = randint(0,len(Lower_alphabet)-1)
        Crypted_lower[min_letter] = min_number

    #Key to letter assignement for the lower alphabet
    for character in Special_characters:
        i = False
        while i is False:
            sp_number = randint(0,len(Special_characters)-1)
            if sp_number not in Crypted_spchar.values():
                i = True
            else:
                sp_number = randint(0,len(Special_characters)-1)
        Crypted_spchar[character] = sp_number
    
        #Key to letter assignement for the lower alphabet
    for num_number in Numbers:
        i = False
        while i is False:
            enum_number = randint(0,len(Numbers)-1)
            if enum_number not in Crypted_numbers.values():
                i = True
            else:
                enum_number = randint(0,len(Numbers)-1)
        Crypted_numbers[num_number] = enum_number

#Encrypting algorithm
def encrypt(msg):
    crypted_message = ""
    crypted_position = 0
    #Test if all the crypted lists are files so the encrypting process will work well
    if bool(Crypted_upper) is True and bool(Crypted_lower) is True and bool(Crypted_spchar) is True and bool(Crypted_numbers) is True:
        for position in range(len(msg)):
            character = msg[position]
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

#Find the key associated with the value in parameter IN a specific dictionnary
def find_key(value, dictionnary):
    for key, val in dictionnary.items():
        if value == val:
            return key

#Decrypting algorithm
def decrypt(msg):
    uncrypted_position = 0
    uncrypted_message = ""
    uncrypted_character = ""
    #Test if all the crypted lists are files so the decrypting process will work well
    if bool(Crypted_upper) is True and bool(Crypted_lower) is True and bool(Crypted_spchar) is True and bool(Crypted_numbers) is True:
        for position in range(len(msg)):
            crypted_character = msg[position]
            if crypted_character in Upper_alphabet:
                uncrypted_position = Upper_alphabet.index(crypted_character)
                uncrypted_message += find_key(uncrypted_position, Crypted_upper)
            if crypted_character in Lower_alphabet:
                uncrypted_position = Lower_alphabet.index(crypted_character)
                uncrypted_message += find_key(uncrypted_position, Crypted_lower)
            if crypted_character in Special_characters:
                uncrypted_position = Special_characters.index(crypted_character)
                uncrypted_message += find_key(uncrypted_position, Crypted_spchar)
            if crypted_character in Numbers:
                uncrypted_position = Numbers.index(crypted_character)
                uncrypted_message += find_key(uncrypted_position, Crypted_numbers)
        return uncrypted_message
    else:
        return("Les paramètres de cryptages ne sont pas initialisés") 

#Fill the crypting list
crypting_creation()
#Message to encode
message_to_encode = input("Message à crypter : ")
print("Votre message est : " + message_to_encode)
encrypted_message = encrypt(message_to_encode)
print("Votre message crypté est : " + encrypted_message)
#Decoding the message
print("Le message décodé est : " + decrypt(encrypted_message))
    