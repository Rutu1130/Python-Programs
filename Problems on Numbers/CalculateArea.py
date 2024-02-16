def CalculateArea(iNo):
    pi = 3.14
    Area =  pi * iNo * iNo
    return Area

def main():

    Radius = 0
    iRet = 0
    print("Enter the Radius of circle :")
    Radius = float(input())

    iRet = CalculateArea(Radius)
    print("Area of circle is :",iRet)

if __name__ =="__main__":
    main()
