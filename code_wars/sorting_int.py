import copy


def descending_order(num):
    return int(str(num)[::-1])

print(descending_order(145267))
 

x = 3
x = x+3
def incN(number: int):
    number = 50
    # print(number)

def inc(number: list[int]):
    number.append(30)
    # print(number)

n = [10, 20]
# print(n)
# inc(n)
# print(n)


class A:
    def __init__(self) -> None:
        self.B = 10
        self.C: list[int] = []
    
    def __str__(self) -> str:
        return f"B: {self.B} | C: {self.C}"

    def __repr__(self) -> str:
        return str(self)

def mut(obj: A):
    obj.B = 30

a = A()
print(a.B)
print(a.C)
mut(copy.copy(a))
incN(a.B)
inc(copy.copy(a.C))
print(a.B)
print(a.C)



def incArray(array: list[A]):
    for a in array:
        a.B += 1

arrayA: list[A] = [A() for _ in range(10)]
print(arrayA)
incArray(copy.deepcopy(arrayA))
print(arrayA)

MyType = type('MyType', (object,), {'a': 1})
m = MyType()
print(m.a)