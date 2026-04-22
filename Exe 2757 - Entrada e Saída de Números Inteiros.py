
a = int(input())
b = int(input())
c = int(input())


print(f"A = {a}, B = {b}, C = {c}")
print(f"A = {a:>10}, B = {b:>10}, C = {c:>10}")
dez = 10
A = str(a)
B = str(b)
C = str(c)
if a < 0:
    tempA = 11 - len(A)
    tempB = 11 - len(B)
    tempC = 11 - len(C)
    zero = "0"
    print(f"A = -{zero * tempA}{abs(a)}, B = {zero * tempB}{b}, C = {zero * tempC}{c}")
else:
    tempA = 10 - len(A)
    tempB = 10 - len(B)
    tempC = 10 - len(C)
    zero = "0"
    print(f"A = {zero * tempA}{a}, B = {zero * tempB}{b}, C = {zero * tempC}{c}")

print(f"A = {a:<10}, B = {b:<10}, C = {c:<10}")
