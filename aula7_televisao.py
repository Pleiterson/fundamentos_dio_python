class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5

    # método para verifica se e a TV está ligada ou não
    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True
    
    # método para aumentar de canal
    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1 # incrementando canal
        
    # método para diminuir de canal
    def diminui_canal(self):
        if self.ligada:
            self.canal -= 1 # decrementando canal


if __name__ == '__main__':
    televisao = Televisao() # criando uma TV conforme a classe Televisao
    print('Televisão está ligada: {}'.format(televisao.ligada))

    televisao.power() # TV ligada
    print('Televisão está ligada: {}'.format(televisao.ligada))

    televisao.power() # TV desligada
    print('Televisão está ligada: {}'.format(televisao.ligada))
    print('Canal: {}'.format(televisao.canal))

    televisao.power() # TV ligada
    print('Televisão está ligada: {}'.format(televisao.ligada))

    televisao.aumenta_canal()
    televisao.aumenta_canal()
    print('Canal: {}'.format(televisao.canal))

    # televisao.diminui_canal()
    # print('Canal: {}'.format(televisao.canal))