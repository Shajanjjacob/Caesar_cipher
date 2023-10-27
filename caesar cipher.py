    
alpha=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
       'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def Encryption(plain_text,shift_key):
    cipher_text=""
    for char in plain_text:
        if char in alpha:
            position=alpha.index(char)
            new_position=(position+shift_key)%26
            cipher_text+=alpha[new_position]
        else:
            cipher_text+=char
    print(f" The text after Encryption {cipher_text}")
        
         
    
def Decryption(cipher_text,shift_key):
    plain_text=""
    for char in cipher_text:
        if char in alpha:
            position=alpha.index(char)
            new_position=(position-shift_key)%26
            plain_text+=alpha[new_position]
        else:
            plain_text+=char
    print(f" The text after Decryption {plain_text}")
    

end=False

while not end:
    en_de=input("Enter 'encrypt' for Encryption and 'decrypt' decryption  \n ")        
    text=input("Enter the text :\n").lower()
    key=int(input("Enter the no of shift key:\n "))

    if en_de =='encrypt':
        Encryption(plain_text=text,shift_key=key)
    elif en_de == 'decrypt':
        Decryption(cipher_text=text,shift_key=key)
        
    again=input("Type 'yes' to continue and 'no' to End !!!!")
    
    if again=='no':
        end=True


    
         
 




 
