
from rnamlp import rnamlp

arq = open("dadosTreinamentoAumento.txt", 'r')
linhas_arq = arq.readlines()
list_entrada = []
list_y_desejado = []


qtd_neuronios = [17, 23, 1]

funcoes_ativacao = [[4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
                    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
                    [4]]

for neuronios, funcoes in zip(qtd_neuronios, funcoes_ativacao):
    if neuronios != len(funcoes):
        input("Camada com {} neuronios definida, porem {} funcoes de ativacoes definidas".format(neuronios,
                                                                                                        len(funcoes)))

for linha in linhas_arq:
    linha = linha.replace('\n', '').strip()
    splitado = linha.split(' ')
    if len(splitado) - 1 != qtd_neuronios[0]:
        input("Entrada definida com {} neuronios, porem contem {} no arquivo lido".format(qtd_neuronios[0],
                                                                                          len(splitado) - 1))

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

