# verificando a nota e média de alunos com valores abaixo de 10
a = int(input('Primeiro bimestre: '))
while a > 10:
  a = int(input('Você digitou errado. Primeiro bimestre: '))

b = int(input('Segundo bimestre: '))
while b > 10:
  b = int(input('Você digitou errado. Segundo bimestre: '))

c = int(input('Terceiro bimestre: '))
while c > 10:
  c = int(input('Você digitou errado. Terceiro bimestre: '))

d = int(input('Quanto bimestre: '))
while d > 10:
  d = int(input('Você digitou errado. Quanto bimestre: '))

media = (a + b + c + d) / 4

print('media: {}'.format(media))


# repete para digitar uma nota até que seja digitado 10
nota = int(input('Entre com a nota: '))
while nota > 10:
  nota = int(input('Nota inválida. Entre com a nota correta: '))
print(nota)


# repetindo os calores de a até 10
a = 0
while a <= 10:
  print(a)
  a += 1


# imprimindo os números primos até o valor digitado
a = int(input('Entre com um valor: '))
for num in range(a + 1):
  div = 0

  for x in range(1, num + 1):
    resto = num % x

    if resto == 0:
      div += 1

  if div == 2:
    print(num)


# verificando se um número digitado é primo
a = int(input('Entre com o número: '))
div = 0

# range gera números aleatórios
for x in range(1, a + 1): # percorre todos os números até o que foi digitado
  resto = a % x # pegando o resto da divisão, verificando se ele é divisível por ele mesmo
  print(x, resto)

  if resto == 0: # verificando se o resto é igual a 0
    div += 1 # se resto = 0, incrementa o div até div ser igual a 2

if div == 2: # se o valor de div for igual a 2, o número digitado é primo, do contrário não é primo
  print('número {} é primo'.format(a))
else:
  print('número {} não é primo'.format(a))