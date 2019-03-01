
from rnamlp import rnamlp
nome_arq_treinamento = "dadosTreinamentoAumento.txt"

arq = open("redeNeuralAumentoExtraida.txt", 'r')
linhas = arq.readlines()

# lendo qtd de camadas
qtd_camadas = []
for qtd_neuronios in linhas[0].strip(' \n').split(' '):
    qtd_camadas.append(int(qtd_neuronios))
del linhas[0]

# lendo funcoes de ativacao
funcoes_ativacao = []
for camada in qtd_camadas:
    funcoes = []
    for funcao in linhas[0].strip(' \n').split(' '):
        funcoes.append(int(funcao))
    funcoes_ativacao.append(funcoes)
    del linhas[0]

pesos_rede = []
for i in qtd_camadas:
    camada = []
    for j in range(i):
        neuronio = []
        for peso in linhas[0].strip(' \n').split(' '):
            neuronio.append(float(peso))
        camada.append(neuronio)
        del linhas[0]
    pesos_rede.append(camada)

biases = []
for i in qtd_camadas:
    camada = []
    for bias in linhas[0].strip(' \n').split(' '):
        camada.append(float(bias))
    biases.append(camada)
    del linhas[0]

rna = rnamlp(qtd_camadas, funcoes_ativacao=funcoes_ativacao)
rna.redefinir_rede(pesos_rede, biases)
arq = open(nome_arq_treinamento, 'r')
linhas = arq.readlines()

entradas = []
saidas = []
for linha in linhas[1::2]:
    linha = linha.strip(' \n').split(' ')
    entradas.append([float(numero) for numero in linha[:-qtd_camadas[-1]]])
    saidas.append([float(numero) for numero in linha[-qtd_camadas[-1]:]])


acertos, positivo, negativo, falso_positivo, falso_negativo = rna.validar(entradas, saidas, True)
print("Acertos: {}\nPositovos {}\nNegativos {}\nFalso positivo {}\n Falso negativo {}".format(acertos,
                                                                                              positivo,
                                                                                              negativo,
                                                                                              falso_positivo,
                                                                                              falso_negativo))
'''
acertos = rna.validar(entradas, saidas)
print("Acertos {}".format(acertos))
'''