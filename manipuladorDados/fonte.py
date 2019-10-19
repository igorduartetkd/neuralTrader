import re
import json
import datetime

def getRegistrosSeparados(nome_ativo):

    name_file_open = nome_ativo
    name_file_open_modify = "../recursos/" + name_file_open + ".txt"

    try:
        file = open(name_file_open_modify)
    except IOError:
        print('Erro ao abrir arquivo {}'.format(name_file_open_modify))
        exit(1)

    text = file.readlines()

    registros = []

    for linha in text:
        saida1 = re.search("^([^- ]*)[^{]*(.*)$", linha) # separando a data de captura dos dados
        dataConsultaBruta = saida1.group(1)
        dataConsulta = dataConsultaBruta[:4] + '-'
        dataConsulta += dataConsultaBruta[4:6] + '-'
        dataConsulta += dataConsultaBruta[6:8]
        dados = saida1.group(2)
        dados = re.sub("'", "\"", dados)
        dados = re.sub("}{", "},{", dados)
        dados = '{"itens": [' + dados + '] }'
        dados = json.loads(dados)
        #print("Data coleta: {}".format(dataConsulta))
        for atributo, valor in dados.items():
            #print("Dia: {} cotacoes encontradas: {}".format(datetime.datetime.fromtimestamp(valor[0]["date"]/1000.0),
            #                                                len(valor)))
            cotacoes = []
            for cotacao in valor:
                cotacoes.append((cotacao["date"], cotacao["price"]))

            registros.append(cotacoes)
    print("Cotacoes de {} dias carregados".format(len(registros)))
    return registros

#getRegistrosSeparados("PETR4.SA")








def remover_primeira_ultima_hora(registros):
    for dia in registros:
        data_inicio = dia[-1][0]
        data_fim = dia[0][0]
        print("Antes: {}".format(len(dia)))
        dia = [x for x in dia[::-1] if not is_primeira_ultima_hora(data_inicio, data_fim, x[0])]
        print("Depois: {}".format(len(dia)))

def is_primeira_ultima_hora(data_inicio, data_fim, data):
    data_inicio = datetime.datetime.fromtimestamp(data_inicio / 1000.0)
    data_fim = datetime.datetime.fromtimestamp(data_fim / 1000.0)
    data = datetime.datetime.fromtimestamp(data / 1000.0)
    print(data)
    if (data - data_inicio).seconds < 3600:
        return True
    if (data_fim - data).seconds < 3600:
        return True
    return False