'''enter a num and print sum of all natural num upto it'''
n=int(input("enter the num:"))
i=1
while i<=n:
    sum=sum+i
    print(f"sum=",sum)
    i+=1