#!/usr/bin/python3
# Program to detect if a given number belongs to the fibonacci sequence

# Fibonacci sequence
#[1,1,2,3,5,8,13...]

# Written expression
# Xn = Xn-1 + Xn-2

def fibonacci_seq():
    fib = [1,1]
    limit = 1
    a = 1
    b = 0

    while limit < 1000:
        fib.append(fib[a]+fib[b])
        a += 1
        b += 1
        limit += 5
    return fib

def fib_dec():
    fibo = fibonacci_seq()
    print(fibo)
    x = 0
    while x < 10:
        number = input("Enter number: ")
        if number == "":
            print("Thank you")
            break
        else:
            if int(number) in fibo:
                print("Yes It is a Fibonacci number")
            else:
                print("Nope, try again")

print(fib_dec())
