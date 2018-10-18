#!/usr/bin/python3

def gcd(p, q):
    if q is 0:
        return p
    r = p%q
    return gcd(q, r)

if __name__ == "__main__":
    print(gcd(12, 3))
