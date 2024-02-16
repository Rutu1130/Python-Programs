def DisplayClass(iMarks):
    if((iMarks >= 0.00) and (iMarks < 35.00)):
        print("you are fail...\n")
    elif((iMarks >= 35.00) and (iMarks < 50.00)):
        print("you are pass class\n")
    elif((iMarks >= 50.00) and (iMarks < 60.00)):
        print("you are second class\n")
    elif((iMarks >= 60.00) and (iMarks < 75.00)):
        print("you are first class\n")
    elif((iMarks >= 75.00) and (iMarks < 100.00)):
        print("you are first class with distinction\n")
    elif((iMarks < 0.00) or (iMarks > 100.00)):
        print("Invalid Marks....\n")
   
def main():
    iValue = 0.00
    print("Enter your percentage :")
    iValue = int(input())
    DisplayClass(iValue)

if __name__ =="__main__":
    main()