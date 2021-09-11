import re


def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]


def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    i = 0
    cp = 0
    while i < 6:
        cp = cp + abs(as_a[i] - as_b[i])
        i += 1
        cp = abs(cp) / 6
    return cp 

  

def calcula_assinatura(texto):
    i = 0
    var = 0
    var_frase = 0
    soma_sentencas = 0
    soma_caracteres = 0
    soma_frases = 0
    lista_palavras = []
    lista_frases = []
    sentencas = separa_sentencas(texto)
    for sent in sentencas:
        novas_frases = separa_frases(sent)
        lista_frases.extend(novas_frases)
        for fr in novas_frases:
            novas_palavras = separa_palavras(fr)
            lista_palavras.extend(novas_palavras)
            while i < len(lista_palavras):
                palavra = str(lista_palavras[i])
                soma_caracteres = len(palavra) + soma_caracteres
                i = i + 1
    número_sentencas = len(sentencas)
    for sentenca in range(len(sentencas)):
        tamanho_sentenca = len(sentencas[var])
        var = var + 1
        soma_sentencas = soma_sentencas + tamanho_sentenca
    número_frases = len(lista_frases)
    for frase in range(len(lista_frases)):
        tamanho_frases = len(lista_frases[var_frase])
        var_frase = var_frase + 1
        soma_frases = soma_frases + tamanho_frases
    soma_palavras = len(lista_palavras)
    tamanho_médio = soma_caracteres / soma_palavras
    Type_token = n_palavras_diferentes(lista_palavras) / soma_palavras
    hapax_legomana = n_palavras_unicas(lista_palavras) / soma_palavras
    médio_sentenca = soma_sentencas / len(sentencas)
    complexidade_sentenca = len(lista_frases) / len(sentencas)
    médio_frase = soma_frases / len(lista_frases)
    return [tamanho_médio, Type_token, hapax_legomana, médio_sentenca, complexidade_sentenca, médio_frase]


def avalia_textos(textos, ass_cp):
    i = 0
    ai = False
    anterior = False
    ss = 0
    while len(textos) > i:
        texto = textos[i]
        ss = calcula_assinatura(texto)
        cp = compara_assinatura(ass_cp, ss)
        if not anterior or anterior > cp:
            anterior = cp
            ai = i
        i += 1
    return ai + 1


def main():
    textos = le_textos()
    ass_cp = le_assinatura()
    ai = avalia_textos(textos, ass_cp)
    print('O autor do texto', ai, 'está infectado com COH-PIAH')
main()
