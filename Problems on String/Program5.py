#/*Accept character from user . If character is small display its corresponding capital ,
#and if it small then display its corresponding capital character . 
# In other cases display as it is.

# Input : Q
# Output : q


def Display(ch):

    if(ch >= 'A' and ch <= "Z"):
        return chr(ord(ch) + 32)
    elif(ch >='a' and ch <='z'):
        return chr(ord (ch) - 32)
    
    else:
        return ch


def main():

    Cvalue = input("Enter the Character : ")

    cRet = Display(Cvalue)

    print("Converted letters are:",cRet)

    return 0

if __name__ == "__main__":
    main()