#from fractions import Fraction
#print(Fraction(2, 10))

#import math
#print(math.gcd(2,10))

n = 2
d = 10
i = 2

while i <= n and d:
    if n%i == 0 and d%i ==0:
        n=n//i
        d=d//i
    else:
        i=i+i
print(n,"/",d)
