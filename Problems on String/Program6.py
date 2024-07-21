def Reverse(string):
    reversed_string = ""
    iLen = len(string)

    for iCnt in range(iLen - 1, -1, -1):
        reversed_string += string[iCnt]

    print(reversed_string)

def main():
    string = input("Enter the string: ")
    Reverse(string)

if __name__ == "__main__":
    main()
