#    1 
#    3 3 
#    5 5 5 
#    7 7 7 7 
#    9 9 9 9 9

rows = 5
i = 1
while i <= rows:
    j = 1
    while j <= i:
        print((i * 2 - 1), end=" ")
        j = j + 1
    i = i + 1
    print('')
