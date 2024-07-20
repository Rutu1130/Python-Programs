# Check whether Charcter is small or not

def ChkCapital(ch):

    if(ch >= "a" and ch <= "z"):
        return True
    else:
        return False



def main():

    cValue = input("Enter the Character : ")

    bRet = ChkCapital(cValue)

    if(bRet == True):
        print("It is Small Character.")

    else:
        print("It is not a Small Character.")

if __name__ == "__main__":
    main()