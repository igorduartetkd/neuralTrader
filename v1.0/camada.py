# camada.py

from neuronio import Neuronio


class Camada():
    def __init__(self, qtd_neuronios, taxa_aprendizagem, qtd_camada_anterior=0, funcoes_ativacao=[]):
        if qtd_neuronios != len(funcoes_ativacao):
            funcoes_ativacao = [4] * qtd_neuronios  # tanh caso nao seja definido
        self.__qtd_camada_anterior = qtd_camada_anterior if qtd_camada_anterior != 0 else qtd_neuronios
        self.__neuronios = [Neuronio(taxa_aprendizagem, self.__qtd_camada_anterior, funcao) for funcao in funcoes_ativacao]
        self.__y_camada = []
        self.__funcoes_ativacao = funcoes_ativacao

    def get_pesos(self):
        pesos = [neuronio.get_w() for neuronio in self.__neuronios]
        return pesos

    def get_biases(self):
        biases = [neuronio.get_bias() for neuronio in self.__neuronios]
        return biases

    def get_funcoes_ativacao(self):
        return self.__funcoes_ativacao

    def set_pesos(self, pesos_camada):
        for neuronio, pesos in zip(self.__neuronios, pesos_camada):
            neuronio.set_w(pesos)

    def set_biases(self, biases):
        for neuronio, bias in zip(self.__neuronios, biases):
            neuronio.set_bias(bias)

    def propagar(self, x):
        if len(x) != self.__qtd_camada_anterior:
            print("Quantidade de entradas diferente da definicao")

        self.__y_camada = [neuronio.estimular(x) for neuronio in self.__neuronios]
        return self.__y_camada

    def corrigir(self, deltas):
        if len(deltas) != len(self.__neuronios):
            print("Quantidade de deltas {}"
                  " diferente de neuronios {}"
                  " - metodo corrigir da classe camada".format(str(len(deltas)), str(len(self.__neuronios))))

        proximos_deltas = [0] * self.__neuronios[0].get_numero_entradas()
        for neuronio, delta in zip(self.__neuronios, deltas):
            neuronio.atualizar_pesos(delta)
            novos_deltas = neuronio.get_delta_fatores()
            proximos_deltas = [antigo + novo for antigo, novo in zip(proximos_deltas, novos_deltas)]

        # print("retornando {} proximos deltas".format(str(len(proximos_deltas))))
        return proximos_deltas
