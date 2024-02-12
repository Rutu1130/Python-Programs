# Accept number from user and print Even numbers 

def DispEven(iNo):
    iCnt = 1
    while(iCnt<= iNo):
        if( (iCnt % 2) == 0):
            print(iCnt)
        iCnt = iCnt + 1

def main():

    iValue = 0
    print("Enter the Number : ")
    iValue = int(input())

    DispEven(iValue)

if __name__ == "__main__":
    main()