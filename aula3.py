# verificando a nota e média de alunos com valores abaixo de 10
a = int(input('Primeiro bimestre: '))
if a > 10: # entra se a for maior que 10
  a = int(input('Você digitou errado. Primeiro bimestre: '))

b = int(input('Segundo bimestre: '))
if b > 10: # entra se b for maior que 10
  b = int(input('Você digitou errado. Segundo bimestre: '))

c = int(input('Terceiro bimestre: '))
if c > 10: # entra se c for maior que 10
  c = int(input('Você digitou errado. Terceiro bimestre: '))

d = int(input('Quanto bimestre: '))
if d > 10: # entra se d for maior que 10
  d = int(input('Você digitou errado. Quanto bimestre: '))

media = (a + b + c + d) / 4

print('media: {}'.format(media))

if a <= 10 and b <= 10 and c <= 10 and d <= 10:
  print('media: {}'.format(media))
else:
  print('foi informado alguma nota errada')


#  verificando se existe um número digita é par ou não
a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))

resto_a = a % 2 # pegando o resto da divisão de a por 2
resto_b = b % 2 # pegando o resto da divisão deba por 2

if resto_a == 0 or not resto_b > 0: # verificando se o resto de a e b é par (resto = 0)
  print('foi digitado um número par') # imprime se existe um número par entre eles
else:
  print('nenhum número par foi digitado') # imprime nenhum número par


# verificando qual é o maior valor de 3 números digitados pelo usuário
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

if a > b and a > c: # verificando se a é maior que b E maior que c
  print('o maior número é {}'.format(a)) # se a for maior que b e c, imprime a
elif b > a and b > c: # verificando se b é maior que a E maior que c
  print('o maior número é {}'.format(b)) # se b for maior que a e c, imprime b
else: # a e b não for maior que c
  print('o maior número é {}'.format(c)) # se c for maior que a e b, imprime c

print('final do programa')