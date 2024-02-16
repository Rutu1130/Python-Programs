def ChkEven(iNo):
    if(iNo % 2 == 0):
        return True

    else:
        return False

def main():
    bRet = False
    iNo = 0
    print("Enter the number :")
    iNo = int(input())

    bRet = ChkEven(iNo)

    if(bRet == True):
        print(iNo,"Number is Even")
    else:
        print(iNo,"Number is Odd ")



if __name__ == "__main__":
    main()