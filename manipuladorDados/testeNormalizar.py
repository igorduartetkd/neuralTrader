
file = open("indiceBovespaHistorico2000.csv", encoding="latin-1")
text = file.readlines()[1:]

registro = []

for linha in text:
    dia = linha[1:3]
    mes = linha[4:6]
    ano = linha[7:11]

    dados = linha[14:].split('"')
    ultimo = float(dados[0].replace('.', '').replace(',', '.'))
    abertura = float(dados[2].replace('.', '').replace(',', '.'))
    maxima = float(dados[4].replace('.', '').replace(',', '.'))
    minima = float(dados[6].replace('.', '').replace(',', '.'))
    if '-' is not dados[8]:
        volume = float(dados[8][:-1].replace('.', '').replace(',', '.'))
    else:
        volume = 0
    variacao = float(dados[10][:-1].replace('.', '').replace(',', '.'))

    if dados[8][-1:] == 'M':
        volume = round(volume*1000000, 2)
    elif dados[8][-1:] == 'K':
        volume = round(volume*1000, 2)

    print(dia + '/' + mes + '/'+ ano + '\t'
          + str(ultimo) + ' |\t'
          + str(abertura) + ' |\t'
          + str(maxima) + ' |\t'
          + str(minima) + ' |\t'
          + str(volume) + ' |\t'
          + str(variacao) + '%')

print(str(len(text)) + " linhas")