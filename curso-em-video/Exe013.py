salario = float(input("Digite seu salário: "))
porcento = (15*salario) / 100
novosalario = porcento + salario

print(f"O novo salário após aumento vai para R${novosalario:.2f} reais")