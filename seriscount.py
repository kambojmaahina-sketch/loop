'''print
1
22
333
4444
55555'''
i=1
while i<=5: #i-row--inner loop counter
    j=1
    while j<=i: #j-column--outer loop counter
        print(i,end=" ")
        j=j+1
    print()
    i=i+1