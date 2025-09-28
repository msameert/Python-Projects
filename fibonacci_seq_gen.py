"""Fibonacci sequence generator using iterators and generators"""

def fibonacci_seq_gen():
    a, b = 0,1
    while True:
     yield a
     a, b = b, a + b

fib = fibonacci_seq_gen()

n = int(input("Enter how many Fibonacci sequence numbers you want : "))
print("Here are your numbers : ")

for i in range(n):
    print(next(fib))
