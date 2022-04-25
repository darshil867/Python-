f = open('file/mydata.txt', 'r')

# print(f.readline(), end='')
# print(f.readline())

f1 = open('file/abc', 'w')
# f1.write(' mobile')

for data in f:
    f1.write(data)

f = open('file/Screenshot (137).png', 'rb')
f1 = open('file/Mypic.png', 'wb')
for i in f:
    f1.write(i)
