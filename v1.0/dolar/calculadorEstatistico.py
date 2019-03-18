'''
arq1 = open("dadosSeparados2000.txt", 'r')
linhas_arq1 = arq1.readlines()

arq_saida = open('dadosEstatisticos.txt', 'w')

list_data = []
list_ultimo = []
list_abertura = []
list_maximo = []
list_minimo = []
list_volume = []
list_variacao = []

for linha in linhas_arq1:
    splitado = linha.split(' ')
    list_data.append(splitado[0])
    list_ultimo.append(float(splitado[1]))
    list_abertura.append(float(splitado[2]))
    list_maximo.append(float(splitado[3]))
    list_minimo.append(float(splitado[4]))
    list_volume.append(float(splitado[5]))
    list_variacao.append(float(splitado[6].replace('\n', '')))
'''


def ifr(dados, numero_periodos=14):
    dimensao = len(dados)
    ifr_saida = [0.]
    soma_ganhos = 0
    soma_perdas = 0
    # para os n primeiros periodos
    for i in range(1, numero_periodos, 1):
        ifr_saida.append(0.)
        variacao = dados[i] - dados[i-1]
        if variacao >= 0.:
            soma_ganhos += variacao
        else:
            soma_perdas -= variacao

    # primeiro ganho medio e perda media
    ganho_medio = soma_ganhos / numero_periodos
    perda_media = soma_perdas / numero_periodos
    fr = ganho_medio/perda_media
    ifr_saida.append(100 - (100/(1 + fr)))

    for i in range(numero_periodos + 1, dimensao, 1):
        variacao = dados[i] - dados[i-1]
        if variacao >= 0.:
            ganho_atual = variacao
            perda_atual = 0.
        else:
            ganho_atual = 0.
            perda_atual = -variacao

        ganho_medio = (ganho_medio*(numero_periodos - 1.) + ganho_atual) / numero_periodos
        perda_media = (perda_media*(numero_periodos - 1.) + perda_atual) / numero_periodos
        fr = ganho_medio / perda_media
        ifr_saida.append(100 - (100 / (1 + fr)))
    return ifr_saida


def MME(dados, numero_periodos):
    mme_saida = []
    k = round((2./(numero_periodos + 1.)), 2)
    dimensao = len(dados)
    soma = 0
    # calculo da primeira media movel (simples)
    for i in range(0, numero_periodos, 1):
        mme_saida.append(0)
        soma += dados[i]
    mms = round(soma/numero_periodos, 2)
    mme = round(((dados[numero_periodos] - mms)*k + mms), 2)
    mme_saida.append(mme)
    for i in range(numero_periodos+1, dimensao, 1):
        mme = round((dados[i] - mme)*k + mme, 2)
        mme_saida.append(mme)

    return mme_saida


def linhaMACD(dados):
    mme26 = MME(dados, 26)
    mme12 = MME(dados, 12)
    linhaMACD_saida = []
    dimensao = len(dados)
    for i in range(0, dimensao, 1):
        linhaMACD_saida.append(round(mme12[i] - mme26[i], 2))

    return linhaMACD_saida


def linha_sinal(dados):
    return MME(dados, 9)


def histogramaMACD(dados):
    linha_macd = linhaMACD(dados)
    linhaDeSinal = linha_sinal(dados)
    histograma_saida = []
    for i in range(0, len(dados), 1):
        histograma_saida.append(round(linha_macd[i]- linhaDeSinal[i], 2))

    return histograma_saida


def MMA(dados, numero_periodos):
    dimensao = len(dados)
    mma_saida = []
    soma = 0
    for i in range(0, numero_periodos, 1):
        soma += dados[i]
        mma_saida.append(0.)

    mma_saida[numero_periodos - 1] = round(soma/numero_periodos, 2)
    for i in range(numero_periodos, dimensao, 1):
        soma -= dados[i-numero_periodos]
        soma += dados[i]
        mma_saida.append(round(soma/numero_periodos, 2))

    return mma_saida


def linhas_DIDI(dados):
    mma3 = MMA(dados, 3)
    mma8 = MMA(dados, 8)
    mma20 = MMA(dados, 20)
    baixa = round(mma3[0] - mma8[0], 2)
    alta = round(mma20[0] - mma8[0], 2)
    didi_baixa_saida = [baixa]
    didi_alta_saida = [alta]
    didi_cruzamento_saida = [0]
    dif_anterior = alta - baixa
    for i in range(1, len(dados), 1):
        baixa = round(mma3[i] - mma8[i], 2)
        alta = round(mma20[i] - mma8[i], 2)
        didi_baixa_saida.append(baixa)
        didi_alta_saida.append(alta)
        # cruzamento
        dif_atual = alta - baixa
        if dif_atual >= 0 and dif_anterior >= 0:
            didi_cruzamento_saida.append(0)
        elif dif_atual < 0 and dif_anterior < 0:
            didi_cruzamento_saida.append(0)
        elif dif_atual >= 0:
            didi_cruzamento_saida.append(1)
        else:
            didi_cruzamento_saida.append(-1)

        dif_anterior = dif_atual

    return didi_baixa_saida, didi_alta_saida, didi_cruzamento_saida


def desvio_padrao(dados, epocas):
    desvio_saida = []
    soma = 0
    for i in range(epocas-1):
        desvio_saida.append(0.)
        soma += dados[i]

    for i in range(epocas-1, len(dados), 1):
        soma += dados[i]
        ma = soma / (epocas)
        soma -= dados[i+1 - epocas]
        acumulador_dp = 0
        for j in range(i - epocas + 1, i, 1):
            acumulador_dp += (dados[j] - ma)*(dados[j] - ma)

        acumulador_dp /= epocas
        acumulador_dp = acumulador_dp ** (1/2)
        desvio_saida.append(round(acumulador_dp, 2))

    return desvio_saida


def bandas_bollinger(dados):
    banda_superior_saida = []
    banda_inferior_saida = []
    fechamento_saida = []
    mma20 = MMA(dados, 20)
    dp = desvio_padrao(dados, 20)
    for i in range(len(dados)):
        superior = round(mma20[i] + 2*dp[i], 2)
        inferior = round(mma20[i] - 2*dp[i], 2)
        fechamento = dados[i]
        banda_superior_saida.append(superior)
        banda_inferior_saida.append(inferior)
        if fechamento < superior and fechamento > inferior:
            fechamento_saida.append(1)
        else:
            fechamento_saida.append(0)

    return [banda_inferior_saida, banda_superior_saida, fechamento_saida]


def normalizar(dados, xnmin=-1, xnmax=1):
    Xmin = min(dados)
    Xmax = max(dados)
    normalizado = [(xnmax - xnmin) * (x - Xmin) / (Xmax - Xmin) + xnmin for x in dados]
    return Xmin, Xmax, normalizado


def desnormalizar(xmin, xmax, normalizado, xnmin=-1, xnmax=1):
    desnormalizado = [round((x - xnmin)*(xmax - xmin)/(xnmax - xnmin) + xmin, 2) for x in normalizado]
    return desnormalizado

'''

indice_forca = ifr(list_ultimo, 14)
print(len(indice_forca))

media_movel = MME(list_ultimo, 20)
print(len(media_movel))

linhamacd = linhaMACD(list_ultimo)
print(len(linhamacd))

linhasinal = MME(list_ultimo, 9)
print(len(linhasinal))

histograma_macd = histogramaMACD(list_ultimo)
print(len(histograma_macd))

mma10 = MMA(list_ultimo, 10)
print(len(mma10))

mma20 = MMA(list_ultimo, 20)
print(len(mma20))

linhadidibaixa, linhadidialta, cruzamentodidi = linhas_DIDI(list_ultimo)
print(len(linhadidibaixa))
print(len(linhadidialta))
print(len(cruzamentodidi))

# dp = desvio_padrao(list_ultimo, 20)
# print(len(dp))
# print(dp)

bandainferior, bandasuperior, fechamento = bandas_bollinger(list_ultimo)
print(len(bandainferior))
print(len(bandasuperior))
print(len(fechamento))
# print(bandainferior)
# print(bandasuperior)
# print(fechamento)




# salvando os dados no arquivo texto
for i in range(len(list_ultimo)):
    arq_saida.write(str(list_data[i]) + ' ' +
                    str(list_ultimo[i]) + ' ' +
                    str(list_abertura[i]) + ' ' +
                    str(list_maximo[i]) + ' ' +
                    str(list_minimo[i]) + ' ' +
                    str(list_volume[i]) + ' ' +
                    str(list_variacao[i]) + ' ' +
                    str(indice_forca[i]) + ' ' +
                    str(linhamacd[i]) + ' ' +
                    str(linhasinal[i]) + ' ' +
                    str(histograma_macd[i]) + ' ' +
                    str(mma10[i]) + ' ' +
                    str(linhadidibaixa[i]) + ' ' +
                    str(linhadidialta[i]) + ' ' +
                    str(cruzamentodidi[i]) + ' ' +
                    str(bandainferior[i]) + ' ' +
                    str(bandasuperior[i]) + ' ' +
                    str(fechamento[i]) + '\n')



mi, ma, dados = normalizar(list_ultimo)
print("minimo {} maximo {}".format(mi, ma))
volta = desnormalizar(mi, ma, dados)
for x, y in zip(list_ultimo, volta):
    if x != y:
        print("x: {} y: {}".format(x, y))
'''