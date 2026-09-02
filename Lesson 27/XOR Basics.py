input("XOR with 0 keeps the number.press enter")
print("5^0=", 5^0)
print("9^0=", 9^0)

input("XOR with itself gives 0")
print("5^5=", 5^5)
print("9^9=", 9^9)

n=int(input("enter a number(try 6 or 11)"))
guess=input("What is 3^" + str(n) + "^3?")
input("XOR cancels- 3 appers twice so it diappears. press enter")
print(" 3^",n,"^3=", 3^n^3,"your guess:", guess)