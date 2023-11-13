n = 9  
sequence_sum = 0
current_term = 1


for i in range(n):
    sequence_sum += current_term
    current_term = current_term * 10 + 1

print("Somme de la séquence:", sequence_sum)



