import random


class ChuteONumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 0
        self.valor_maximo = 200
        self.palpite = 0
        self.tentativas = 0

    def Iniciar(self):
        self.valor_aleatorio = self.GerarValor()
        self.PalpiteDoUsuario()

        while self.palpite != self.valor_aleatorio:
            if self.palpite > self.valor_aleatorio:
                print('Digite um valor menor.')
                self.PalpiteDoUsuario()

            elif self.palpite < self.valor_aleatorio:
                print('Digite um valor maior.')
                self.PalpiteDoUsuario()

        print(f'Parabéns, você acertou após {self.tentativas} tentativas!')

    def PalpiteDoUsuario(self):
        self.tentativas += 1
        try:
            self.palpite = int(
                input(f'Digite um valor entre {self.valor_minimo} e {self.valor_maximo}: '))
        except ValueError:
            print('Você deve digitar apenas números.')
            self.PalpiteDoUsuario()

    def GerarValor(self):
        return random.randint(self.valor_minimo, self.valor_maximo)


iniciar_jogo = ChuteONumero()
iniciar_jogo.Iniciar()
