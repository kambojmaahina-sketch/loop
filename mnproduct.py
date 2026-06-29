'''enter m and n and print product of m,n times'''
m=int(input("Enter m:"))
n=int(input("Enter n:"))
product=1
i=1
while i<=n:
    product=product*m
    print(f"product=",product)
    i+=1

    #--different approach
m=int(input("Enter m:"))
n=int(input("Enter n:"))
result=m**n
print(f"{result}")