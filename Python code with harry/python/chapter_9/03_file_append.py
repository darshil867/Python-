# f = open('write.txt', 'w') # write mode
f = open('write.txt', 'a') # append mode
f.write('This is a text, I want to write in file\n')
f.write('second line: This is a text, I want to write in file\n')
f.close()