# write a program to print Sum of N numbers 

def Display(iNo):
    i = 1
    iSum = 0
    while (i <=iNo):
        iSum = i + iSum 
        i = i+1
    print("Sum of N numbers are :",iSum)

def main():
   
    print("Enter the value that you want to print : ")
    Value= int(input())
    Display(Value)

if __name__ == "__main__":
    main()