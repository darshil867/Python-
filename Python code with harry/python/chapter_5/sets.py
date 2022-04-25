mySet = {1, 34, 53}
mySet.add(45)
mySet.add("1")
print(mySet)

mySet.remove(34)
mySet.add("1")
# print(mySet.pop())  remove random number
print(mySet)

print(len(mySet))
print(mySet.union({34, 55}))
print(mySet.intersection({1, 56}))
