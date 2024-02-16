def RangeDisplayEven(iStart,iEnd):
    
    if(iStart % 2 !=0):
        iStart +=1
    for iCnt in range(iStart,iEnd+1,2):
        print(iCnt)
    print("\n")

def main():

    print("enter Staring Value : ")
    iValue1 = int(input())

    print("Enter Ending Value : ")
    iValue2 = int(input())

    RangeDisplayEven(iValue1,iValue2)


if __name__ == "__main__":
    main()