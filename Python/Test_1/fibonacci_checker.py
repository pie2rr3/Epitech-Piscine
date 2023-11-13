import sys

if len(sys.argv) == 1:
    print("not enough argument")
    exit(84)

digits = sys.argv[1::1]
isRight = True

if len(digits) > 2:
    for i in range(2, len(digits)):
        if digits[i].replace("-", "").isdigit() == False or digits[i - 1].replace("-", "").isdigit() == False or digits[i - 2].replace("-", "").isdigit() == False:
            print("Not a valid number")
            exit(84)
        elif int(digits[i]) != int(digits[i - 1]) + int(digits[i - 2]):
            isRight = False
            break
else:
    isRight = False

if isRight == True:
    print("OK")
else:
    print("Not a Fibonacci sequence") 