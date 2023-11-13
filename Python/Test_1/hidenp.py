import sys

if len(sys.argv) != 3:
    print("please enter 2 string")
    exit(84)

string1 = sys.argv[1]
string2 = sys.argv[2]
i = 0

for c in string2:
    if i != len(string1) and c == string1[i]:
        i += 1
if i == len(string1):
    print(1)
else:
    print(0)