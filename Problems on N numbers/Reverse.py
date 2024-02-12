# write a program to print N numbers in Reverse order

def Display(iNo):
  
    while (iNo >= 1):
        print(iNo)
        iNo = iNo-1

def main():
    Value = 0
    print("Enter the value that you want to print : ")
    Value= int(input())
    Display(Value)

if __name__ == "__main__":
    main()