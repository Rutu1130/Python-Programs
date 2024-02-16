def CheckPrime(iNo):

    
    if(iNo < 0):
        iNo = -iNo

    for i in range (iNo):
        if(iNo % (iNo /2) == 0):
            return False
    return True
    

def main():
    iValue = 0

    bret = False

    print("Enter the first number : \n")
    iValue = int(input())

    bret = CheckPrime(iValue1)

    if bret:
        print( "is a prime number")
    else:
        print( "is Not a prime number")

    return 0

if __name__ == "__main__":
    main()
