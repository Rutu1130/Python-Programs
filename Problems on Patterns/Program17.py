
#    1 
#    1 2
#    1   3
#    1     4
#    1       5
#    1 2 3 4 5 6

n = 6  # Number of rows

for i in range(1, n + 1):
    count = 1
    for j in range(i):
        if j == 0 or j == i - 1 or i == n:
            print(count, end=' ')
        else:
            print(' ', end=' ')
        count += 1
    print()  
