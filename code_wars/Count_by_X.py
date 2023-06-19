def count_by(x, n):
    b = list()
    for i in range(n):
        b.append(x*(i+1))
    return b

print(count_by(10, 5))