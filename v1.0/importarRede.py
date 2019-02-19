
from rnamlp import rnamlp

arq = open("redeNeuralAumentoExtraida.txt", 'r')
linhas = arq.readlines()

# lendo qtd de camadas
qtd_camadas = []
for qtd_neuronios in linhas[0][:-2].split(' '):
    qtd_camadas.append(int(qtd_neuronios))
del linhas[0]

# lendo funcoes de ativacao
funcoes_ativacao = []
for camada in qtd_camadas:
    funcoes = []
    for funcao in linhas[0][:-2].split(' '):
        funcoes.append(int(funcao))
    funcoes_ativacao.append(funcoes)
    del linhas[0]

pesos_rede = []
for i in qtd_camadas:
    camada = []
    for j in range(i):
        neuronio = []
        for peso in linhas[0][:-2].split(' '):
            neuronio.append(float(peso))
        camada.append(neuronio)
        del linhas[0]
    pesos_rede.append(camada)

biases = []
for i in qtd_camadas:
    camada = []
    for bias in linhas[0][:-2].split(' '):
        camada.append(float(bias))
    biases.append(camada)
    del linhas[0]

rna = rnamlp(qtd_camadas, funcoes_ativacao=funcoes_ativacao)
rna.redefinir_rede(pesos_rede, biases)
print(pesos_rede)
arq = open("dadosTreinamentoAdivinha.txt", 'r')
linhas = arq.readlines()

entradas = []
saidas = []
for linha in linhas:
    linha = linha[:-2]
    linha = linha.split(' ')
    entradas.append([float(numero) for numero in linha[:-qtd_camadas[-1]]])
    saidas.append([float(numero) for numero in linha[-qtd_camadas[-1]:]])

'''
acertos, positivo, negativo, falso_positivo, falso_negativo = rna.validar(entradas, saidas, True)
print("Acertos: {}\nPositovos {}\nNegativos {}\nFalso positivo {}\n Falso negativo {}".format(acertos,
                                                                                              positivo,
                                                                                              negativo,
                                                                                              falso_positivo,
                                                                                              falso_negativo))
'''
acertos = rna.validar(entradas, saidas)
print("Acertos {}".format(acertos))