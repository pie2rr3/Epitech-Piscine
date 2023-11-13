import sys

if len(sys.argv) > 2:
    print("too many argument")
    exit(84)
elif len(sys.argv) == 1:
    print("too few argument")
    exit(84)
elif sys.argv[1].isdigit() == False or sys.argv[1] == "":
    print("please enter a correct number")
    exit(84)

validString = sys.argv[1]

sum = 0

for i in range(0, len(validString)):
    if i % 2 == 1:
        if int(validString[i]) * 2 > 9:
            sum +=  int(validString[i]) * 2 - 9
        else:
            sum += int(validString[i]) * 2
    else:
        sum += int(validString[i])

if sum % 10 == 0:
    print("valid")
else:
    print("invalid")