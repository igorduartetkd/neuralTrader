file = open("indiceBovespaHistorico2000.csv", encoding="latin-1")
file_write = open("dadosSeparados2000.txt", 'w')
text = file.readlines()[1:]

registro = []

for linha in text[::-1]:
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

    file_write.write(dia + '/' + mes + '/'+ ano + ' '
          + str(ultimo) + ' '
          + str(abertura) + ' '
          + str(maxima) + ' '
          + str(minima) + ' '
          + str(volume) + ' '
          + str(variacao) + '\n')