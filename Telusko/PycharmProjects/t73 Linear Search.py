pos = -1

def search(list, n):

    for i in range(len(list)):
        if list[i] == n:
            globals()['pos'] = i
            return True

    return False

list = [11, 22, 33, 44, 55, 66]
n = 44

if search(list, n):
    print('Found at', pos + 1)
else:
    print('Not Found')