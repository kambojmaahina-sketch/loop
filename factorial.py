'''enter a num and print its factorial'''
n=int(input("enter the num:"))
factorial=1
i=1
while i<=n:
    factorial=factorial*i
    print(f"factorial=",factorial)
    i+=1