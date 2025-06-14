a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = []

for x in a:
    if x in b:
        c.append(x)

c = list(set(c))

print(c)

#or you can use this for quicker one liner
c = list(set(a) & set(b))
print(c)