from calculadorEstatistico import normalizar

list_data = []
list_ultimo = []
list_abertura = []
list_maximo = []
list_minimo = []
list_volume = []
list_variacao = []
nome_arq_leitura = "dadosSeparados2000.txt"
nome_arq_escrita_aumento = "dadosTreinamentoAumento.txt"
nome_arq_escrita_adivinha = "dadosTreinamentoAdivinha.txt"
arq_aumento = open(nome_arq_escrita_aumento, 'w')
arq_adivinha = open(nome_arq_escrita_adivinha, 'w')

def preparar():

    arq1 = open(nome_arq_leitura, 'r')
    linhas_arq1 = arq1.readlines()

    for linha in linhas_arq1[::-1]:
        splitado = linha.strip(' \n').split(' ')
        list_data.append(splitado[0])
        list_ultimo.append(float(splitado[1]))
        list_abertura.append(float(splitado[2]))
        list_maximo.append(float(splitado[3]))
        list_minimo.append(float(splitado[4]))
        list_volume.append(float(splitado[5]))
        list_variacao.append(float(splitado[6]))


def get_treinamento(n_periodos, qtd_testes, tipo_teste='aumento'):
    if qtd_testes + n_periodos + 5 >= len(list_ultimo):
        print("Chegou no final do arquivo de {} ao prepararTreinamento -> getLinhaTreinamento".format(nome_arq_leitura))

    testes_aumento = list()
    saidas_aumento = list()
    testes_adivinha = list()
    saidas_adivinha = list()
    for i in range(qtd_testes):
        teste_aumento = list()
        teste_adivinha = list()
        for j in range(n_periodos):
            teste_aumento.append(list_ultimo[i + j])
            teste_adivinha.append(list_ultimo[i + j])
        # teste de tendencia normaliza apenas dados de entrada
        mini, maxi, teste_aumento = normalizar(teste_aumento)
        resposta = -1
        if list_ultimo[i + n_periodos - 1] * 0.039 < list_ultimo[i + n_periodos + 3] - list_ultimo[i + n_periodos - 1]:
            resposta = 1
        if list_ultimo[i + n_periodos - 1] * 0.039 < list_ultimo[i + n_periodos + 2] - list_ultimo[i + n_periodos - 1]:
            resposta = 1
        if list_ultimo[i + n_periodos - 1] * 0.039 < list_ultimo[i + n_periodos + 1] - list_ultimo[i + n_periodos - 1]:
            resposta = 1
        if list_ultimo[i + n_periodos - 1] * 0.039 < list_ultimo[i + n_periodos] - list_ultimo[i + n_periodos - 1]:
            resposta = 1
        '''
        if -list_ultimo[i + n_periodos - 1] * 0.039 > list_ultimo[i + n_periodos] - list_ultimo[i + n_periodos - 1]:
            resposta = -1
        if -list_ultimo[i + n_periodos - 1] * 0.039 > list_ultimo[i + n_periodos + 1] - list_ultimo[i + n_periodos - 1]:
            resposta = -1
        if -list_ultimo[i + n_periodos - 1] * 0.039 > list_ultimo[i + n_periodos + 2] - list_ultimo[i + n_periodos - 1]:
            resposta = -1
        if -list_ultimo[i + n_periodos - 1] * 0.039 > list_ultimo[i + n_periodos + 3] - list_ultimo[i + n_periodos - 1]:
            resposta = -1
        '''
        armazenar_teste(arq_aumento, mini, maxi, teste_aumento, resposta)
        testes_aumento.append(teste_aumento)
        saidas_aumento.append([resposta])

        # teste de adivinhar normaliza entrada e saida
        teste_adivinha.append(list_ultimo[i + n_periodos])
        mini, maxi, teste_adivinha = normalizar(teste_adivinha)
        testes_adivinha.append(teste_adivinha[:-1])
        resposta = teste_adivinha[-1:][0]
        saidas_adivinha.append(resposta)
        armazenar_teste(arq_adivinha, mini, maxi, teste_adivinha[:-1], resposta)
    if tipo_teste is "aumento":
        return testes_aumento, saidas_aumento
    return testes_adivinha, saidas_adivinha


def armazenar_teste(arq, mini, maxi, teste, saida):
    arq.write(str(mini) + ' ' + str(maxi) + '\n')
    for i in teste:
        arq.write(str(i) + ' ')
    arq.write(str(saida) + '\n')

#preparar()
#get_treinamento(20, 100)