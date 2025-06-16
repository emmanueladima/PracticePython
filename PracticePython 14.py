import random as rd

a = rd.choices(range(1, 20), k=10)
b = []

def func():
    global b
    b = list(set(a))


func()

print("List a:", a)
print("List b:", b)
