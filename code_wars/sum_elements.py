""" Given n, take the sum of the digits of n. If that value has more 
than one digit, continue reducing in this way until a single-digit number is produced. 
The input will be a non-negative integer."""


# n = 493193
# def digital_root(n):
#     b = list(map(int, str(n)))
#     while len(b) >= 1: 
#         a = sum(b)
#         c = list(map(int, str(a)))
#         while len(c) >= 1:
#             s = sum(c)
#             m = list(map(int, str(s)))
#             while len(m) >= 1:
#                 g = sum(m)
#                 print (g)
#                 break
#             break
#         break 

def digital_root(n):
    b = list(map(int, str(n)))
    while len(b) > 1: 
        a = sum(b)
        b = list(map(int, str(a)))
    return sum(b)



## рекурсия, улучшенная версия

# def digital_root(n):
#     b = sum(list(map(int, str(n))))
#     if b >9:
#         return digital_root(b)
#     return b

# ## конченный чел
# def digital_root(n):
# 	return n%9 or n and 9 

print (digital_root(114))