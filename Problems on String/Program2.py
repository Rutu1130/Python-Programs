# Check whether Charcter is capital or not

def ChkCapital(ch):

    if(ch >= "A" and ch <= "Z"):
        return True
    else:
        return False



def main():

    cValue = input("Enter the Character : ")

    bRet = ChkCapital(cValue)

    if(bRet == True):
        print("It is Capital Character.")

    else:
        print("It is not a Capital Character.")

if __name__ == "__main__":
    main()