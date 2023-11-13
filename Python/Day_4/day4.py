#Conditionals

def task01():
    if int(input("Enter a number: ")) == 42:
        print("Correct answer")

def task02():
    if int(input("Enter a number: "))%2==0:
        print("The integer is even")
    else:
        print("The integer is odd")

def task03():
    psw = input("Enter the password: ")
    match psw:
        case "open sesame":
            print("access granted")
        case "will you open, you goddamn !¤*@¡":
            print("access fucking granted")
        case _:
            print("permission denied")

def task04():
    n = int(input("Enter a number: "))
    if n==42 or n<=21 or n%2==0 or (n/2)<21 or (n%2!=0 and n>=45):
        print("OK")
    else:
        print("You got wrong my poor friend")

def task05():
    a = 42
    b = 41
    if a == b:
        print ("A and B are the same")
    if b <= a:
        print ("B is equal or lower than A")
    if b != a:
        print ("B is different from A")

#Loops

def task10():
    for i in range(0, 1001):
        print(i)

def task11():
    str = input("Write a word: ")
    str2 = ""
    for i in range(0, len(str)):
        str2 += 2*str[i]
    print(str2)

def task12():
    for i in range(1001, 0, -1):
        if i%7==0:
            print(i)

def task13():
    for i in range(-30, 31):
        str = ""
        if i%3==0:
            str += "Fizz"
        if i%5==0:
            str += "Buzz"
        if str != "":
            print(str)
        else:
            print(i)

def task14():
    for i in range(100, 1, -1):
        print(str(i)+" bottles of age appropriate bottles on the wall")
    print("1 bottle of age appropriate bottle on the wall")

def task15():
    n = int(input("Enter a number: "))
    for i in range(2, n//2):
        string = ""
        for j in range(n-1, 1, -1):
            if j%i==0:
                string += str(j)+" "
        print(string)

def challenge():
    vowels = ["a", "e", "i", "o", "u", "y"]
    string = input("Enter a word: ")
    n = int(input("Enter a number: "))
    if n!=0:
        if n>=42:
            print(n)
        else:
            for s in string:
                if s in vowels:
                    print(n)
                    break
    else:
        exit()
        
#Encryption

def task21():
    alpha = "abcdefghijklmnopqrstuvwxyz"
    string = input("Enter a sentence: ")
    key = int(input("Enter a key: "))
    newString = ""
    for s in string:
        if s in alpha:
            place = alpha.find(s)+key
            if place > 25:
                place -= 25
            newString += alpha[place]
        else:
            newString += s
    print(newString)
task21()

def task215():
    alpha = "abcdefghijklmnopqrstuvwxyz"
    string = input("Enter a encrypted sentence: ")
    key = int(input("Enter a key: "))
    newString = ""
    for s in string:
        if s in alpha:
            place = alpha.find(s)-key
            if place < 0:
                place += 26
            newString += alpha[place]
        else:
            newString += s
    print(newString)

def task22():
    alpha = "abcdefghijklmnopqrstuvwxyz"
    string = input("Enter a sentence: ")
    key = input("Enter the key: ")
    while len(string)>len(key):
        key += key
    if len(string)<len(key):
        key = key[:len(string)]
    ed = input("Encode (e) or decode (d) ? ")
    newString = ""
    match ed:
        case "e":
            for i in range(0, len(string)):
                place = alpha.find(string[i]) + alpha.find(key[i])
                if place > 25:
                    place -= 25
                newString += alpha[place]
        case "d":
            for i in range(0, len(string)):
                place = alpha.find(string[i]) - alpha.find(key[i])
                if place < 0:
                    place += 26
                newString += alpha[place]
        case _:
            print("Wrong input")
    print(newString)

