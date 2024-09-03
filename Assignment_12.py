num1 = 1
num2 = 1
fibonacci = []
for i in range(1,10):
    fib = num1 + num2
    num1 = num2
    num2 = fib

    # print(fib)
    fibonacci.append(fib)

print(f'Your Fibonacci series from 2 to 100 is {fibonacci}')
