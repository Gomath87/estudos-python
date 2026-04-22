S = 1
cont2 = 2
for cont in range(3,40,2):
    S = S + (cont/cont2)
    cont2 *= 2

print(f"{S:.2f}")