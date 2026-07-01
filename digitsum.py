'''enter a num and print sum of its digits'''
num=int(input("enter a num:"))
x=0
while num>0:
    x=x+num%10
    num=num//10
    print(f"sum of digits=",x)