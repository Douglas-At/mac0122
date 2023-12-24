
def Selecao(a):
    print(a)
    n = len(a)
    # i = 0, 1, 2, ..., n - 2
    for i in range(n - 1):
        # determina o índice do menor elemento a partir de i
        imin = i
        for j in range(i + 1, n):
            if (a[imin] > a[j]): imin = j
        # troca a posição do menor com a posição de i-ésimo
        a[i], a[imin] = a[imin], a[i]
        print(a)
        
def Bolha(a):
    x = 0
    print(a)
    n = len(a)
    # i = 1, 2, ..., n - 1
    for i in range(1, n):
        # sobe com a[i] até encontrar o lugar adequado
        j = i
        #print(i,a[j], a[j - 1])
        while j > 0 and a[j] < a[j - 1]:
        
        # troca com o seu vizinho
            
            a[j], a[j - 1] = a[j - 1], a[j]
            x +=1
            # continua subindo
            j = j - 1
            print(a)
    print('numero de passos = ',x)

def insercao(a):
    n = len(a)
    # todos a partir do segundo elemento
    for i in range(1, n):
        x = a[i] # guarda a[i]
        # desloca todos os necessários para
        # liberar um lugar para a[i]
        j = i - 1
        while j >= 0 and a[j] > x:
            a[j + 1] = a[j]
            j = j - 1
            # a posição j + 1 ficou livre para receber a[i]
        a[j + 1] = x

def particiona(lista, inicio, fim):
    print(lista)
    i, j = inicio, fim
    pivo = lista[fim] # último elemento
    while True:
        # Aumentado i
        while i < j and lista[i] <= pivo: i = i + 1
        if i < j:
            lista[i], lista[j] = pivo, lista[i]
            print(lista)
            # lista[j] é maior que o pivô – avança 1
            j = j - 1
        else: break
        # Diminuindo j
        while i < j and lista[j] >= pivo: j = j - 1
        if i < j:
            lista[i], lista[j] = lista[j], pivo
            print(lista)
            # lista [i] é maior que o pivô – avança 1
            i = i + 1
        else: break

    return i      

def BoyerMoore1(a, b):
    m, n = len(a), len(b)
    conta = 0
    # tabela de últimas ocorrências de cada caractere em a
    ult = [-1] * 256
    # varrer a e definir as últimas ocorrências de cada caractere
    for k in range(m): ult[ord(a[k])] = k
    # procura a em b – i e j da direita para a esquerda
    k = m - 1

    while k < n:
        j, i = k, m - 1
        while i >= 0:
            if a[i] != b[j]: break
            j, i = j - 1, i - 1
        # comparação chegou ao fim
        if i < 0: conta += 1
        # caso particular - se k é n-1 (último de b)
        # então k+1 é índice inválido
        # o if abaixo evita esse caso
        if k + 1 >= n: break
        # desloca baseado no valor de b[k+1]
        k = k + m - ult[ord(b[k+1])]    
    return conta

print(BoyerMoore1("abcd","abacacbabcdcdabd"))

lista = [1,0,7,4,8,0,4]

carlos =[1,1,8,0,6,3,5]
teste = [8,4,7,3,6,2,9]
#Selecao(lista)
#print(lista)
particiona(lista,0,6)
print(lista)