##Joel Sepulveda Martins## Tem que alterar as entradas 81
##nao deixar espaço no final das linhas do arquivo txt, para nao dar erro
##OS ARQUIVOS DE ENTRADA .TXT CRIADOS PELO PROFESSOR DEVEM SEGUIR A MESMA ESTRUTURA DE ESCRITA QUE OS QUE PASSADOS PELO MESMO NO TRABALHO PARA QUE FUNCIONE, ESPAÇOS VIRGULAS E ETC, IGUAL
def union(count, list):
    conjunto1 = list[count + 1].split(', ')
    conjunto2 = list[count + 2].split(', ')
    allconj = conjunto1 + conjunto2
    conjuntouniao = []
    for p in allconj:
        c = p in conjuntouniao
        if c == True:
            z = 0
        else:
            conjuntouniao.append(p)
    return conjuntouniao

def intersection(count, list):
    conjunto1 = list[count + 1].split(', ')
    conjunto2 = list[count + 2].split(', ')
    conjuntointer = []
    for p in conjunto1:
        c = p in conjunto2
        if c == True:
            conjuntointer.append(p)
    return conjuntointer

def difference(count, list):
    conjunto1 = list[count + 1].split(', ')
    conjunto2 = list[count + 2].split(', ')
    conjuntodiferen = []
    for p in conjunto1:
        c = p not in conjunto2
        if c == True:
            conjuntodiferen.append(p)
    return conjuntodiferen
def cartesianproduct(count, list):
    conjunto1 = list[count + 1].split(', ')
    conjunto2 = list[count + 2].split(', ')
    result = []
    tamconj1 = len(conjunto1)
    tamconj2 = len(conjunto2)
    for i in range(tamconj1 * tamconj2):
        result.append([])
    count = 0
    for p in conjunto1:
        for c in conjunto2:
            result[count].append(p)
            result[count].append(c)
            count += 1
    tam = len(result)
    resultformat = []
    for i in range(0, tamconj1 * tamconj2):
        resultformat.append(result[i])
    return result
def readandinteract():
    lines = []
    for i in (operacoes):
        i.split(' \n')
        lines.append(i)
    return lines
def printresult(resultoperation, formatlist):
    size = len(resultoperation)
    if formatlist != 'C':
        print('{', end='')
    count = 0
    for p in range(0, size):
        if formatlist == 'C':
            print('{', end='')
            for y in range(0,2):
                print(resultoperation[p][y].rstrip(), end='')
                if y == 0:
                    print(', ', end='')

            print('}', end='')
        else:
            print(resultoperation[p].rstrip(), end='')
        if count < size - 1:
            print(',', end=' ')
        count += 1
    if formatlist != 'C':
        print('}', end=' ')
    return resultoperation
with open('operations.txt', 'r') as operacoes:##entrada do arquivo de texto, arquivos possiveis: (operations, operations2, operations3, operations4)
    list = readandinteract()
    count = 0
    numberlines = int(list[0]) * 3
    while numberlines > count:
        count += 1
        formatlist = list[count].rstrip()
        if formatlist == 'U' or formatlist == 'I' or formatlist == 'D' or formatlist == 'C':
            if formatlist == 'U':
                resultoperation = union(count, list)
                print('Resultado Da União')
                resultoperation = printresult(resultoperation, formatlist)
                print(' ')
                print('==' * 60)
            if formatlist == 'I':
                print('Resultado Da Intersecção')
                resultoperation = intersection(count, list)
                resultoperation = printresult(resultoperation, formatlist)
                print(' ')
                print('==' * 60)
            if formatlist == 'D':
                print('Resultado Da Diferença')
                resultoperation = difference(count, list)
                resultoperation = printresult(resultoperation, formatlist)
                print(' ')
                print('=='*60)
            if formatlist == 'C':
                print('Resultado Do Produto Cartesiano')
                resultoperation = cartesianproduct(count, list)
                resultoperation = printresult(resultoperation, formatlist)
                print(' ')
                print('==' * 60)


