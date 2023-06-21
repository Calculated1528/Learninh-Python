def count(s):
    d= {}
    for i in range(len(s)):
        t = 0
        for j in range(len(s)):
            if s[i] == s[j]:
                t +=1
        d[s[i]] = t
    return d
print(count('mhoolboom'))
