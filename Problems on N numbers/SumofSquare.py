# write a program to print Sum of Square of  N numbers 

def SumOfSquare(iNo):
    iCnt = 1
    iSum = 0

    while(iCnt <= iNo):
        iSum = iSum + (iCnt * iCnt)
        iCnt = iCnt + 1
    print("Sum of Square of N numbers are : ",iSum)

def main():

    print("Enter value that yuo want :")
    iValue = int(input())

    SumOfSquare(iValue)

if __name__ == "__main__":
    main()