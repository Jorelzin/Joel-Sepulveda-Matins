##Joel Sepulveda Martins## Tem que alterar as entradas  line 81
##nao deixar espaço no final das linhas do arquivo txt, para nao dar erro
##OS ARQUIVOS DE ENTRADA .TXT CRIADOS PELO PROFESSOR DEVEM SEGUIR A MESMA ESTRUTURA DE ESCRITA QUE OS QUE PASSADOS PELO MESMO NO TRABALHO PARA QUE FUNCIONE, ESPAÇOS VIRGULAS E ETC, IGUAL
###Enunciado
'''Para  obter  os  pontos  relativos  a  este  trabalho,  você  deverá  criar  um  programa,  utilizando  a
linguagem  Python, C, ou C++.  Este  programa,  quando  executado,  irá  apresentar  os  resultados  de
operações que serão realizadas entre dois conjuntos de dados.
O  programa  que  você  desenvolverá  irá  receber  como  entrada um arquivo de texto  (.txt)
contendo vários conjuntos de dados e várias operações. Estas operações e dados estarão representadas
em um arquivo de textos contendo apenas os dados referentes as operações que devem ser realizadas
segundo a seguinte regra fixa: a primeira linha do arquivo de texto de entrada conterá o número de
operações  que  estão  descritas  no  arquivo,  este  número  de  operações  será  um  inteiro;  as  linhas
seguintes  seguirão  sempre  o  mesmo  padrão  de  três  linhas:  a  primeira  linha  apresenta  o  código  da
operação  (U para união, I para interseção, D para diferença e C produto cartesiano),  a  segunda  e
terceira linhas conterão os elementos dos conjuntos separados por virgulas. A seguir está um exemplo
das linhas que podem existir em um arquivo de testes para o programa que você irá desenvolver:
4
U
3, 5, 67, 7
1, 2, 3, 4
I
1, 2, 3, 4, 5
4, 5
D
1, A, C, 34
A, C, D, 23
C
3, 4, 5, 5, A, B, R
1, B, C, D, 1
Neste exemplo temos 4 operações uma união (U), uma interseção (I), um diferença (D) e um
produto cartesiano (C). A união, definida por U, deverá ser executada sobre os conjuntos {𝟑,𝟓,𝟔𝟕,𝟕} e
{𝟏,𝟐,𝟑,𝟒}, cujos elementos estão explicitados nas linhas posteriores a definição da operção (U).
A resposta do seu programa deverá conter a operação realizada, descrita por extenso, os dados
dos conjuntos identificados, e o resultado da operação. No caso da união a linha de saída deverá conter
a informação e a formatação mostrada a seguir:
União: conjunto 1 {3,5,67,7}, conjunto 2 {1,2,3,4}. Resultado: {3,5,67,7,1,2,4}
Seu programa deverá mostrar a saída no terminal, ou em um arquivo de textos. Em qualquer
um dos casos, a saída será composta por uma linha de saída para cada operação constante no arquivo
de  textos  de  entrada  formatada  segundo  o  exemplo  de  saída  acima.  Observe  as  letras  maiúsculas  e
minúsculas, e os pontos utilizados na formatação da linha de saída apresenta acima.
No  caso  do  texto  de  exemplo,  teremos  4  linhas,  e  apenas  4  linhas  de  saída,  formatadas  e
pontuadas conforme o exemplo de saída acima. O uso de linhas extras na saída, ou erros de formatação,
implicam em perda de pontos como pode ser visto na rubrica de avaliação constante neste documento. '''
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
def printresult(resultoperation, formatlist, conjunto1, conjunto2):
    size = len(resultoperation)
    sizeconj1 = len(conjunto1)
    sizeconj2 = len(conjunto2)
    count = 0
    if formatlist == 'U':
        print('União: ', end='')
    if formatlist == 'C':
        print('Produto Cartesiano: ', end='')
    if formatlist == 'I':
        print('Intersecção: ', end='')
    if formatlist == 'D':
        print('Diferença: ', end='')
    print('Conjunto 1 {', end='')
    for p in range(0, sizeconj1):
        print(conjunto1[p].rstrip(), end='')
        if count < sizeconj1 - 1:
            print(', ', end='')
            count += 1
    print('}, ', end='')
    print('Conjunto 2 {', end='')
    count = 0
    for p in range(0, sizeconj2):
        print(conjunto2[p].rstrip(), end='')
        if count < sizeconj2 - 1:
            print(', ', end='')
            count += 1
    print('}, ', end='')
    count = 0
    if formatlist == 'U':
        print('Resultado Da União ', end='')
    if formatlist == 'C':
        print('Resultado Do Produto Cartesiano ', end='')
    if formatlist == 'I':
        print('Resultado Da Intersecção ', end='')
    if formatlist == 'D':
        print('Resultado Da Diferença ', end='')
    print('{', end='')
    for p in range(0, size):
        if formatlist == 'C':
            print('(', end='')
            for y in range(0,2):
                print(resultoperation[p][y].rstrip(), end='')
                if y == 0:
                    print(', ', end='')

            print(')', end='')
        else:
            print(resultoperation[p].rstrip(), end='')
        if count < size - 1:
            print(',', end=' ')
        count += 1
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
                conjunto1 = list[count + 1].split(', ')
                conjunto2 = list[count + 2].split(', ')
                resultoperation = union(count, list)
                resultoperation = printresult(resultoperation, formatlist, conjunto1, conjunto2)
                print(' ')
            if formatlist == 'I':
                conjunto1 = list[count + 1].split(', ')
                conjunto2 = list[count + 2].split(', ')
                resultoperation = intersection(count, list)
                resultoperation = printresult(resultoperation, formatlist, conjunto1, conjunto2)
                print(' ')

            if formatlist == 'D':
                conjunto1 = list[count + 1].split(', ')
                conjunto2 = list[count + 2].split(', ')
                resultoperation = difference(count, list)
                resultoperation = printresult(resultoperation, formatlist, conjunto1, conjunto2)
                print(' ')

            if formatlist == 'C':
                conjunto1 = list[count + 1].split(', ')
                conjunto2 = list[count + 2].split(', ')
                resultoperation = cartesianproduct(count, list)
                resultoperation = printresult(resultoperation, formatlist, conjunto1, conjunto2)
                print(' ')



