
def CalculatePercentage(Marks,Total):

    iPercentage = (Marks / Total)*100
    return iPercentage

def main():
    iValue1 = 0
    iValue2 = 0
    bRet = 0.0

    print("Enter the marks : ")
    iValue1 = int(input())

    print("Enter the total marks : ")
    iValue2 = int(input())

    bRet = CalculatePercentage(iValue1,iValue2)
    print("Your percentage is :", bRet)


if __name__ == "__main__":
    main()

