# #Número de caracteres

# name = input("Digite seu nome: ")
# print(len(name))

#Soma de Valores
# valor1 = int(input("Digite o primeiro número: "))
# valor2 = int(input("Digite o segundo número: "))
# print(valor1 + valor2)

#Desafio
nome = input("Digite seu nome: ")
salario = round(float(input("Digite seu salário: ")), 2)
bonus = round(float(input("Digite seu bonus: ")))

kpi_diferenca = round((salario/bonus) * 100, 2)
kpi = (1000 + salario) * bonus

print(f"Olá {nome} a diferença do seu salário e do seu bonus foi de: {kpi_diferenca}%, kpi de {kpi}")