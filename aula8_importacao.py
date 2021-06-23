from aula7_televisao import Televisao # importando a classe Televisao do arquivo aula7_televisao
from aula7_calculadora1 import Calculadora # importando a classe Calculadora do arquivo aula7_calculadora1
from aula8_contador_letras import contador_letras, teste # importando e acessando os métodos contador_letras e teste do arquivo aula8_contador_letras

# método main
if __name__ == '__main__':
    televisao = Televisao()
    print(televisao.ligada)

    televisao.power()
    print(televisao.ligada)

    calculadora = Calculadora(5, 10)
    print(calculadora.soma())

    lista = ['cachorro', 'gato', 'elefante']
    total_letras = contador_letras(lista)
    print('total de letras por palavra de lista: {}'.format(total_letras))
    print(teste())