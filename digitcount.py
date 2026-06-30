'''enter a num and count its digits '''
num=int(input("enter the num:"))
x=0
while num>0:
    x=x+1
    num=num//10
    print(f"Digit_count=",x)