# Conjuntos em Python - set

lista_duplicidade = [1, 1, 2, 3, 3, 4, 5]
valor_unico = set(lista_duplicidade)
print(valor_unico)
print()

# add: Adiciona valores que ainda não existem no conjunto
print(" === add() ===")
conjunto = {1, 2}
conjunto.add(2)
print(conjunto)
conjunto.add(3)
print(conjunto)
print()

# discard: Remove um valor específico, mas se o valor não existe ele ignora
print(" === discard() ===")
numeros = {1, 2, 3, 4, 5, 6, 7, 8}
numeros.discard(8)
numeros.discard(99)
print(numeros)
print()

# pop: Remove o valor na primeira posição do conjunto
print(" === pop() ===")
numeros = {1, 2, 3, 4, 5, 6, 7, 8}
numeros.pop()
numeros.pop()
print(numeros)
print()

# remove: Remove um valor específico, mas se o valor não existe ele retorna um erro
print(" === remove() ===")
numeros = {1, 2, 3, 4, 5, 6, 7, 8}
numeros.remove(1)
# numeros.remove(99)
print(numeros)
print()

# union: Retorna um conjunto novo com as ocorrências únicas da união dos dois coinjuntos
print(" === union() ===")
conjunto_a = {1, 2}
conjunto_b = {3, 4}
print(conjunto_a.union(conjunto_b))
print()

# intersection: Retorna os valores que ocorrem nos dois conjuntos
print(" === intersection() ===")
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}
print(conjunto_a.intersection(conjunto_b))
print()

# difference: Retorna os valores que tenho apenas no conjunto_a que não ocorrem não no conjunto_b
print(" === difference() ===")
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}
print(conjunto_a.difference(conjunto_b))
print()

# symetric_difference: Retorna todos os valores em comum nos dois conjuntos
print(" === symetric_difference() ===")
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}
print(conjunto_a.symmetric_difference(conjunto_b))
print()

# issubset: Retorna True se todos os valores de conjunto_a ocorrem no conjunto_B, caso contrário retorna False
print(" === issubset() ===")
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}
print(conjunto_a.issubset(conjunto_b))
print()

# issuperset: Retorna True se todos os elementos de conjunto_b ocorrem no conjunto_a, caso contrário retorna False
print(" === issuperset() ===")
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}
print(conjunto_a.issuperset(conjunto_b))
print()

# isdisjoint: Retorna True se nenhum elemento do conjunto_a ocorre no conjunto_b
print(" === isdisjoint() ===")
conjunto_a = {1, 2, 3}
conjunto_b ={4, 5, 6, 7}
print(conjunto_a.isdisjoint(conjunto_b))
print()