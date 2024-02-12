# write a program to print N numbers 

def Display(iNo):
    i = 1
    while (i <=iNo):
        print(i)
        i = i+1

def main():
   
    print("Enter the value that you want to print : ")
    Value= int(input())
    Display(Value)

if __name__ == "__main__":
    main()