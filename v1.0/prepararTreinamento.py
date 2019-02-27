arq_name = "dadosSeparados2000.txt"
arq1 = open(arq_name, 'r')
linhas_arq1 = arq1.readlines()

list_data = []
list_ultimo = []
list_abertura = []
list_maximo = []
list_minimo = []
list_volume = []
list_variacao = []

for linha in linhas_arq1[::-1]:
    splitado = linha.strip(' \n').split(' ')
    list_data.append(splitado[0])
    list_ultimo.append(float(splitado[1]))
    list_abertura.append(float(splitado[2]))
    list_maximo.append(float(splitado[3]))
    list_minimo.append(float(splitado[4]))
    list_volume.append(float(splitado[5]))
    list_variacao.append(float(splitado[6]))
print(list_data)

def getLinhaTreinamento(n_periodos, inicio):
    if inicio + n_periodos >= len(list_ultimo):
        print("Chegou no final do arquivo de {} ao prepararTreinamento -> getLinhaTreinamento".format(arq_name))

    entrada = list()
    for i in range(inicio, n_periodos):
        entrada.append(list_ultimo[i])

    return entrada, list_ultimo[n_periodos]
