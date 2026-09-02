input("XOR all numbers - pairs cancel, the odd one strays. press enter")
print("list:[2,3,4,3,2]")
print("odd accuring:", 2^3^4^3^2)

n=int(input("enter a number(try  7 or 11)"))
nums=[3,n,5,3,5]
guess = input("Which number in "+str(nums)+"appears once?")
result=0
for x in nums:
    result^=x
input("XOR cncels pais-the odd one survives. press enter")
print("list:", nums, "odd occuring:", result, "your guess:",guess)