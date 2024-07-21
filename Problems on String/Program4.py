
# Accept character from user and check whether it is Alphabet or not
#(0 - 9)


def ChkDigit(ch):

    if(ch >= "0" and ch <= "9"):
        return True
    else:
        return False



def main():

    cValue = input("Enter the Digit : ")

    bRet = ChkDigit(cValue)

    if(bRet == True):
        print("It is Digit.")

    else:
        print("It is not a Digit.")

if __name__ == "__main__":
    main()