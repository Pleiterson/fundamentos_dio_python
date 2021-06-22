# conjunto utiliza {}. type 'set'. Não pode ter itens repetidos, são ignorados

# conjunto = {1, 2, 3, 4, 4, 2} # conjunto não pode ter números repetidos
# conjunto.add(5) # add() adiciona um novo número no conjunto, no caso o 5
# conjunto.discard(2) # discard() elimina um número do conjunto, no caso 2
# print(conjunto) # imprimindo conjunto

conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}
conjunto_uniao = conjunto.union(conjunto2) # realizando a união (union) do conjunto com conjunto2 eliminando números repetidos
print('União: {}'.format(conjunto_uniao)) # imprimindo {1,2,3,4,5,6,7,8}

conjunto_interseccao = conjunto.intersection(conjunto2) # realizando a interseção (intersection) do conjunto com conjunto2, números em comum nos dois conjuntos
print('Interseção: {}'.format(conjunto_interseccao)) # imprimindo {5}

conjunto_diferenca1 = conjunto.difference(conjunto2) # realizando a diferença (difference) do conjunto com conjunto2, números que tem no conjunto e que não tem no conjunto2
conjunto_diferenca2 = conjunto2.difference(conjunto) # realizando a diferença (difference) do conjunto2 com conjunto, números que tem no conjunto2 e que não tem no conjunto
print('Diferença entre 1 e 2: {}'.format(conjunto_diferenca1)) # imprimindo {1,2,3,4}
print('Diferença entre 2 e 1: {}'.format(conjunto_diferenca2)) # imprimindo {6,7,8}

conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2) # realizando a diferença simétrica (symmetric_difference) do conjunto com conjunto2, números que não tem em um e no outro conjunto
print('Diferença simétrica: {}'.format(conjunto_diff_simetrica)) # imprimindo {1,2,3,4,6,7,8}

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_subset1 = conjunto_a.issubset(conjunto_b) # verifica se o conjunto_a é um subconjunto (issubset) conjunto_b, os mesmos números que tem no conjunto_a tem que ter no conjunto_b
conjunto_subset2 = conjunto_b.issubset(conjunto_a) # verifica se o conjunto_b é um subconjunto (issubset) conjunto_a, os mesmos números que tem no conjunto_b tem que ter no conjunto_a
print('A é subconjunto de B: {}'.format(conjunto_subset1)) # imprimindo True, conjunto_b têm os mesmos números que o conjunto_a
print('B não é subconjunto de A: {}'.format(conjunto_subset2)) # imprimindo False, falta os números 4 e 5 no conjunto_a

conjunto_superset1 = conjunto_b.issuperset(conjunto_a) # verifica se conjunto_a tem todos os elementos do conjunto_b, superconjunto (issuperset)
conjunto_superset2 = conjunto_a.issuperset(conjunto_b) # verifica se conjunto_b tem todos os elementos do conjunto_a, superconjunto (issuperset)
print('B é um superconjunto de A: {}'.format(conjunto_superset1)) # imprimindo True, conjunto_b têm todos elementos do conjunto_a
print('A não é um superconjunto de B: {}'.format(conjunto_superset2)) # imprimindo False, conjunto_a não têm todos elementos do conjunto_b

lista = ['cachorro', 'cachorro', 'gato', 'gato', 'elefante']
print(lista)

conjunto_animais = set(lista) # converte a lista (lista) em conjunto_animais
print(conjunto_animais) # imprime conjunto_animais sem valores repetidos

lista_animais = list(conjunto_animais) # converte o conjunto (conjunto_animais) em lista
print(lista_animais) # imprime conjunto_animais sem valores repetidos, após a conversão da lista em conjunto e depois para lista novamente