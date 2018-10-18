#!/usr/bin/env python3

def gcd(p, q):
    """
    Calculates the greatest commond divisor for two numbers p and q.
    """
    if q == 0:
        return p
    r = p%q
    return gcd(q, r)

if __name__ == "__main__":
    print(gcd(12, 3))

assert gcd(12, 3) == 3
print(gcd(12, 3))
    

