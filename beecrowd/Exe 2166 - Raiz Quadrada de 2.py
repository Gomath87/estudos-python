
num = int(input())
d = 2
r = 0
if num == 0:
    print("1.0000000000")
else:
    for cont in range(1,num+1):
        r = 2 + 1/r
resultado = 1 + 1/r
print(f"{resultado:.10f}")
