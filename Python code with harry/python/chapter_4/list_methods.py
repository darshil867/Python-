myListOfNumbers = [34, 21, 76, 87, 23, 12]
print(myListOfNumbers)

myListOfNumbers.sort()
print(myListOfNumbers)

myListOfNumbers.reverse()
print(myListOfNumbers)

myListOfNumbers.append(45)   # add 45 at the end of the list
print(myListOfNumbers)

myListOfNumbers.insert(3, 63)
print(myListOfNumbers)

myListOfNumbers.pop()  # remove an element from the end of the list
myListOfNumbers.pop(3)  # remove an element from the given index
print(myListOfNumbers)

myListOfNumbers.remove(76)   # remove the first occurance of a given item from the list
print(myListOfNumbers)