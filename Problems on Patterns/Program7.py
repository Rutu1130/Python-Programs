
#Input : Enter the number of rows: 4
#   *  *  *  *
#   *  *  *
#   *  *
#   *


rows = int(input("Enter the number of rows: "))
for i in range(rows + 1, 0, -1):
    for j in range(0, i - 1):
        print("* ", end=" ")

    print()