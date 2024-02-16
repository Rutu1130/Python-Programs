

def RangeDisplay(iStart,iEnd):
    iCnt = 0
    if(iStart > iEnd):
        print("Invalid Range")

    else:
        for iCnt in range(iStart,iEnd+1):
            print(iCnt)
    print("\n")


def main():
   
    print("Enter the starting value : ")
    iValue1 = int(input())
    print("Enter the Ending value : ")
    iValue2 = int(input())

    print("Range is : ")
    RangeDisplay(iValue1,iValue2)
  
    return 0 

if __name__ == "__main__":
    main()