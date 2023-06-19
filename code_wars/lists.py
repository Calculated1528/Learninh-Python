def array_diff(a, b):
    c = []
    """ 1 2 2 | 1 2 \ 0
        1 2   | 1   \ 2 """
    for i in a:
        if i not in b:
            c.append(i)
    return (c)
                


print (array_diff([1, 2, 2], [2]))

# name = 'Otabek'
# if '1' in name:
#     print (True)