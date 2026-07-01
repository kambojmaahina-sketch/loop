'''print
1
12
123
1234
12345'''
i=1
while i<=5: #i-row--inner loop counter
    j=1
    while j<=i: #j-column--outer loop counter
        print(j,end=" ")
        j=j+1
    print()
    i=i+1