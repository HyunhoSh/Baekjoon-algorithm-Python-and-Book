import sys

sys.setrecursionlimit(10**7)

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
    
n = int(sys.stdin.readline())

print(factorial(n))

