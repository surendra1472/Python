'''
Created on Oct 17, 2018

@author: Surendra
'''
class Fibonacci:
    def __init__(self):
        print("Hello Fibonacci")

    def printNfirstFibonacci(self, n):
        print("Printing first {0} fibonacci")
        t1 = 0;
        t2 = 1
        for i in range(n):
            print(t1)
            t1, t2 = t2, t1 + t2


def gcd(a, b):
    if b == 0:
        return a
    aa = a % b
    return gcd(b, aa)


print(gcd(10, 20))

if(__name__ == "__main__"):
    fibonacci = Fibonacci()
    fibonacci.printNfirstFibonacci(10)
    fibonacci.printNfirstFibonacci(0)
    fibonacci.printNfirstFibonacci(1)
    fibonacci.printNfirstFibonacci(-1)
