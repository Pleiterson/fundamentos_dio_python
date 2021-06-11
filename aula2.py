a = int(input('Entre com o primeiro valor: ')) # input pega do teclado o valor digitado pelo usuário e converte ele para inteiro com int() na variável a
b = int(input('Entre com o segundo valor: ')) # input pega do teclado o valor digitado pelo usuário e converte ele para inteiro com int() na variável b

print(type(a))

soma = a + b # operador de soma
subtracao = a - b # operador de subtração
multiplicacao = a * b # operador de multiplicação
divisao = a / b # operador de divisão
resto = a % b # operador de resto da divisão
resultado = (
  'Soma: {soma}.' # podemos chamar uma operação com ela por {soma}
  '\nSubtração: {subtracao}. ' # \n quebra de linha, enter
  '\nMultiplicação: {multiplicacao}'
  '\nDivisão: {divisao}'
  '\nResto: {resto}'.format(
    soma=soma, # definindo qual variável pertence ao valor dentro de {}
    subtracao=subtracao,
    resto=resto,
    multiplicacao=multiplicacao,
    divisao=divisao))

print(resultado) # imprimindo na tela o resultado das operações

# x = '1' # definido automaticamente o valor como uma string
# # soma2 = int(x) + 1 # não há como somar um valor int com uma string
# # print(soma2)