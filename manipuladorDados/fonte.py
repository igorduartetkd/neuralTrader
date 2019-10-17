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

    registros = {}

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
        print("Data coleta: {}".format(dataConsulta))
        for atributo, valor in dados.items():
            print("Dia: {} cotacoes encontradas: {}".format(datetime.datetime.fromtimestamp(valor[0]["date"]/1000.0),
                                                             len(valor)))
            cotacoes = {}
            for cotacao in valor:
                cotacoes[cotacao["date"]] = cotacao["price"]

            registros[valor[0]["date"]] = cotacoes
    print("Cotacoes de {} dias carregados".format(len(registros)))
    return registros

getRegistrosSeparados("PETR4.SA")