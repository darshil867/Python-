pos = -1

def search(list, n):

    l = 0
    u = len(list) - 1

    while l <= u:

        mid = (l + u) // 2

        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid + 1
            else:
                u = mid - 1

    return False

list = [23, 44, 63, 75, 123, 564, 765]
n = 765

if search(list, n):
    print('Found at', pos + 1)
else:
    print('Not Found')