class Error(Exception): # classe Error herdando da Exception
    pass # classe vazia

class InputError(Error): # classe InputError herdando da Error
    def __init__(self, message): # construtor da classe InputError
        self.message = message

while True: # vai executar enquanto a verdade for verdade, rsrs
    try:
        x = int(input('Entre com uma nota de 0 a 10: ')) # se digitar uma letra vai gerar erro e vai cair em 'ValueError', digitando número sai do laço
        print(x)
        if x > 10: # vai mostrar a mensagem se o número digitado for maior que 10
            raise InputError('Nota não pode ser maior que 10') # com raise conseguimos forçar uma exceção, que no caso é InputError()
        elif x < 0: # vai mostrar a mensagem se o número digitado for menor que 0
            raise InputError('Nota não pode ser menor que 0')
        break
    except ValueError:
        print('Valor inválido. Deve-se digitar apenas números.')
    except InputError as ex: # mostrando a mensagem da exceção ao usuário em ex
        print(ex) # imprimindo ex = erro
