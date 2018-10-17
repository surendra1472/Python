'''
Created on Oct 17, 2018

@author: Surendra
'''
class GCD:
    def __init__(self):
        print("Hello Fibonacci")

    def getGCDOf(self, a, b):
        print("Calculating GCD of {0}, {1}".format(a, b))
        if b == 0:
            return a
        aa = a % b
        return self.getGCDOf(b, aa)


if (__name__ == "__main__"):
    gcd = GCD()
    print(gcd.getGCDOf(10, 20))
