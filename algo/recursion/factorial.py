#!/usr/bin/env python3

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

assert factorial(5) == 120

print(factorial(5))
