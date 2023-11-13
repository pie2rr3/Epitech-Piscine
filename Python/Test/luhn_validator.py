a = "123456"

doubler = 0
doubler_2 = 0

soustraction = 0
addition = 0

for i in a:
    doubler = a[i::-2] * i
    for i in doubler:
        if doubler[i] > 9:
            soustraction = doubler[i] - 9
    for i in soustraction:
        addition = addition + int(i)
        if addition % 10 == 0:
            print("valid")
        else:
            print("invalid")

# for i in a:
#     doubler = a[1::2]
#     print(doubler)

   
   
#     for i in doubler:
#         doubler_2 = doubler_2 + int(i)
      
# print(doubler_2)

# num = input("Entrez un nombre: ")
# sum = 0

# for i in num:
#     sum = sum + int(i)

# print(sum)



    
    