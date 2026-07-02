'''print
1
21
321
4321
54321'''
i=1
while i<=5: #i-row--inner loop counter
    j=i
    while j>=1: #j-column--outer loop counter
        print(j,end=" ")
        j=j-1
    print()
    i=i+1