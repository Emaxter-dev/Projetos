from enum import Enum

#Definindo a classe dos Status do Elevador
class StatusElevador(Enum):
    PARADO = 'Parado'
    DESCENDO = 'Descendo'
    SUBINDO = 'Subindo'

#Definindo a classe do Elevador
class Elevador:
    def __init__(self, capacidade_maxima: int, peso_maximo: int):
        if capacidade_maxima > 6:
            raise ValueError('Capacidade máxima excedida!')
        if peso_maximo > 500:
            raise ValueError('Peso máximo excedido!')
        
#Definindo propriedades iniciais

        self.andar_atual = 0
        self.porta_aberta = False
        self.status = StatusElevador.PARADO
        self.capacidade_maxima = capacidade_maxima
        self.passageiros = 0
        self.rota = []

#Função para entrar passageiros

    def entrar_passageiros(self, quantidade: int):
        if not self.porta_aberta or self.status != StatusElevador.PARADO:
            raise RuntimeError('Passageiros só podem entrar com o elevador parado e porta aberta!')
        
        if quantidade <= 0:
            raise ValueError('Quantidade inválida')
        
        if self.passageiros + quantidade > self.capacidade_maxima:
            raise ValueError('Capacidade máxima excedida!')
        
        self.passageiros += quantidade

#Função para sair passageiros

    def sair_passageiros(self, quantidade: int):
        if not self.porta_aberta or self.status != StatusElevador.PARADO:
            raise RuntimeError('Passageiros só podem sair com o elevador parado e porta aberta!')
        
        if quantidade <= 0 or quantidade > self.passageiros:
            raise ValueError('Quantidade inválida.')
        
        self.passageiros -= quantidade

#Função para selecionar andares

    def selecionar_andares(self, andares):
        if andares is None:
            raise TypeError('Andar inválido')
        
        if not self.porta_aberta:
            raise RuntimeError('Os andares só podem ser selecionados com porta aberta.')
        
        for andar in andares:
            if andar != self.andar_atual and andar not in self.rota:
                self.rota.append(andar)

#Função para fechar as portas

    def fechar_portas(self):
        if not self.rota:
            raise RuntimeError('Não há rota definida.')
        
        self.porta_aberta = False
        self.definir_status()

#Função para abrir as portas

    def abrir_portas(self):
        self.porta_aberta = True
        self.status = StatusElevador.PARADO

#Função para status

    def definir_status(self):
        if not self.rota:
            return
        
        if self.rota[0] > self.andar_atual:
            self.status = StatusElevador.SUBINDO
            self.rota.sort()
        else:
            self.status = StatusElevador.DESCENDO
            self.rota.sort(reverse = True)

#Função para mover

    def mover(self):
        if self.porta_aberta:
            raise RuntimeError('O elevador não pode se mover com a porta aberta!')
        
        if not self.rota:
            return
        
        proximo_andar = self.rota.pop(0)
        self.andar_atual = proximo_andar

        self.abrir_porta()

        if self.rota:
            self.fechar_porta()

#Definindo a classe que cria o objeto Elevador
class ElevadorFactory:
    def __init__(self):
            pass

    def criar_elevador(self, peso_maximo: int, capacidade_maxima: int) -> Elevador:
        return Elevador(peso_maximo, capacidade_maxima)