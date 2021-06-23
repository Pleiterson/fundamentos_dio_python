# lambda: é uma função anônima. Uma forma de simplificar algo que será utilizado mais de uma vez no código

contador_letras = lambda lista: [len(x) for x in lista] # faz a leitura da quantidade de letras de palavras e retorna tudo como uma lista
lista_animais = ['cachorro', 'gato', 'elefante']
print(contador_letras(lista_animais))

soma = lambda a, b: a + b # somando dois números
subtracao = lambda a, b: a - b # subtraindo dois números
print(soma(5, 10)) # chamado soma
print(subtracao(10, 5)) # chamado subtração

# tipo dicionário
calculadora = {
    'soma': lambda a, b: a + b, # função lambda soma
    'subtracao': lambda a, b: a - b, # função lambda subtração
    'multiplicacao': lambda a, b: a * b, # função lambda multiplicação
    'divisao': lambda a, b: a / b, # função lambda divisão
}
print(type(calculadora)) # imprimindo o tipo definido da calculadora 'dict' é dicionário

soma = calculadora['soma'] # acessando o dicionário calculadora e a função soma
# soma = lambda a, b: a + b
multiplicacao = calculadora['multiplicacao'] # acessando o dicionário calculadora e a função multiplicação
print('A soma é: {}'.format(soma(10, 5)))
print('A multiplicação é: {}'.format(multiplicacao(10, 2)))