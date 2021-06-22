# lista: é mutável, consegue alterar valores, ordenar, etc. É utilizado []
# tupla: é imutável, não consegue alterar valores, ordenar, etc. Deve converter a tupla para lista para realizar as alterações necessárias. É utilizado ()

lista = [12, 10, 7, 5] # lista de inteiros
lista_animal = ['cachorro', 'gato', 'elefante', 'lobo', 'arara'] # lista de strings
lista_animal[0] = 'macaco' # alterando o valor da posição 0 da lista_animal de cachorro para macaco
print(lista) # imprime todo o conteúdo da lista
print(lista_animal)

soma = 0
for x in lista:
  print(x) # imprimindo os valores da lista
  soma += x # somando os valores da lista
print(soma) # imprimindo a soma dos valores da lista

print(sum(lista)) # imprimindo a soma dos valores da lista com a função sum(lista)

tupla = (1, 10, 12, 14) # tupla de inteiros
print(len(tupla)) # len() retorna quantos elementos temos em uma tupla
print(len(lista_animal)) # len() retorna quantos elementos temos em uma lista

tupla_animal = tuple(lista_animal) # converte a lista_animal (lista) em tupla
print(type(tupla_animal)) # type() imprime o tipo do elemento tupla_animal
print(tupla_animal) # imprimindo a tupla_animal

lista_numerica = list(tupla) # converte a tupla (tupla) em lista
print(type(lista_numerica)) # type() imprime o tipo do elemento lista_numerica

lista_numerica[0] = 100 # alterando o valor da posição 0 da lista_numerica de 1 para 100
print(lista_numerica) # imprime a lista_numerica
print(lista_animal[1]) # imprime 'gato'

nova_lista = lista_animal * 3 # multiplica a lista_animal por 3, mesmo sendo uma string
print(nova_lista) # vai imprimir a nova_lista que contém seus dados repetidos 3x de lista_animal

lista.sort() # sort() ordena a lista em ordem numérica
lista_animal.sort() # sort() ordena a lista em ordem alfabética
print(lista)
print(lista_animal)

lista_animal.reverse() # reverse() ordena a lista em ordem alfabética de z a a
print(lista_animal)

if 'lobo' in lista_animal: # verifica se tem lobo na lista_animal
  print('existe um lobo na lista')
else: # se não tem lobo e inclui o item na lista_animal
  print('não existe um lobo na lista. Será incluído.')
  lista_animal.append('lobo') # append inclui novos item a lista_animal
  print(lista_animal)


lista_animal.pop(1) # retira o item da lista_animal, no caso 'gato', se não passar valor remove sempre o último item
print(lista_animal)

lista_animal.remove('elefante') # remove o item 'elefante' da lista_animal
print(lista_animal)