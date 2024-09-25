rows = int(input("Enter the number of rows: "))
num = 1
stop = 2

for i in range(rows):

    for j in range(1, stop):
        print(num, end=" ")
        num += 1

    print()
    stop += 2