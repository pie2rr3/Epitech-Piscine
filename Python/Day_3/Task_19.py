# a = "This is a test. Is it possible to fly? Good things come to those who never give up"
# b = a.split()
# print(b[0], b[5], b[9])


a= "This is a test. Is it possible to fly? Good things come to those who never give up"
phrasecoupé=a.split()
b=len(phrasecoupé)
q=""

for i in range(0,b-1):
    x=len(phrasecoupé[i])
    for h in range(0,x-1):
        mot=phrasecoupé[i]
        if mot[h].isupper():
         q=q+" "+mot

print(q)


