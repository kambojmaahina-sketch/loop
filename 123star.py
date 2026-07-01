'''print 
*
**
***'''
i=1
while i<=3: #i-row--inner loop counter
    j=1
    while j<=i: #j-column--outer loop counter
        print("*",end=" ")
        j=j+1
    print()
    i=i+1