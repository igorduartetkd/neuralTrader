from calculadorEstatistico import normalizar

list_data = []
list_ultimo = []
list_abertura = []
list_maximo = []
list_minimo = []
list_volume = []
list_variacao = []
nome_arq_leitura = "dadosSeparados-diarioDolarFuturo2002-2012.txt"
nome_arq_escrita_aumento = "dadosTreinamentoAumento-diarioDolarFuturo2002-2012.txt"
nome_arq_escrita_adivinha = "dadosTreinamentoAdivinha-diarioDolarFuturo2002-2012.txt"
arq_aumento = open(nome_arq_escrita_aumento, 'w')
arq_adivinha = open(nome_arq_escrita_adivinha, 'w')

def preparar(inicio=0):

    arq1 = open(nome_arq_leitura, 'r')
    linhas_arq1 = arq1.readlines()

    for linha in linhas_arq1[inicio:]:
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
    contador = 0
    porcent = 101.2 / 100
    for i in range(qtd_testes):
        teste_aumento = list()
        teste_adivinha = list()
        for j in range(n_periodos):
            teste_aumento.append(list_ultimo[i + j])
            teste_adivinha.append(list_ultimo[i + j])
        # teste de tendencia normaliza apenas dados de entrada
        mini, maxi, teste_aumento = normalizar(teste_aumento)
        resposta = -1
        media = 0
        media += list_ultimo[i + n_periodos + 4]
        media += list_ultimo[i + n_periodos + 3]
        media += list_ultimo[i + n_periodos + 2]
        media += list_ultimo[i + n_periodos + 1]
        media += list_ultimo[i + n_periodos]
        media /= 5
        if list_ultimo[i + n_periodos - 1] * porcent < media:
            resposta = 1
            contador += 1
            print(contador)
        '''
        if list_ultimo[i + n_periodos - 1] * porcent < list_ultimo[i + n_periodos + 3]:
            resposta = 1
            contador += 1
            print(contador)
        elif list_ultimo[i + n_periodos - 1] * porcent < list_ultimo[i + n_periodos + 2]:
            resposta = 1
            contador += 1
            print(contador)
        elif list_ultimo[i + n_periodos - 1] * porcent < list_ultimo[i + n_periodos + 1]:
            resposta = 1
            contador += 1
            print(contador)
        elif list_ultimo[i + n_periodos - 1] * porcent < list_ultimo[i + n_periodos]:
            resposta = 1
            contador += 1
            print(contador)
        
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
        arq_teste.write(str(resposta ) + '\n')
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
    #arq.write(str(mini) + ' ' + str(maxi) + '\n')
    for i in teste:
        arq.write(str(i) + ' ')
    arq.write(str(saida) + '\n')


arq_teste = open('arq-saida.txt', 'w')

preparar(0)
get_treinamento(10, 1000)