#!/usr/bin/env python3

def event():
    players = ["alice", "bob", "charlie", "david", "ethann", "faustin"]
    events = {"killed monster", "found treasure", "leveled up"}

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def prime(n):
    count = 0
    number = 2

    while count < n:
        is_prime = True
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
        if is_prime:
            yield number
            count += 1
        number += 1


if __name__ == "__main__":
    n = 1000
    print("=== Game Data Stream Processor ===")
    print("\n=== Generator Demonstration ===")
    print(f"\nProcessing {n} game events...\n")
    print("\n=== Stream Analytics ===")
    prime_len = 5
    prime_list = []
    prime_number = prime(10)
    for i in range(prime_len):
        prime_list.append(next(prime_number))
    prime_str = ", ".join(map(str, prime_list))
    fibo_list = []
    fibo_len = 10
    fib = fibonacci()
    for i in range(fibo_len):
        fibo_list.append(next(fib))
    fibo_str = ", ".join(map(str, fibo_list))
    print(f"Fibonacci sequence (first {fibo_len}): {fibo_str}")
    print(f"Prime numbers (first {prime_len}): {prime_str}")
