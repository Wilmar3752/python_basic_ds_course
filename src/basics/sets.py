num_1_10_set = {1,2,3,4,5,6,7,8,9,10} #key:value
print(num_1_10_set)
#print(type(num_1_10_set))
num_pares_set = {2,4,6,8,10, 12, 14, 16, 18, 20}
print(num_pares_set)

print(num_1_10_set | num_pares_set) #union
print(num_1_10_set & num_pares_set) #interseccion
print(num_1_10_set - num_pares_set) #diferencia
print(num_pares_set - num_1_10_set) #diferencia

