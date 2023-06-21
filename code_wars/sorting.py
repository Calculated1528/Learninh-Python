def descending_order(num):
    b = list(map(int, str(num)))
    b.sort()
    n = int(''.join(map(str, b))[::-1])
    return n

print(descending_order(5380))