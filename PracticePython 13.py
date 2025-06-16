def fib():
    num = int(input('Enter the number of Fibonacci numbers to generate: '))

    if num <= 0:
        print('Please enter a positive integer.')

    elif num == 1:
        return [1]

    else:
        fib_list = [1, 1]
        for i in range(2, num):
            newnumber = fib_list[-1] + fib_list[-2]
            fib_list.append(newnumber)
        return fib_list
    
fib_list = fib()
print("Fibonacci sequence:", fib_list)



