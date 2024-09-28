#    A  
#    B C
#    D E F
#    G H I J
#    K L M N O
#    P Q R S T U
#    V W X Y Z [ \

# ASCII number of 'A'
ascii_number = 65
rows = 7
for i in range(0, rows):
    for j in range(0, i + 1):
        character = chr(ascii_number)
        print(character, end=' ')
        ascii_number += 1
    print(" ")