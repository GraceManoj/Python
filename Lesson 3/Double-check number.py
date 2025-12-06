num=int(input("Enter number to check:"))
if num>40:
    print("Number is greater than 40")
    if num%2==0:
        print("And it is even too.")
    else:
        print("And it is odd")
else:
    print("Number is less than 40")