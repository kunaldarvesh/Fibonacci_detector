#!/usr/bin/python3
# Program to detect if a given number belongs to the fibonacci sequence

# Fibonacci sequence
#[1,1,2,3,5,8,13...]

# Written expression
# Xn = Xn-1 + Xn-2

fib = [1,1]
x = 1
a = 1
b = 0

while x < 100:
    fib.append(fib[a]+fib[b])
    a += 1
    b += 1
    x += 5

print(fib)
