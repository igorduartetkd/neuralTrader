import prepararTreinamento
from rnamlp import rnamlp
'''
arq = open("dadosTreinamentoAumento.txt", 'r')
linhas_arq = arq.readlines()
list_entrada = []
list_y_desejado = []
'''
n_periodos = 17
prepararTreinamento.preparar()
qtd_neuronios = [n_periodos, 17, 1]

funcoes_ativacao = [[4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
                    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
                    [4]]
'''
funcoes_ativacao = [[7, 7, 7, 7, 7, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
                    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
                    [4]]
'''
for neuronios, funcoes in zip(qtd_neuronios, funcoes_ativacao):
    if neuronios != len(funcoes):
        input("Camada com {} neuronios definida, porem {} funcoes de ativacoes definidas".format(neuronios,
                                                                                                len(funcoes)))


rna = rnamlp(qtd_neuronios, taxa_aprendizagem=0.01, funcoes_ativacao=funcoes_ativacao, limiar_parada=0.01)
rna.treinar(prepararTreinamento.get_treinamento(n_periodos, 500))
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

