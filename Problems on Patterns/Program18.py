
#    5 5 5 5 5 
#    4 4 4 4 
#    3 3 3 
#    2 2 
#    1 

rows = 5
# reverse loop
for i in range(rows, 0, -1):
    num = i
    for j in range(0, i):
        print(num, end=' ')
    print("\r")