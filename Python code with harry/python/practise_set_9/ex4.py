with open('donkey.txt', 'r') as f:
    text = f.read()

text = text.replace('donkey', '######')

with open('donkey.txt', 'w') as f:
    f.write(text)