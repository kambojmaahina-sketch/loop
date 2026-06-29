'''Take input of 2 numbers and print sum everytime until user want to exit'''
while True:
    a=int(input("Enter a:"))
    b=int(input("Enter b:"))

    print("Sum=" ,a+b)

    choice=input("Do you want to continue? (yes/no): ")
    if choice=="no" or choice=="NO":
        print("Program ended")
        break