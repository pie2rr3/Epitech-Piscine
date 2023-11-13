#Task_00

# def f ( x ) :
#     return 2 * x + 1
# def g () :
#     return 7

# y = f (2)
# print ( y )
# y = f (5) + g ()
# print ( y )

#Task_01

# def bread () :
#     print (" <////////// > ")
# def lettuce () :
#     print (" ~~~~~~~~~~~~ ")
# def tomato () :
#     print ("O O O O O O")
# def ham () :
#     print (" ============ ")
    
# bread(), lettuce(), tomato(), ham(), ham(), bread()

#Task_02

# def bread () :
#     print (" <////////// > ")
# def lettuce () :
#     print (" ~~~~~~~~~~~~ ")
# def tomato () :
#     print ("O O O O O O")
# def ham () :
#     print (" ============ ")

# def sandwich ():
#     (bread(), lettuce(), tomato(), ham(), ham(), bread())
    
# for i in range(42):
#     sandwich()

#Task_03

# def bread () :
#     print (" <////////// > ")
# def lettuce () :
#     print (" ~~~~~~~~~~~~ ")
# def tomato () :
#     print ("O O O O O O")
# def ham () :
#     print (" ============ ")

# def sandwich ():
#     (bread(), lettuce(), tomato(), ham(), ham(), bread())
    
# x = int((input("tu veux cmb de sandwich ?")))

# def chef():
#     if x <= 0:
#         print("repete frero")
#     else:
#         for i in range(x):
#             sandwich()
# chef()

#Task_04


# def bread () :
#     print (" <////////// > ")
# def lettuce () :
#     print (" ~~~~~~~~~~~~ ")
# def tomato () :
#     print ("O O O O O O")
# def ham () :
#     print (" ============ ")
# def vegan():
#     (bread(), lettuce(), lettuce(),tomato(), tomato(),bread())

# def sandwich ():
#     (bread(), lettuce(), tomato(), ham(), ham(), bread())
    
# x = int(input("tu veux cmb de sandwich ?"))
# v = int(input("tu veux un vegan?"))
    
# def chef():
#     if x <= 0:
#         print("repete frero")
#     elif v == "Oui" or v == "oui" or v == "oue" or v == "oue":
#         vegan()
#     else:
#         for i in range(x):
#             sandwich()

# chef()


#Challenge

# import time
# x = input("Donne un chiffre stp")
# z = input("Donne une puissance mon super pote")
# y = 1

# startingTime = time.time()

# def puissance ():
#     for i in range(int((z))):
#         y = y * int(z)
        
# duration = time.time() - startingTime
# puissance()

#Recursion_Task_01

# a = input("donne moi viiiiite un mot jvais m'énerver ! ")

# def palindrome(a):
#     if a == a[::-1]:
#         return print("Ton mot est un palindrome bg")
#     else:
#         print("c pas un palindrome ton mot XD")

# palindrome(a)

# def palindrome(a):
#     a = a.replace(" ", "").lower().replace("?","")
#     if len(a) <= 1:
#         return True
#     if a[0] != a[-1]:
#         return False
#     return palindrome(a[1:-1])


# print(palindrome("Was it a car or a cat I saw?"))   

#Task_02

#Task_00

def funA(s, n):
    compte = 0
    for i in s:
        if i.islower():
            compte += 1
    return compte >= n

s = input("Donne un mot stp (lower): ")
n = int(input("Donne un nombre : "))

# resultA = funA(s, n)
# print(f"Il y a au moins {n} lettres minuscules gros bg: {resultA}")

# def funB(s, n):
#     compte = 0
#     for i in s:
#         if i.isupper():
#             compte += 1
#     return compte >= n

# s = input("Donne un mot stp (upper): ")
# n = int(input("Donne un nombre : "))

# resultB = funB(s, n)
# print(f"Il y a au moins {n} lettres majuscules gros bg: {resultB}")

# def funC(s, n):
#     compte = 0
#     for i in s:
#         if isinstance(i, int):
#             compte += 1
#     return compte >= n

# s = input("Donne un mot stp (characters): ")
# n = int(input("Donne un nombre : "))

# resultC = funC(s, n)
# print(f"Il y a au moins {n} lettres gros bg: {resultC}")

# def funD(s, n):
#     compte = 0
#     for i in s:
#         if i == "@_!#$%^&*()<>?/\|}{~":
#             compte += 1
#     return compte >= n

# s = input("Donne un mot stp (special characters): ")
# n = int(input("Donne un nombre : "))

# resultD = funD(s, n)
# print(f"Il y a au moins {n} caractères spéciaux gros bg: {resultD}")

#Danny Phantom version

# a=input("donne un string, stp : ")
# b=input("un integer vite, viiiiite !!! ")

# def funA(a):
#     y=len(a)
#     z=0
#     for i in range(y):
#         if a[i].islower ():
#             z += +1
#         else:
#             z=z
#     return z

# z=funA(a)
# if z>=int(b):
#     print("A = true")
# else:
#     print ("A = false") 


# def funB(a):
#     y=len(a)
#     z=0
#     for i in range(y):
#         if a[i].isupper ():
#             z += +1
#         else:
#             z=z
#     return z

# z=funB(a)
# if z>=int(b):
#     print("B = true")
# else:
#     print ("B = false") 


# def funC(a,b):
#     y=len(a)
#     if y>=int(b):
#         print("C = true")
#     else:
#         print ("C = false")
# funC(a,b)


# def funD(a):

#     y=len(a)
#     z=0
#     for i in range(0, len(a)):

#         if (a[i].isalpha()):
#             continue

#         elif (a[i].isdigit()):
#             continue
#         else: 
#             z += 1
#     return z
# z=funD(a)
# if z>=int(b):
#    print("D = true")
# else:
#    print ("D = false")

# def funE(a):
#     x=a.split()
#     y=len(x)
#     z=0
#     for i in range(y):
#         try:
#          val = int(x[i])
#          z=z+1
#         except ValueError:
#             z=z
#     return z

# z=funE(a)
# if z>=int(b):
#    print("E = true")
# else:
#    print ("E = false")

#Task_01

def funA(s, n):
    compte = 0
    for i in s:
        if i.islower():
            compte += 1
    return compte >= n

s = input("Donne un mot stp (lower): ")
n = int(input("Donne un nombre : "))

resultA = funA(s, n)
print(f"Il y a au moins {n} lettres majuscules gros bg: {resultA}")



  
#Task_02










    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    








    





    
    
    







    

