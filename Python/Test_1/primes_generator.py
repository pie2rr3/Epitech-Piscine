import sys

if len(sys.argv) != 3:
    print("please enter 2 digit")
    exit(84)
elif (sys.argv[1].isdigit() == False or sys.argv[2].isdigit() == False):
    print("please enter 2 digit")
    exit(84)

i1 = int(sys.argv[1])
i2 = int(sys.argv[2])

if i1 > i2:
    for i in range(i1, i2 - 1, - 1):
        isPrime = True
        for x in range(2, i):
            if i % x == 0:
                isPrime = False
                break
        if isPrime == True and i != 1:
            print(i)
else:
    for i in range(i1, i2+ 1):
        isPrime = True
        for x in range(2, i):
            if i % x == 0:
                isPrime = False
                break
        if isPrime == True and i != 1:
            print(i)