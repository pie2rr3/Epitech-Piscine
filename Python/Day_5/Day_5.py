#Task_01

# a = [0,1,2,3,4]
# print(a[0])

#Task_02

# a = [0,1,2,3,4]
# print(a[-1])

#Task_03

# a = [0,1,2,3,4]
# a.append(5)
# print(a)

#Task_04

# a = [0,1,2,3,4]
# print(a)

#Task_05

# a = [10,23,50,22,34]
# a.remove(a[-1])
# print(a)

#Task_06

# a = [10,23,50,22,34]
# a.insert(0,777)
# print(a)

#Task_07

# a = "Pierre le plus bo"
# print(a[2:5])

#Task_08

# a = [10,23,50,22,34]
# b = a[::-1]
# print(b)

#Task_09

# a = [10,23,50,22,34]
# b = a[::2]
# print(b)

#Task_10

#Task_11

# my_first_list = [4 , 5 , 6]
# my_second_list = [1 , 2 , 3]
# my_first_list.extend(my_second_list)
# print(my_first_list)

# my_first_list = [7 , 8 , 9]
# my_second_list = [4 , 5 , 6]
# my_first_list = my_first_list + my_second_list
# print(my_first_list)

# my_first_list = [7 , 8 , 9]
# my_second_list = [4 , 5 , 6]
# my_first_list = [* my_first_list , * my_second_list]

#Task_01

# a = [7, 8, 9, 4, 5, 6, 88, 99, 354, 173]
# b = len(a)
# c = 1
# for i in range(0, b-1):
#     c = c*a[i]
# print(c)

#Task_02

# print([x + 10 for x in [3, 2, 6, 7, 1, 4]])

#Task_03

# print(list(map(lambda x: x * x, [3, 2, 6, 7, 1, 4])))
#or 
# print([x * x for x in [3, 2, 6, 7, 1, 4]])

#Task_04

# a = [1000,36373,6,3678,88]
# print(str(min(a)) + "\n" + str(max(a)))

#Task_05

# a = [1000,36373,6,3678,88,-4,0]
# a2 = [i for i in a if i < 7 ]
# print(a2)

#Task_06

# a = [1000,36373,6,3678,88,-4,0]
# a.sort()
# print(a)

#Task_07

# print([x // 2 if x % 2 == 0 else x * 2 for x in [42, 3, 4, 18, 3, 10]])

#Task_08

# print(list(filter(lambda x: x > 10, [42, 3, 4, 18, 3, 10])))
# #or
# print([x > 10 for x in [3, 2, 6, 7, 1, 4]])

#Task_09

# print([*enumerate([42, 3, 4, 18, 3, 10])])

#Task_10

# first_name = [" Jackie ", " Bruce ", " Arnold ", " Sylvester "]
# last_name = [" Stallone ", " Schwarzenegger ", " Willis ", " Chan "]
# magic = [* zip ( first_name , last_name [:: -1]) ]
# print ( magic [0])
# print ( magic [3])
# print ( magic [1][0]) #lorsque il y en a 2 on précise le tableau que l'on utilise [0] = first_name et [1] = ... donc [1][0] = Bruce du 1ere tableau
# print ( magic [0][1])
# print ( magic [2])

#Challenge

# import time
# import random
# startingTime = time.time()

# a=[0]*1000000
# for i in range(0,1000000):
#     a[i]= random.randint(-1000000,1000000)
# a.sort()
# duration = time.time()- startingTime
# print(duration)

#Task_01

# student = {"name" : "Caca" ,"academic_year" : "2020"}

#Task_02

# student = {"name" : "Danny" ,
#            "academic_year" : "2020", 
#            "units" : {"name" : "Web Developement",
#                       "Credits" : 15,
#                       "Grade" : "Java"
#                       }}



#Task_03

# student = {"name" : "Danny" ,
#            "academic_year" : "2020", 
#            "units" : {"name" : "Web Developement",
#                       "Credits" : "Network and System Administration",
#                       "Grade" : "Java"
#                       }}

# grade_weight_mapping = {"A" : 4, 
#                         "B" : 3, 
#                         "C" : 2, 
#                         "D" : 1, 
#                         "E" : 0}





#Task_04

#Task_01


# symbole = '*'
# n = 8

# for i in range(16):
#     if i <= n:
#         print(symbole * i)
#     else:
#         print(symbole * (n - (i - n)))



        
	






    

        
        
        
        
    
    






   
        


    



























    
    
    































