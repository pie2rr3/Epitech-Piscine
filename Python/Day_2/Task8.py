#import numpy 
#import math
#print (math.pi)
#print (numpy.pi)

a = 0
for i in range(1,100000000000):
    a = a + (4/((-(-1)**i) * ((i*2)-1)))
print(a)



