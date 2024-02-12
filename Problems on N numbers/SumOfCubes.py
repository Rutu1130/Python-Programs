# write a program to print Sum of Cube of  N numbers 

def SumOfCube(iNo):
    iCnt = 1
    iSum = 0

    while(iCnt <= iNo):
        iSum = iSum + (iCnt * iCnt * iCnt)
        iCnt = iCnt + 1
    print("Sum of Cubes of N numbers are : ",iSum)

def main():

    print("Enter value that yuo want :")
    iValue = int(input())

    SumOfCube(iValue)

if __name__ == "__main__":
    main()