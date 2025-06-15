a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#print([x for x in a if x % 2 == 0])

#Lists[] show everything at once instead of doing a for loop for sets() like eg below

b = (x for x in a if x % 2 == 0)

for n in b:
    print(n)