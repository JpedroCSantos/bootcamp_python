# 6. Eliminação de Duplicatas
# Objetivo: Dada uma lista de emails, remover todos os duplicados.
# emails = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]
# emails_unicos = list(set(emails))
# print(emails_unicos)


# 7. Filtragem de Dados
# Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.
# idades = [22, 15, 30, 17, 18]
# filter_idades = [idade for idade in idades if idade >= 18]
# print(filter_idades)


# 8. Ordenação Personalizada
# Objetivo: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.
# pessoas = [
#     {"nome": "Alice", "idade": 30},
#     {"nome": "Bob", "idade": 25},
#     {"nome": "Carol", "idade": 20}
# ]

# pessoas.sort(key=lambda item: item["nome"])
# print(pessoas)

# 9. Agregação de Dados
# Objetivo: Dado um conjunto de números, calcular a média.
# numeros = [10, 20, 30, 40, 50]
# media = sum(numeros)/len(numeros)
# print(media)

# 10. Divisão de Dados em Grupos
# Objetivo: Dada uma lista de valores, dividir em duas listas: uma 
# para valores pares e outra para ímpares.

# valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# lista_par = [number for number in valores if (number % 2) == 0]
# lista_impar = [number for number in valores if (number % 2) != 0]
# print(lista_par)
# print(lista_impar)

# Exercícios com Dicionários
# 11. Atualização de Dados
# Objetivo: Dada uma lista de dicionários representando produtos, 
# atualizar o preço de um produto específico.

# produtos = [
#     {"id": 1, "nome": "Teclado", "preço": 100},
#     {"id": 2, "nome": "Mouse", "preço": 80},
#     {"id": 3, "nome": "Monitor", "preço": 300}
# ]

# valid_update = False
# while valid_update is not True:
#     product_id = int(input("Digite o id do produto a ser atualizado: "))

#     produto = next((produto for produto in produtos if produto["id"] == product_id), None)
#     if produto is not None:
#         new_value = float(input("Digite um novo valor para o produto: "))
#         produto["preço"] = new_value
#         print(produto)
#         print(produtos)
#         valid_update = True
#     else:
#         print("Produto não encontrado")


# 12. Fusão de Dicionários
# Objetivo: Dados dois dicionários, fundi-los em um único dicionário.

# dicionario1 = {"a": 1, "b": 2}
# dicionario2 = {"c": 3, "d": 4}

# compact_dict = {**dicionario1, **dicionario2}
# print(compact_dict)

# 13. Filtragem de Dados em Dicionário
# Objetivo: Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.

# estoque = {"Teclado": 10, "Mouse": 0, "Monitor": 3, "CPU": 0}
# estoque_positivo = {produto: quantidade for produto, quantidade in estoque.items() if quantidade > 0}

# 14. Extração de Chaves e Valores
# Objetivo: Dado um dicionário, criar listas separadas para suas chaves e valores.
# dicionario: dict = {"a": 1, "b": 2, "c": 3}
# key_list: list = []
# value_list: list = []
# for key, value in dicionario.items():
#     key_list.append(key)
#     value_list.append(value)

# print(key_list)
# print(value_list)


# 15. Contagem de Frequência de Itens
# Objetivo: Dada uma string, contar a frequência de cada caractere usando um dicionário.

texto = "engenharia de dados , é engenharia sim"
frequencia = {}

split_text = texto.split()
for word in split_text:
    if word in frequencia:
        frequencia[word] += 1
    else:
        frequencia[word] = 1

print(frequencia)