# rnamlp.py

from camada import Camada
import numpy as np


class rnamlp():
    def __init__(self, qtd_neuronios_camadas=[2, 2, 2, 1],
                 taxa_aprendizagem=0.4,
                 funcoes_ativacao=[],
                 limiar_parada=0.01,
                 com_camada_entrada=True):
        self.__limiar_parada = limiar_parada
        self.__camadas = []
        #self.__camadas = [Camada(qtd_neuronios_camadas[0], taxa_aprendizagem, funcoes_ativacao=funcoes_ativacao[0])]
        self.__com_camada_entrada = com_camada_entrada
        self.__funcoes_ativacao = funcoes_ativacao
        if funcoes_ativacao == []:
            self.__funcoes_ativacao = [[4 for _ in range(j)] for j in qtd_neuronios_camadas[1:]]
        for i in range(len(qtd_neuronios_camadas) - 1):
            self.__camadas.append(Camada(qtd_neuronios_camadas[i+1],
                                         taxa_aprendizagem,
                                         qtd_neuronios_camadas[i],
                                         self.__funcoes_ativacao[i]))

    def extrair_rede(self):
        pesos_camadas = [camada.get_pesos() for camada in self.__camadas]
        biases_camadas = [camada.get_biases() for camada in self.__camadas]
        funcoes_ativacao = [camada.get_funcoes_ativacao() for camada in self.__camadas]
        return pesos_camadas, biases_camadas, funcoes_ativacao

    def redefinir_rede(self, pesos_camadas, biases_camadas):
        for camada, pesos, biases in zip(self.__camadas, pesos_camadas, biases_camadas):
            camada.set_pesos(pesos)
            camada.set_biases(biases)

    def forward(self, entrada):
        saida_camada_anterior = entrada

        for camada in self.__camadas:
            saida_camada_anterior = camada.propagar(saida_camada_anterior)

        return saida_camada_anterior

    def backward(self, erros):
        if erros == [0] * len(erros):
            return
        for camada in self.__camadas[::-1]:
            erros = camada.corrigir(erros)

    def __ciclo_treinamento(self, entradas, saidas):
        erro_medio_quadratico = 0
        for entrada, saidas_esperadas in zip(entradas, saidas):
            saida_rede = self.forward(entrada)
            erros = [saida_esperada - saida for saida_esperada, saida in zip(saidas_esperadas, saida_rede)]
            self.backward(erros)
            erro_medio_quadratico += sum([e ** 2 for e in erros]) / 2

        erro_medio_quadratico /= len(entradas)
        return erro_medio_quadratico

    def treinar(self, entradas, saidas, ciclos = 1000000):

        erro_medio_quadratico_anterior = 0
        for ciclo in range(ciclos):
            erro_medio_quadratico = self.__ciclo_treinamento(entradas, saidas)
            print("Ciclo {}  erro medio quadratico {}".format(str(ciclo), str(erro_medio_quadratico)))
            if erro_medio_quadratico <= self.__limiar_parada:
                print("Atingiu o limiar de parada {} e {}".format(
                    np.abs(erro_medio_quadratico - erro_medio_quadratico_anterior), self.__limiar_parada))
                break
            '''
            if np.abs(erro_medio_quadratico - erro_medio_quadratico_anterior) <= self.__limiar_parada:
                print("Atingiu o limiar de parada {} e {}".format(np.abs(erro_medio_quadratico - erro_medio_quadratico_anterior), self.__limiar_parada))
                break
            '''
            erro_medio_quadratico_anterior = erro_medio_quadratico

    def validar(self, entradas, saidas, saida_binaria=False):
        acertos = 0
        positivo = 0
        negativo = 0
        falso_positivo = 0
        falso_negativo = 0
        for entrada, saidas_esperadas in zip(entradas, saidas):
            saidas_rede = self.forward(entrada)
            if saida_binaria:
                erros = [round(saida_esperada - saida) for saida_esperada, saida in zip(saidas_esperadas, saidas_rede)]
                print("Saida esperada {} saida da rede {}".format(saidas_esperadas[0], saidas_rede[0]))
                if erros == [0] * len(erros):
                    acertos += 1
                s_esp = saidas_esperadas[0]
                s_rede = saidas_rede[0]
                print("saida esperada {} saida da rede {}".format(s_esp, s_rede))
                if round(s_esp) == 1 and round(s_rede) == 1:
                    positivo += 1
                elif round(s_esp) == 1 and round(s_rede) != 1:
                    falso_negativo += 1
                elif (round(s_esp) == 0 or round(s_esp) == -1) and round(s_rede) == round(s_esp):
                    negativo += 1
                elif (round(s_esp) == 0 or round(s_esp) == -1) and round(s_rede) != round(s_esp):
                    falso_positivo += 1
            else: # saida nao binaria
                erros = [saida_esperada - saida for saida_esperada, saida in zip(saidas_esperadas, saidas_rede)]
                print("Saida esperada {} saida da rede {}".format(saidas_esperadas[0], saidas_rede[0]))
                if erros == [0] * len(erros):
                    acertos += 1
        if saida_binaria:
            return acertos, positivo, negativo, falso_positivo, falso_negativo
        else:
            return acertos

'''
if __name__ == '__main__':
    rede = rnamlp()
    pesos = [[[111, 112], [121, 122]], [[211, 212], [221, 222]], [[311, 312]]]
    biases = [[11, 12], [21, 22], [31]]
    rede.redefinir_rede(pesos, biases)
    pesos2, biases2 = rede.extrair_rede()
    print(pesos2)

'''
