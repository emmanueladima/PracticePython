a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
c = []

for x in a:
    if x < 5:
        b.append(x)

print(b)

value = int(input("Enter a value: "))

for i in a:
    if i < value:
        c.append(i)

print(c)
