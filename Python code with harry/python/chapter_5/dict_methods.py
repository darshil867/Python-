oxford = {
    "gift": "Something willingly given to someone to appreciate",
    "this": "A keyword in c++",
    "Youtube": "A video sharing platform",
    "instagram": "a picture sharing platform",
    "mylist": [1, 3, 45]
}

print()
print(oxford.items())
print()
print(oxford)
print()

oxford.update({'Darshil' : 'Good Boy', 'mylist' : [2, 5]})

for a, b in oxford.items():
    print(a, ':', b)
print()


for key in oxford.keys():
    print(key)
print()

print(oxford.get('notpresent'))