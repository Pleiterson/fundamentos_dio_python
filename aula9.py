import shutil # biblioteca para manipulação de arquivos, copiar, mover, etc.

def escrever_arquivo(texto):
    diretorio = 'D:/dev/repos/fundamentos_dio_python/teste.txt' # caminho e nome do arquivo
    arquivo = open(diretorio, 'w') # open gera o arquivo desejado, w escreve uma nova escrita no conteúdo do arquivo já existente
    arquivo.write(texto) # escrevendo o texto repassado
    arquivo.close() # fechando o arquivo

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a') # a realiza um novo texto de escrita no arquivo já existente
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r') # r refere-se a leitura do arquivo
    texto = arquivo.read() # lendo o arquivo
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    #print(aluno_nota)

    aluno_nota = aluno_nota.split('\n')
    #print(aluno_nota)

    lista_media = []
    for x in aluno_nota:
        lista_notas = x.split(',') # colocando todos os itens da linha em uma lista ['Cesar','7','9','3','8']
        aluno = lista_notas[0] # colocando o nome do aluno na posição 0 em aluno
        lista_notas.pop(0) # adicionando as notas dos alunos na lista_notas
        print(aluno) # imprimindo aluno 'Cesar'
        print(lista_notas) # imprimindo lista_notas ['7','9','3','8']

        media = lambda notas: sum([int(i) for i in notas]) / 4 # calculando a média das notas, transforma os números em inteiros, soma , faz a média e retorna
        print(media(lista_notas))

        lista_media.append({aluno:media(lista_notas)}) # adicionando os dados do aluno e a sua média em lista_media
    return lista_media
        #print(sum(lista_notas))

def copia_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, 'D:/dev/repos/fundamentos_dio_python/aula09/') # copiando o arquivo 'notas.txt' para a pasta informada

def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, 'D:/dev/repos/fundamentos_dio_python/aula09/notas_alunos/notas_alunos.txt') # movendo o arquivo 'notas.txt' para a pasta informada com outro nome 'notas_alunos.txt'

# método main
if __name__ == '__main__':
    escrever_arquivo('Primeira linha.\n') # chamado a função escrever_arquivo() e escreve um texto no arquivo 'teste.txt'
    atualizar_arquivo('teste.txt', 'Segunda linha.\n') # chamado a função atualizar_arquivo() e atualiza com o texto no arquivo 'teste.txt'
    ler_arquivo('teste.txt')

    aluno = 'Cesar,7,9,3,8\n'
    aluno1 = 'Felipe,7,8,5,6\n'
    atualizar_arquivo('notas.txt', aluno)
    atualizar_arquivo('notas.txt', aluno1)
    ler_arquivo('notas.txt')

    lista_media = media_notas('notas.txt') # definindo a lista_media e chamado a função media_notas()
    print(lista_media) #imprime lista_media

    copia_arquivo('notas.txt') # chamado o método copia_arquivo() para copiar o arquivo 'notas.txt'
    move_arquivo('notas.txt') # chamado o método move_arquivo() para copiar o arquivo 'notas.txt'
