l1 = ["shivam", "Soham", "Harry", "Deepika", "Sachin"]

i = 0
while i < len(l1):
    if l1[i].startswith("S"):
        print(f"Good morning {l1[i]}")
    i += 1