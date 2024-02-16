
def Maximum(iNo1,iNo2):
    if(iNo1 > iNo2):
        return iNo1
    else:
        return iNo2


def main():
    iValue1 = 0
    iValue2 = 0
    iRet = 0

    print("Enter the First value\n")
    iValue1 = int(input())

    print("Enter the Second value\n")
    iValue2 = int(input())

    iRet = Maximum(iValue1,iValue2)
    print("Largest number is :",iRet)

    return 0

if __name__ == "__main__":
    main()
