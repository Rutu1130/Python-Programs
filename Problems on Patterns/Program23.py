#    1 
#    2    1 
#    4    2    1 
#    8    4    2    1 
#    16    8    4    2    1 
#    32   16    8    4    2    1 
#    64   32   16    8    4    2    1 
#    128   64   32   16    8    4    2    1 

rows = 9
for i in range(1, rows):
    for j in range(-1 + i, -1, -1):
        print(format(2 ** j, "4d"), end=' ')
    print("")