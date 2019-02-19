
from rnamlp import rnamlp

arq = open("dadosTreinamentoAumento.txt", 'r')
linhas_arq = arq.readlines()
list_entrada = []
list_y_desejado = []


'''
for linha in linhas_arq:
    splitado = linha.split(' ')
    list_y_desejado.append([float(splitado[17].replace('\n', ''))])
    list_entrada.append([float(splitado[0]), float(splitado[1]), float(splitado[2]), float(splitado[3]),
                         float(splitado[4]), float(splitado[5]), float(splitado[6]), float(splitado[7]),
                         float(splitado[8]), float(splitado[9]), float(splitado[10]), float(splitado[11]),
                         float(splitado[12]), float(splitado[13]), float(splitado[14]), float(splitado[15]),
                         float(splitado[16])])

for linha in linhas_arq:
    splitado = linha.split(' ')
    list_entrada.append([float(splitado[0]), float(splitado[1])])
    list_y_desejado.append([float(splitado[2])])
'''
qtd_neuronios = [21, 23, 1]

funcoes_ativacao = [[4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
                    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
                    [4]]

for linha in linhas_arq:
    linha = linha.replace('\n', '').strip()
    splitado = linha.split(' ')
    list_y_desejado.append([float(splitado[qtd_neuronios[0]])])
    list_entrada.append([float(splitado[i]) for i in range(qtd_neuronios[0])])
# qtd_neuronios = [17, 20, 1]
# funcoes_ativacao = [[4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
#                    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3],
#                    [3]]

'''
funcoes_ativacao = [[4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
                    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
                    [3]]
                    '''

rna = rnamlp(qtd_neuronios, taxa_aprendizagem=0.001, funcoes_ativacao=funcoes_ativacao, limiar_parada=0.001)
rna.treinar(list_entrada, list_y_desejado)
camadas, biases, funcoes_ativacao = rna.extrair_rede()
arq = open("redeNeuralAumentoExtraida.txt", 'w')

for qtd in qtd_neuronios:
    arq.write(str(qtd) + ' ')
arq.write('\n')
for camada in funcoes_ativacao:
    for funcao in camada:
        arq.write(str(funcao) + ' ')
    arq.write('\n')

for camada in camadas:
    for neuronio in camada:
        for peso in neuronio:
            arq.write(str(peso) + ' ')
        arq.write('\n')

for camada in biases:
    for bias in camada:
        arq.write(str(bias) + ' ')
    arq.write('\n')

