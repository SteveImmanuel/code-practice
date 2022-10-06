def bisect_left(arr, val):
    l, h = 0, len(arr)

    while l < h:
        m = (l+h) // 2
        if arr[m] < val:
            l = m + 1
        else:
            h = m
    return l

def bisect_right(arr, val):
    l, h = 0, len(arr)

    while l < h:
        m = (l+h) // 2
        if arr[m] <= val:
            l = m + 1
        else:
            h = m
    return l

arr = [1,2,3,3,3,3,4]
print(bisect_left(arr, 4))
print(bisect_right(arr, 3))

