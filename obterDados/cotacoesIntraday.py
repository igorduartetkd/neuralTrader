#!/usr/bin/env python

from datetime import datetime
from json import loads
import re

from requests import get

base = 'http://cotacoes.economia.uol.com.br/ws/asset'
intraday = base + '/{asset}/intraday?size=400&callback=uolfinancecallback0'


def buscar_ativos():
    print("Buscando ativos")
    caminho_arquivo = "ativos.txt"
    print("Abrindo arquivo {} como leitura".format(caminho_arquivo))
    arq = open(caminho_arquivo, 'r')
    indices = [i.strip() for i in arq.readlines()]
    print("+ Quantidade de papeis a buscar: {}".format(len(indices)))
    return indices


def encontrar_codigo_ativos(indices):
    global base
    print("Procurando codigos dos ativos")
    assets_bruto = base + '/stock/list?size=10000'
    assets_bruto = get(assets_bruto).content.decode()
    assets = {}
    for indice in indices:
        regex = "\"idt\":\\s*(\\d+),\\s*\"code\":\\s*\"({}[^\"]*)\"".format(indice)
        padrao = re.search(regex, assets_bruto)
        if padrao:
            assets[padrao.group(2)] = padrao.group(1)
        else:
            print("- Codigo do ativo {} nao encontrado!".format(indice))

    print("+ Quantidade de ativos encontrados com codigo: {}".format(len(assets)))
    return assets


def get_intraday(asset):
    url = intraday.format(**{'asset': asset})
    return loads(get(url).content[20:-2].decode('utf-8'))


def salvar_dados(asset, quote):
    print("Salvando dados")
    today = datetime.now().strftime('%Y%m%d')
    caminho = "intraday/{}.txt".format(asset)
    arq = open(caminho, 'a+')
    dados = ''.join(map(str, quote))
    print("+ Salvando {} dados no arquivo {}".format(len(quote), caminho))
    arq.write("{} - {}\n".format(today, dados))
    print("+ Fechando arquivo {}".format(caminho))
    arq.close()
    print("+ Arquivo {} fechado".format(caminho))


if __name__ == '__main__':
    indices = buscar_ativos()
    assets = encontrar_codigo_ativos(indices)
    for asset, code in assets.items():
        quote = get_intraday(code).get('data', {})

        if len(quote):
            salvar_dados(asset, quote)

