import calculadorEstatistico
import fonte
import datetime

registros = []
nome_arq_escrita_aumento = "dadosTreinamento2.txt"
arq = open(nome_arq_escrita_aumento, 'w')

def preparar():
    global registros
    registros = fonte.getRegistrosSeparados('PETR4.SA')


def remover_primeira_ultima_hora(registros):
    novos_registros = []
    for dia in registros:
        data_inicio = dia[-1][0]
        data_fim = dia[0][0]
        dia = [x for x in dia[::-1] if not is_primeira_ultima_hora(data_inicio, data_fim, x[0])]
        novos_registros.append(dia)
    return novos_registros


def is_primeira_ultima_hora(data_inicio, data_fim, data):
    data_inicio = milis2data(data_inicio)
    data_fim = milis2data(data_fim)
    data = milis2data(data)
    if (data - data_inicio).seconds < 3600:
        return True
    if (data_fim - data).seconds < 3600:
        return True
    return False


def milis2data(milissegundos):
    return datetime.datetime.fromtimestamp(milissegundos / 1000.0)

def armazenar_teste(arq, mini, maxi, teste, saida):
    arq.write(str(mini) + ' ' + str(maxi) + '\n')
    for i in teste:
        arq.write(str(i) + ' ')
    arq.write(str(saida) + '\n')


def calcular_saida_esperada(media, ultimo, tipo=2):
    saida_esperada = 0
    if tipo == 1:
        if media < ultimo:
            saida_esperada = 1
        elif media > ultimo:
            saida_esperada = -1

    elif tipo == 2:
        if media * 1.001 < ultimo:
            saida_esperada = 1
        elif media * 0.999 > ultimo:
            saida_esperada = -1

    return saida_esperada

def montar_linha_treinamento(dados):
    media_ultimos = calculadorEstatistico.media(dados[-5:-1])
    saida_esperada = calcular_saida_esperada(media_ultimos, dados[-1])

    mini, maxi, dados_normalizados = calculadorEstatistico.normalizar(dados[:-1])
    armazenar_teste(arq, mini, maxi, dados_normalizados, saida_esperada)


def get_apenas_precos(registros):
    novo_registro = []
    for dia in registros:
        dia = [x[1] for x in dia]
        novo_registro.append(dia)
    return novo_registro


def criar_treinamento(janela_size):
    global registros
    preparar()
    registros = remover_primeira_ultima_hora(registros)
    registros = get_apenas_precos(registros)

    for dia in registros:
        for i in range(len(dia) - janela_size - 1):
            montar_linha_treinamento(dia[i:i + janela_size + 1])



criar_treinamento(20)



''' verificacao se existe um intervalo muito grande entre uma cotacao e outra
for registro in registros:
    for x, y in zip(registro[1:], registro):
        if (milis2data(x[0]) - milis2data(y[0])).seconds > 360:
            print("{} - {}  =  {}".format(milis2data(x[0]), milis2data(y[0]), milis2data(x[0]) - milis2data(y[0])))
'''