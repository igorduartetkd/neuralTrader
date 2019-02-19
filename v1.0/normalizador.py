
from sklearn import preprocessing

arq = open("dadosEstatisticos.txt", 'r')
arq_normalizado = open("dadosNormalizados2000.txt", 'w')
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

for linha in linhas_arq[::-1]:
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
    list_cruzamento_didi.append(int(splitado[14]))
    list_bollinger_inferior.append(float(splitado[15]))
    list_bollinger_superior.append(float(splitado[16]))
    list_bollinger_fechamento.append(int(splitado[17].replace('\n', '')))



list_normalizada= preprocessing.normalize([list_ultimo, list_abertura, list_maximo, list_minimo,list_volume,
                                           list_variacao, list_ifr14, list_linha_macd, list_linha_sinal,
                                           list_histograma_macd, list_mma10, list_didi_baixa, list_didi_alta,
                                           list_cruzamento_didi, list_bollinger_inferior, list_bollinger_superior,
                                           list_bollinger_fechamento])


for i in range(0, len(list_normalizada[0]), 1):
    arq_normalizado.write(list_data[i] + ' ' +
                          str(list_normalizada[0][i]) + ' ' +
                          str(list_normalizada[1][i]) + ' ' +
                          str(list_normalizada[2][i]) + ' ' +
                          str(list_normalizada[3][i]) + ' ' +
                          str(list_normalizada[4][i]) + ' ' +
                          str(list_normalizada[5][i]) + ' ' +
                          str(list_normalizada[6][i]) + ' ' +
                          str(list_normalizada[7][i]) + ' ' +
                          str(list_normalizada[8][i]) + ' ' +
                          str(list_normalizada[9][i]) + ' ' +
                          str(list_normalizada[10][i]) + ' ' +
                          str(list_normalizada[11][i]) + ' ' +
                          str(list_normalizada[12][i]) + ' ' +
                          str(list_normalizada[13][i]) + ' ' +
                          str(list_normalizada[14][i]) + ' ' +
                          str(list_normalizada[15][i]) + ' ' +
                          str(list_normalizada[16][i]) + ' ' + '\n')

