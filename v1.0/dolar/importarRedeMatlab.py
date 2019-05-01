import montarRedeMatlab
from rnamlp import rnamlp
nome_arq_treinamento = "dadosTreinamentoAumento-diarioDolarFuturo2002-2012.txt"

#montarRedeMatlab.montar()
arq = open("redeNeuralExtraidaMatlab2.txt", 'r')
linhas = arq.readlines()

# lendo qtd de camadas
qtd_camadas = []
for qtd_neuronios in linhas[0].strip(' \n').split(' '):
    qtd_camadas.append(int(qtd_neuronios))
del linhas[0]
print(qtd_camadas)
'''
# lendo funcoes de ativacao
funcoes_ativacao = []
for camada in qtd_camadas[1:]:
    funcoes = []
    for funcao in linhas[0].strip(' \n').split(' '):
        funcoes.append(int(funcao))
    funcoes_ativacao.append(funcoes)
    del linhas[0]
'''
pesos_rede = []
for i in qtd_camadas[1:]:
    camada = []
    for j in range(i):
        neuronio = []
        for peso in linhas[0].strip(' \n').split(' '):
            neuronio.append(float(peso))
        camada.append(neuronio)
        del linhas[0]
    pesos_rede.append(camada)

biases = []
for i in qtd_camadas[1:]:
    camada = []
    for bias in linhas[0].strip(' \n').split(' '):
        camada.append(float(bias))
    biases.append(camada)
    del linhas[0]


print(pesos_rede)
print(biases)
#rna = rnamlp(qtd_camadas, funcoes_ativacao=funcoes_ativacao, com_camada_entrada=True)
rna = rnamlp(qtd_neuronios_camadas=qtd_camadas, com_camada_entrada=True)
rna.redefinir_rede(pesos_rede, biases)
arq = open(nome_arq_treinamento, 'r')
linhas = arq.readlines()

entradas = []
saidas = []
for linha in linhas[1:]:
    linha = linha.strip(' \n').split(' ')
    entradas.append([float(numero) for numero in linha[:-qtd_camadas[-1]]])
    saidas.append([float(numero) for numero in linha[-qtd_camadas[-1]:]])


acertos, positivo, negativo, falso_positivo, falso_negativo = rna.validar(entradas, saidas, True)
if positivo is not 0 and negativo is not 0:
    print("Acertos: {}\nPositovos {} -> {}%"
          "\nNegativos {} -> {}%"
          "\nFalso positivo {} -> {}%"
          "\n Falso negativo {} -> {}%".format(acertos,
                                          positivo, round(100 * positivo / (positivo+falso_positivo), 2),
                                          negativo, round(100 * negativo / (negativo + falso_negativo), 2),
                                          falso_positivo, round((100 * falso_positivo / (falso_positivo + positivo)), 2),
                                          falso_negativo, round(100 * falso_negativo / (falso_negativo + negativo), 2)))
else:
    print("positivos ou negativos deu zerado (problema pode ser no arredondamento)")
'''
acertos = rna.validar(entradas, saidas)
print("Acertos {}".format(acertos))
'''