
def Average(iNo1,iNo2,iNo3):
    return(iNo1 + iNo2 + iNo3) / 3

def main():
    iValue1 = 0
    iValue2 = 0
    iValue3 = 0
    iRet = 0

    print("Enter the First value\n")
    iValue1 = int(input())

    print("Enter the Second value\n")
    iValue2 = int(input())

    print("Enter the Second value\n")
    iValue3 = int(input())

    iRet = Average(iValue1,iValue2,iValue3)
    print("Average is :",iRet)
    return 0 

if __name__ == "__main__":
    main(pytho)