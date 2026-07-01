'''nested loop
initialize outer loop counter
while con:
    initialize inner loop counter
    while con:
        statement1
        statement2
        inc/dec in inner loop
statement--
inc/dec in outer loop'''

i=1
while i<=3: #i-row--inner loop counter
    j=1
    while j<=2: #j-column--outer loop counter
        print("*",end=" ")
        j=j+1
    print()
    i=i+1
