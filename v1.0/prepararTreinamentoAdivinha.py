
arq = open("dadosNormalizados2000.txt", 'r')
arq_treinamento = open("dadosTreinamentoAdivinha.txt", 'w')
arq_treinamento_aumento = open("dadosTreinamentoAumento.txt", 'w')
linhas_arq = arq.readlines()

list_data = []
list_ultimo = []
list_abertura = []
list_maximo = []
list_minimo = []
list_volume = []
list_variacao = []
list_ifr14 = []
list_linha_macd = []
list_linha_sinal = []
list_histograma_macd = []
list_mma10 = []
list_didi_baixa = []
list_didi_alta = []
list_cruzamento_didi = []
list_bollinger_superior = []
list_bollinger_inferior = []
list_bollinger_fechamento = []

for linha in linhas_arq[:1000]:
    splitado = linha.split(' ')
    list_data.append(splitado[0])
    list_ultimo.append(float(splitado[1]))
    list_abertura.append(float(splitado[2]))
    list_maximo.append(float(splitado[3]))
    list_minimo.append(float(splitado[4]))
    list_volume.append(float(splitado[5]))
    list_variacao.append(float(splitado[6]))
    list_ifr14.append(float(splitado[7]))
    list_linha_macd.append(float(splitado[8]))
    list_linha_sinal.append(float(splitado[9]))
    list_histograma_macd.append(float(splitado[10]))
    list_mma10.append(float(splitado[11]))
    list_didi_baixa.append(float(splitado[12]))
    list_didi_alta.append(float(splitado[13]))
    list_cruzamento_didi.append(float(splitado[14]))
    list_bollinger_inferior.append(float(splitado[15]))
    list_bollinger_superior.append(float(splitado[16]))
    list_bollinger_fechamento.append(float(splitado[17].replace('\n', '')))


for i in range(30, len(list_data) - 30, 1):
    arq_treinamento.write(str(list_ultimo[i]) + ' ' +
                          str(list_abertura[i]) + ' ' +
                          str(list_maximo[i]) + ' ' +
                          str(list_minimo[i]) + ' ' +
                          str(list_volume[i]) + ' ' +
                          str(list_variacao[i]) + ' ' +
                          str(list_ifr14[i]) + ' ' +
                          str(list_linha_macd[i]) + ' ' +
                          str(list_linha_sinal[i]) + ' ' +
                          str(list_histograma_macd[i]) + ' ' +
                          str(list_mma10[i]) + ' ' +
                          str(list_didi_baixa[i]) + ' ' +
                          str(list_didi_alta[i]) + ' ' +
                          str(list_cruzamento_didi[i]) + ' ' +
                          str(list_bollinger_inferior[i]) + ' ' +
                          str(list_bollinger_superior[i]) + ' ' +
                          str(list_bollinger_fechamento[i]) + ' ' +
                          str(list_ultimo[i+1]) + ' ' + '\n')
    subiu = 0.0
    if list_ultimo[i] * 0.039 < list_ultimo[i+4] - list_ultimo[i]:
        subiu = 1.0
    elif list_ultimo[i] * 0.039 < list_ultimo[i+3] - list_ultimo[i]:
        subiu = 1.0
    elif list_ultimo[i] * 0.039 < list_ultimo[i+2] - list_ultimo[i]:
        subiu = 1.0
    elif list_ultimo[i] * 0.039 < list_ultimo[i+1] - list_ultimo[i]:
        subiu = 1.0

    arq_treinamento_aumento.write(str(list_ultimo[i]) + ' ' +
                          str(list_abertura[i]) + ' ' +
                          str(list_maximo[i]) + ' ' +
                          str(list_minimo[i]) + ' ' +
                          str(list_volume[i]) + ' ' +
                          str(list_variacao[i]) + ' ' +
                          str(list_ifr14[i]) + ' ' +
                          str(list_linha_macd[i]) + ' ' +
                          str(list_linha_sinal[i]) + ' ' +
                          str(list_histograma_macd[i]) + ' ' +
                          str(list_mma10[i]) + ' ' +
                          str(list_didi_baixa[i]) + ' ' +
                          str(list_didi_alta[i]) + ' ' +
                          str(list_cruzamento_didi[i]) + ' ' +
                          str(list_bollinger_inferior[i]) + ' ' +
                          str(list_bollinger_superior[i]) + ' ' +
                          str(list_bollinger_fechamento[i]) + ' ' +
                          str(subiu) + ' ' + '\n')
