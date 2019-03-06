# neuronio.py
import random
import numpy as np


class Neuronio():
    def __init__(self, taxa_aprendizagem, numero_entradas, funcao_ativacao=4):
        self.__bias = random.uniform(-0.9, 0.9)
        # self.__w = np.random.randn(1, numero_entradas)[0]
        self.__w = [random.uniform(-0.9, 0.9) for _ in range(numero_entradas)]
        self.__taxa_aprendizagem = taxa_aprendizagem
        self.__funcao_ativacao = funcao_ativacao

        self.__I = 0
        self.__y_entrada = []
        self.__delta = 0

        # print("w definido: {}".format(self.__w))

    def get_w(self):
        return self.__w

    def get_bias(self):
        return self.__bias

    def get_taxa_aprendizagem(self):
        return self.__taxa_aprendizagem

    def get_delta(self):
        return self.__delta

    def get_numero_entradas(self):
        return len(self.__w)

    def set_w(self, w):
        self.__w = w

    def set_bias(self, bias):
        self.__bias = bias

    def estimular(self, entradas):
        self.__y_entrada = entradas
        acumulador = np.dot(self.__w, self.__y_entrada)
        acumulador += self.__bias
        self.__I = acumulador
        return self.funcao_ativacao(acumulador, self.__funcao_ativacao)

    def funcao_ativacao(self, entrada, funcao, a=0.2):
        if funcao == 1:  # binaria
            if entrada > 0:
                return 1
            else:
                return 0

        elif funcao == 2:  # linear
            return entrada

        elif funcao == 3:  # sigmoide(x) = 1/(1+e^(-x))
            return 1.0/(1.0 + np.exp(-entrada))

        elif funcao == 4:  # tanh(x) = 2*sigmoide(2x) -1
            return 2.0/(1.0 + np.exp(-2 * entrada)) - 1

        elif funcao == 5:  # ReLU (x) = max{0,x}
            return max(0, entrada)

        elif funcao == 6:  # Leaky ReLU(x, a) = max{ax, x}
            return max(a*entrada, entrada)

        elif funcao == 7:  # ELU(x, a) = {x, x>=0; a*(e^x-1), x<0}
            if entrada >= 0:
                return entrada
            return a*(np.exp(entrada) - 1)

    def derivada_funcao_ativacao(self, entrada, funcao, a=0.2):
        if funcao == 1:  # binaria
                return 1

        elif funcao == 2:  # linear
            return 1

        elif funcao == 3:  # sigmoide'(x) = e^(-x)/(1+e^(-x))²
            return np.exp(-entrada)/((1.0 + np.exp(-entrada)) ** 2)

        elif funcao == 4:  # tanh'(x) = 1 - tanh(x)²
            return 1.0 - (2.0/(1.0 + np.exp(-2 * entrada)) - 1) ** 2

        elif funcao == 5:  # ReLU'(x) = {1, se x>=0; 0, se x<0}
            if entrada < 0:
                return 0
            return 1

        elif funcao == 6:  # Leaky ReLU'(x,a) = {1, x>=0; a, x<0}
            if entrada < 0:
                return a
            return 1

        elif funcao == 7:  # ELU'(x, a) = {1, x>=0; ELU(x, a) + a, x<0}
            if entrada >= 0:
                return 1
            return self.funcao_ativacao(entrada, 7, a) + a

    def calcular_delta(self, dot_camada_adiante):
        self.__delta = dot_camada_adiante * self.derivada_funcao_ativacao(self.__I, self.__funcao_ativacao)
        return self.__delta

    def atualizar_pesos(self, dot_camada_adiante):
        self.calcular_delta(dot_camada_adiante)
        self.__bias += self.__taxa_aprendizagem * self.__delta

        for i in range(len(self.__w)):
            ajuste = self.__taxa_aprendizagem * self.__delta * self.__y_entrada[i]
            self.__w += ajuste

    def get_delta_fatores(self):
        delta_fatores = [self.__delta * w for w in self.__w]
        return delta_fatores
