from datetime import date, time, datetime, timedelta # importando os arquivos do python para trabalhar com datas e horas

def trabalhando_com_datetime():
    data_atual = datetime.now() # acessando a data e hora atual com milissegundos
    print(data_atual)
    print(data_atual.strftime('%d/%m/%Y %H:%M:%S')) # convertendo a data para o formato desejado, no caso dd/mm/aaaa hh:mm:ss
    print(data_atual.strftime('%c')) # converte a data com o dia da semana, mês, dia, hora, minuto, segundo e ano 'Wed Jun 23 15:36:03 2021' 
    print(data_atual.day) # mostrando apenas o dia da data atual, consegue buscar os dados separados, mes, ano, hora, minuto, etc.
    print(data_atual.weekday()) # mostrando o valor da semana que está atualmente, quarta = wednesday = 2. Iniciando sempre de segunda-feira

    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabádo', 'Domingo') # tupla dos dias da semana, não muda, portanto, imutável
    print(tupla[data_atual.weekday()]) # pegando o dia da semana em português conforme o dia da semama em data_atual.weekday()

    data_criada = datetime(2018, 6, 20, 15, 30, 20) # criando uma data diferente da atual
    print(data_criada) # imprimindo a data criada
    print(data_criada.strftime('%c'))

    data_string = '01/01/2019 12:20:22' # data em string a ser convertida em datetime
    print(type(data_string))
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y %H:%M:%S') # convertendo a data string acima em datetime
    print(data_convertida) # imprimindo a data convertida
    print(type(data_convertida))

    nova_data = data_convertida - timedelta(days=365, hours=2, minutes=15) # timedelta conseguidos subtrair as datas, conseguimos manipular com operadores matemáticos
    print(nova_data) # imprimindo o resultado da operação acima, subtraiu 1 ano, 2 horas e 15 minutos

def trabalhando_com_date():
    data_atual = date.today() # pegando a data atual
    print(data_atual)
    print(type(data_atual)) # imprimindo o tipo da data_atual 'datetime.date'

    data_atual_str = data_atual.strftime('%A %B %Y') # convertendo a data para o formato desejado, no caso A = semana, B = mês, Y = ano
    print(data_atual_str)
    print(type(data_atual_str)) # imprimindo o tipo da data_atual_str 'str' string

def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30) # definindo os valores do horário
    print(horario)
    print(type(horario)) # imprimindo o tipo do horario 'datetime.date'

    horario_str = horario.strftime('%H:%M:%S') # convertendo a hora para o formato desejado, no caso H:M:S
    print(horario_str)
    print(type(horario_str)) # imprimindo o tipo do horario_str 'str' string

if __name__ == '__main__':
    # trabalhando_com_date()
    # trabalhando_com_time()
    trabalhando_com_datetime()
