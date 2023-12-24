import time
from datetime import datetime
import pandas as pd
import xlwings as xw
#ordem de classificacao NOME, DATA DE NASCIMENTO, PELA IDENTIDADE (rg?) IMPORTANTE


#feito identico na aula, coloca a ordem de preferencia de sort e depois segue 
def chave_de_ordenacao(elemento):
        return (elemento[1], datetime.strptime(elemento[2], "%d/%m/%Y"), elemento[0])


def ler_arquivo(name):
    with open(name, 'r') as file:
        conteudo = file.read()
        
    TAB = [i.split(",") for i in conteudo.split("\n")[:-1]]
    return TAB
#transformado em uma lista TAB
def comparacao(a,b):
    if a == b: return print("*** Classificação correta")
    return print("*** Classificação incorreta")

#precisa de inicio e fim 
def ClassificaInserção_tim(TAB, esquerda, direita):
    
    
    for i in range(esquerda + 1, direita + 1):
        x = TAB[i]  
    
        j = i -1
        while j >= esquerda and chave_de_ordenacao(x) < chave_de_ordenacao(TAB[j]):
            TAB[j + 1] = TAB[j]
            j -= 1
    
        TAB[j + 1] = x        
        

#copiado das aulas poucas modificacao nesse sort
def classificacaoMerge_tim(array, left, m, r):
    array_length1 = m - left + 1
    array_length2 = r - m
    right_arr = []
    left_arr = []
    #substitui o loop por esse modelo 
    for i in range(0, array_length1):
        left_arr.append(array[left + i]) 
    
    for i in range(0, array_length2):
        right_arr.append(array[m + 1 + i]) 

    i = 0
    j = 0
    k = left

    while j < array_length2 and i < array_length1:
        if chave_de_ordenacao(left_arr[i]) <= chave_de_ordenacao(right_arr[j]):
            array[k] = left_arr[i]
            i += 1
        else:
            array[k] = right_arr[j]
            j += 1
        k += 1

    while i < array_length1:
        array[k] = left_arr[i]
        i += 1
        k += 1

    while j < array_length2:
        array[k] = right_arr[j]
        j += 1
        k += 1


#preciso fazer um algo de insercao exclusivo do timsort
def ClassificaInserção(TAB):
    start = time.time()
    n = len(TAB)
    
    for i in range(1, n):
        x = TAB[i]  
    
        j = i - 1
        while j >= 0 and (
            x[1].lower() < TAB[j][1].lower() or #int(x[0]) < int(TAB[j][0])
            (x[1].lower() == TAB[j][1].lower() and datetime.strptime(x[2], "%d/%m/%Y") < datetime.strptime(TAB[j][2], "%d/%m/%Y")) or #datetime.strptime(x[2], "%d/%m/%Y") < datetime.strptime(TAB[j][2], "%d/%m/%Y"
            #precisei inverter é nome depois idade e por fim id 
            (x[1].lower() == TAB[j][1].lower() and datetime.strptime(x[2], "%d/%m/%Y") == datetime.strptime(TAB[j][2], "%d/%m/%Y") and int(x[0]) < int(TAB[j][0]))
        ):
            TAB[j + 1] = TAB[j]
            j = j - 1
        
        TAB[j + 1] = x

    print("Tempo de classificação Inserção = ",time.time() - start)
    

def ClassificaQuick(TAB):
    start = time.time()
    pilha = [(0, len(TAB) - 1)]
    
    while pilha:
        inicio, fim = pilha.pop()

        if inicio < fim:
            pivot = TAB[fim]
            i = inicio - 1

            for j in range(inicio, fim):
                if chave_de_ordenacao(TAB[j]) <= chave_de_ordenacao(pivot):
                    i += 1
                    TAB[i], TAB[j] = TAB[j], TAB[i]

            TAB[i + 1], TAB[fim] = TAB[fim], TAB[i + 1]
            local_pivot = i + 1

            pilha.append((inicio, local_pivot - 1))
            pilha.append((local_pivot + 1, fim))
    print("Tempo de classificação Quick = ",time.time() - start)

def find_minrun(n):
    MINIMUM = 32
    r = 0
    while n >= MINIMUM:
        r |= n & 1
        n >>= 1
    return n + r # é o tamanho do bloco

def ClassificaTIM(TAB):
    start = time.time()
    #precisa de um algoritmo de insercao de um merge 
    #feito os algo
    
    n = len(TAB)
    min_run = find_minrun(n)

    for i in range(0, n, min_run):
        ClassificaInserção_tim(TAB, i, min((i + min_run - 1), n - 1))

    size = min_run
    while size < n:
        for left in range(0, n, size * 2):
            mid = left + size - 1
            right = min((left + size * 2 - 1), (n - 1))

            if mid < right:
                classificacaoMerge_tim(TAB, left, mid, right)

        size *= 2
    print("Tempo de classificação TIM = ",time.time() - start)

def ClassificaSort(TAB):
    start = time.time()

    TAB.sort(key=chave_de_ordenacao)
    
    print("Tempo de classificação sort() = ",time.time() - start)


#func_sort = [ClassificaSort, ClassificaInserção,ClassificaQuick,ClassificaTIM,]
x = 0
while True:
    
    name = str(input("Nome do arquivo de origem: "))
    print()
    
    if name == "fim":
        break
    if x == 15:
        break

    try:
        TAB = ler_arquivo(name)
        
        #feito a copia
        TABS = TAB[:] #comprar para o sort
        ClassificaSort(TABS)
        print()
        
        #todos usando uma copia TABX de tab e fazendo a comparação
        TABX = TAB[:]
        ClassificaInserção(TABX)
        
        comparacao(TABS,TABX)
        print()

        #METODO QUICK 
        TABX = TAB[:]
        ClassificaQuick(TABX)
        comparacao(TABS,TABX)
        print()
        
        #CLASSIFICACAO TIM MAIS COMPARACAO
        TABX = TAB[:]
        ClassificaTIM(TABX)
        comparacao(TABS,TABX)
        
        print()
            
    except Exception as e:
        print(e)
        print('arquivo não localizado tente outro nome ')
    