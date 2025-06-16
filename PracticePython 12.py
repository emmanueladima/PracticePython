import random as rd
a = rd.sample(range(1,20),10)

b = []

def func():
    b.append(a[0])
    b.append(a[-1])

func()
print("List a:", a)
print("List b:", b)
