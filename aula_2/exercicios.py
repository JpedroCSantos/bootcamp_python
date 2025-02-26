import math
# #### Inteiros (`int`)

# # 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
# num_1 = int(input("Insira o 1º número: "))
# num_2 = int(input("Insira o 2º número: "))
# print(num_1 + num_2)

# # 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
# num_1 = int(input("Insira o 1º número: "))
# print(f'Resto da divisão: {num_1 % 5}')

# # 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
# num_1 = int(input("Insira o 1º número: "))
# num_2 = int(input("Insira o 2º número: "))
# print(num_1 * num_2)

# # 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
# num_1 = int(input("Insira o 1º número: "))
# num_2 = int(input("Insira o 2º número: "))
# print(num_1 // num_2)

# # 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
# num_1 = int(input("Insira o 1º número: "))
# print(num_1 ** 2)

"""******************************************************************************************"""
# #### Números de Ponto Flutuante (`float`)

# # 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
# num_1 = float(input("Insira o 1º número: "))
# num_2 = float(input("Insira o 1º número: "))
# print(num_1 + num_2)

# # 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
# num_1 = float(input("Insira o 1º número: "))
# num_2 = float(input("Insira o 2º número: "))
# print((num_1 + num_2) / 2)

# # 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# num_1 = float(input("Insira a base: "))
# num_2 = float(input("Insira o expoente: "))
# print(num_1 ** num_2)

# # 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# celsius = float(input("Insira a temperatura em Celsius: "))
# print((celsius * 9/5) + 32)

# # 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
# num_1 = float(input("Insira o raio do circulo: "))
# raio = math.pi * (num_1 ** 2)
# print(f'{raio:.2f}')

"""******************************************************************************************"""
# #### Strings (`str`)

# # 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# string_1 = input("Digite seu texto: ")
# print(string_1.upper())

# # 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# string_1 = input("Digite seu nome completo: ")
# print(string_1.lower())

# # 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# string_1 = input("Digite sua frase: ")
# print(string_1.strip())

# # 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
# data = input("Digite a data no formato 'dd/mm/aaaa': ")
# data_separada = data.split('/')
# for index, item in enumerate(data_separada):
#     data_dict = ['Dia', "Mês", "Ano"]
#     print(f"{data_dict[index]} : {item}")

# # 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
# string_1 = input("Digite seu texto: ")
# string_2 = input("Digite seu texto: ")
# print(string_1 + " " + string_2)

"""******************************************************************************************"""

# #### Booleanos (`bool`)

# # 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# value_1 = input("Digite 'True' ou ' False': ") == "True"
# value_2 = input("Digite 'True' ou ' False': ") == "True"
# print((value_1 and value_2))

# # 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# value_1 = input("Digite 'True' ou ' False': ") == "True"
# value_2 = input("Digite 'True' ou ' False': ") == "True"
# print((value_1 or value_2))

# # 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# value_1 = input("Digite 'True' ou ' False': ") == "True"
# print(not value_1)

# # 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# num_1 = float(input("Insira o 1º número: "))
# num_2 = float(input("Insira o 1º número: "))
# print(f'O número {num_1} é igual ao número {num_2} {num_1 == num_2}')

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
num_1 = float(input("Insira o 1º número: "))
num_2 = float(input("Insira o 1º número: "))
print(f'O número {num_1} é igual ao número {num_2} {num_1 != num_2}')

# #### try-except e if

# 21: Conversor de Temperatura


# 22: Verificador de Palíndromo


# 23: Calculadora Simples


# 24: Classificador de Números


# 25: Conversão de Tipo com Validação
