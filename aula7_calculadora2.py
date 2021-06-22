class Calculadora:
    # def __init__(self):
        # pass # pass define o método como vazio

    def soma(self, valor_a, valor_b):
        return valor_a + valor_b # retorna a soma dos dois valores

    def subtracao(self, valor_a, valor_b):
        return valor_a - valor_b # retorna a subtração dos dois valores

    def multiplacacao(self, valor_a, valor_b):
        return valor_a * valor_b # retorna a multiplicação dos dois valores

    def divisao(self, valor_a, valor_b):
        return valor_a / valor_b # retorna a divisão dos dois valores


calculadora = Calculadora()
print(calculadora.soma(10, 2)) # chamado a função soma e instanciando os valores a e b
print(calculadora.subtracao(5, 3)) # chamado a função subtração e instanciando os valores a e b
print(calculadora.divisao(100, 2)) # chamado a função divisão e instanciando os valores a e b
print(calculadora.multiplacacao(10, 5)) # chamado a função multiplicação e instanciando os valores a e b