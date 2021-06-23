
lista = [1, 10]

# tudo que estiver dentro do try vai cair nas exceções
try: # ocorrendo um erro na primeira linha, já para a execução dos demais códigos
    divisao = 10 / 1 # se alterar 1 por 0, vai cair em 'ZeroDivisionError'
    numero = lista[1] # se alterar o 1 por 3 vai cair em 'IndexError'
    arquivo = open('teste.txt', 'r') # se alterar o nome do arquivo, vai cair em 'Exception'
    texto = arquivo.read() # lendo o arquivo
except ZeroDivisionError:
    print('Não é possível realizar divisão por 0') # informa quando há uma divisão por zero
except ArithmeticError:
    print('Houve um erro ao realizar uma operação aritmética') # idem ao 'ZeroDivisionError'
except IndexError:
    print('Erro ao acessar um índice inválido da lista') # informa quando tenta acessar um índice inexistente na lista
except Exception as ex:
    print('Erro desconhecido. Erro: {}'.format(ex)) # qualquer erro que aparecer, vai ser armazendo no ex e mostrado ao usuário
else: # vai executar quando não ocorrer nenhuma exceção
    print('Executa quando não ocorre exceção') # se não encontrar nenhuma exceção (exception) vai entrar nesta mensagem
finally: # vai executar independente do erro, não entra no bloco try
    print('Sempre executa') # sempre vai aparecer
    print('Fechando arquivo') # vai fechar o arquivo, mesmo dando o erros nos exceptions
    arquivo.close() # fecha o arquivo
