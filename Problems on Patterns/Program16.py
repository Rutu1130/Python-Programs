#           1
#          1 2
#        1 2 3
#      1 2 3 4
#    1 2 3 4 5
#  1 2 3 4 5 6
#1 2 3 4 5 6 7
rows = int(input("Enter the number of rows: "))

for i in range(1, rows+1):
    num = 1

    for j in range(rows,0,-1):
        if j > i:
            print(" ", end=" ")
        else:
            print(num, end=" ")
            num += 1

    print()
