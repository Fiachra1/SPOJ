#Solution works however I read that determining primes in python is never going to pass the spoj time limit
import sympy

t=int(input())
for cases in range (t):
    m,n=input().split()
    m= int(m)
    n=int(n)
    for i in range (m,n+1):
        if sympy.isprime(i):
            print(i)
        else:
            continue
    print ('')