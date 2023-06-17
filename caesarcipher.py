import time 
print("------WELCOME TO CEASAR CIPHER-----------")
time.sleep(1)

alpha_lower=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
alpha_upper=[i.upper() for i in alpha_lower]

def again():
    again=input("Do want to run again? Y/N \n")
    if again.upper()=="Y":
        time.sleep(1)
        choice()
    elif again.upper()=="N":
        print("Terminating the program...")
        time.sleep(2)
    else:
        print("Invalid Input. Try again.")
        again()

def encode():
    encode=input("Enter the sentence you you want to encode.\n")
    shift = int(input("Enter Shift Value: "))
    output=""
    for i in encode:
        if i.islower():
            index= alpha_lower.index(i)
            index+=shift
            output+=alpha_lower[index]
        else:
            index= alpha_upper.index(i)
            index+=shift
            output+=alpha_upper[index]
    print(f"Ceasar Cipher Text for given Plain Text is {output}")
    time.sleep(2)
    again()
    
def decode():
    decode=input("Enter the sentence you you want to decode.\n")
    shift = int(input("Enter Shift Value: "))
    output=""
    for i in decode:
        if i.islower():
            index= alpha_lower.index(i)
            index-=shift
            output+=alpha_lower[index]
        else:
            index= alpha_upper.index(i)
            index-=shift
            output+=alpha_upper[index]
    print(f"Plain Text for given Caesar Cipher Text is {output}")
    time.sleep(2)
    again()
    

        
        
    

def choice():
    choice=int(input("""Do you want to:
                1. Encrypt Data to Cipher?
                2. Decrypt Data from Cipher?
                (Type 1 or Type 2)\n"""))
    if choice==1:
        print("~~~ENCRYPT DATA TO CEASAR CIPHER~~~")
        encode()
    elif choice==2:
        print("~~~DECRYPT DATA FROM CEASAR CIPHER~~~")
        decode()
    else: 
        print("Invalid choice. Enter again. ")
        choice()
        
choice()    





    
            
    
    
    
    
    
# def decode():
   # decode=input("Enter the sentence you want to decode.\n")