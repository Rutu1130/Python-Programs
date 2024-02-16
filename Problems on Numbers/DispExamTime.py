
def DisplayExamTime(Standard):
    if(Standard == 1):
        print("Your Exam at 8 AM\n")
    elif(Standard == 2):
        print("Your Exam at 9 AM\n")
    elif(Standard == 3):
        print("Your Exam at 10 AM\n")
    elif(Standard == 4):
        print("Your Exam at 11 AM\n")
    elif(Standard == 5):
        print("Your Exam at 12 PM\n")
    else:
        print("Invalid Input.....\n")

def main():
    iNo = 0
    print("Enter the Standard :")
    iNo = int(input())
    DisplayExamTime(iNo)

if __name__ == "__main__":
    main()