
import matplotlib.pyplot as plt

arq = open("dadosNormalizados2000.txt", 'r')

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



for linha in linhas_arq:
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



plt.subplot(5, 2, 1)
plt.plot(list_ifr14)
plt.ylabel('IFR14')
plt.grid(True)

plt.subplot(5, 2, 2)
plt.plot(list_linha_macd)
plt.ylabel('MACD l')
plt.grid(True)

plt.subplot(5, 2, 3)
plt.plot(list_linha_sinal)
plt.ylabel('MACD s')
plt.grid(True)

plt.subplot(5, 2, 4)
plt.plot(list_histograma_macd)
plt.ylabel('MACD h')
plt.grid(True)

plt.subplot(5, 2, 5)
plt.plot(list_mma10)
plt.ylabel('MMA10')
plt.grid(True)

plt.subplot(5, 2, 6)
plt.plot(list_didi_baixa)
plt.plot(list_didi_alta)
plt.ylabel('DIDI')
plt.grid(True)

plt.subplot(5, 2, 7)
plt.plot(list_cruzamento_didi)
plt.ylabel('DIDI C')
plt.grid(True)

plt.subplot(5, 2, 8)
plt.plot(list_bollinger_inferior)
plt.plot(list_bollinger_superior)
plt.ylabel('BOLLINGER')
plt.grid(True)

plt.subplot(5, 2, 9)
plt.plot(list_bollinger_fechamento)
plt.ylabel('boll F.')
plt.grid(True)

plt.subplot(5, 2, 10)
plt.plot(list_ultimo)
plt.ylabel('DADOS')
plt.grid(True)

plt.show()
