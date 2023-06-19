def narcissistic( value ):
    b = list(map(int, str(value)))
    for i in range(len(b)):
        b[i]= (b[i])**(len(b))
    s = sum(b)
    print(s)
    if s == value:
        return True
    else:
        return False

print(narcissistic(1))