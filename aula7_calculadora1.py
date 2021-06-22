# classe calculadora, sempre começa com a primeira letra maiúscula
class Calculadora:
    #método init, não retorna nenhuma valor
    def __init__(self, num1, num2):
        self.valor_a = num1 # atribuindo o primeiro valor a variável valor_a
        self.valor_b = num2 # atribuindo o segundo valor a variável valor_b
    
    #função de soma
    def soma(self):
        return self.valor_a + self.valor_b # retorna a soma dos dois valores

    #função de subtração
    def subtracao(self):
        return self.valor_a - self.valor_b # retorna a subtração dos dois valores
    
    #função de multiplicação
    def multiplacacao(self):
        return self.valor_a * self.valor_b # retorna a multiplicação dos dois valores

    #função de divisão
    def divisao(self):
        return self.valor_a / self.valor_b # retorna a divisão dos dois valores


if __name__ == '__main__':
    calculadora = Calculadora(10, 2) # passando os valores por parâmetro para o método init da classe Calculadora
    print(calculadora.valor_a) # acessando o valor_a repassado para o método init da classe Calculadora
    print(calculadora.soma()) # chamando a função soma da classe Calculadora
    print(calculadora.subtracao()) # chamando a função subtração da classe Calculadora
    print(calculadora.divisao()) # chamando a função divisão da classe Calculadora
    print(calculadora.multiplacacao()) # chamando a função multiplicação da classe Calculadora