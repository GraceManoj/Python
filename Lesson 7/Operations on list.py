fruits=['apple','orange','pear','kiwi','strawberry','mango','banana']
print ("Length of list", len(fruits))
print("First element", fruits[0])
print("Last element", fruits[-1])

fruits.append('jackfruit')
print("Updated list", fruits)

fruits.remove('orange')
print("Updated list", fruits)

fruits.sort()
print("Sorted list", fruits)

fruits.pop(1)
print("Updated list", fruits)

fruits.reverse()
print("Reversed list", fruits)

print("Multiplication on list:", fruits*2)

fruits=fruits[:4]
print("sliced list:", fruits)

fruits.clear()
print("Updated list:", fruits)