# Accept character from user and check whether it is Alphabet or not

def ChkAlpha(ch):
    if (ch >=  'a' and  ch <= 'z') or (ch >= 'A'  and ch <= 'Z'):
        return True
    else:
        return False

def main():
    cValue = input("Enter the character: ")

    # Ensure the input is a single character
    if len(cValue) != 1:
        print("Please enter exactly one character.")
        return

    bRet = ChkAlpha(cValue)

    if (bRet == True):
        print("It is a character.")
    else:
        print("It is not a character.")

if __name__ == "__main__":
    main()
