
arq_camada1 = open('primeiracamada.txt', 'r')
arq_camada2 = open('segundacamada.txt', 'r')
arq_camada3 = open('camadasaida.txt', 'r')
arq_bias1 = open('b1.txt', 'r')
arq_bias2 = open('b2.txt', 'r')

linhas = arq_camada1.readlines()
camada1 = []
for linha in linhas:
    neuronio = []
    for peso in linha.strip(' \n').split(' '):
        neuronio.append(float(peso))
    camada1.append(neuronio)

linhas = arq_camada2.readlines()
camada2 = []
for linha in linhas:
    neuronio = []
    for peso in linha.strip(' \n').split(' '):
        neuronio.append(float(peso))
    camada2.append(neuronio)

linhas = arq_camada3.readlines()
camada3 = []
for linha in linhas:
    neuronio = []
    for peso in linha.strip(' \n').split(' '):
        neuronio.append(float(peso))
    camada3.append(neuronio)

linhas = arq_bias1.readlines()
bias1 = []
for linha in linhas:
    neuronio = []
    for peso in linha.strip(' \n').split(' '):
        neuronio.append(float(peso))
    bias1.append(neuronio)

linhas = arq_bias2.readlines()
bias2 = []
for linha in linhas:
    neuronio = []
    for peso in linha.strip(' \n').split(' '):
        neuronio.append(float(peso))
    bias2.append(neuronio)

arq_saida = open('redeNeuralExtraidaMatlab.txt', 'w')
arq_saida.write(str(len(camada1)) + ' ' + str(len(camada2)) + ' ' + str(len(camada3)) + '\n')

camadas = [camada1, camada2, camada3]

for camada in camadas:
    funcoes = []
    for _ in camada:
        arq_saida.write('4 ')

    arq_saida.write('\n')

for camada in camadas:
    for neuronio in camada:
        for peso in neuronio:
            arq_saida.write(str(peso) + ' ')
        arq_saida.write('\n')

bias0 = [[0] for _ in range(len(camada1))]
biases = [bias0, bias1, bias2]

for camada in biases:
    for bias in camada:
        arq_saida.write(str(bias[0]) + ' ')
    arq_saida.write('\n')
