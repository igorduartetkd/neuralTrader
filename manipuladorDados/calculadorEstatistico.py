
def normalizar(dados, xnmin=-1, xnmax=1):
    Xmin = min(dados)
    Xmax = max(dados)
    normalizado = [(xnmax - xnmin) * (x - Xmin) / (Xmax - Xmin) + xnmin for x in dados]
    return Xmin, Xmax, normalizado


def desnormalizar(xmin, xmax, normalizado, xnmin=-1, xnmax=1):
    desnormalizado = [round((x - xnmin)*(xmax - xmin)/(xnmax - xnmin) + xmin, 2) for x in normalizado]
    return desnormalizado


def media(dados):
    return sum(dados) / len(dados)
