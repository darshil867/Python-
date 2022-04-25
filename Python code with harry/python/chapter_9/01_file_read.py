f = open('this.txt', 'r')
# text = f.read(7)

# text = f.readline()
# print(text)
# text = f.readline()
# print(text)
# text = f.readline()
# print(text)

textList = f.readlines()
print(textList)
f.close()