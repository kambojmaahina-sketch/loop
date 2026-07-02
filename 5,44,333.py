'''print
5
44
333
2222
11111'''
i=5
while i>=1: #i-row--inner loop counter
    j=5
    while j>=i: #j-column--outer loop counter
        print(i,end=" ")
        j=j-1
    print()
    i=i-1