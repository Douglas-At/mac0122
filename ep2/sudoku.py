#primeira coisa que vou fazer é ver se o sudoku que recebi é bm ou n
#se sim vou salvar como txt
import time
def LeiaMatrizLocal(NomeArquivo):
    # retorna a matriz lida ou [] se houver algum erro
    # abrir o arquivo para leitura
    try:
        arq = open(NomeArquivo, "r")
    except:
        print("O jogo {} não esta correto".format(NomeArquivo.split(".")[0]))
        return [] # retorna lista vazia se deu erro
    # inicia matriz Sudoku a ser lida: 9 linhas x 9 colunas
    
    # ler cada uma das linhas do arquivo
    matriz =[]
    for linha in arq.read().split("\n"):
        v = linha.split()
        linha_sudoku = []
        if len(v) !=9:
            print("O jogo {} não esta correto".format(NomeArquivo.split(".")[0]))
            return []
        for i in v:
            #verificar se realmente é numero
            try:
                valor = int(i)
            except:
                print("O jogo {} não esta correto".format(NomeArquivo.split(".")[0]))
                return []

            #verificar se o numero é valido sudoku
            if valor < 0 or valor > 9:
                print("O jogo {} não esta correto".format(NomeArquivo.split(".")[0]))
                return []
            #colocar o valor na linha
            
            linha_sudoku.append(valor)        
        matriz.append(linha_sudoku)
    #fazer uma verificação de valores únicos por linha 
    ###JA VOU TER QUE FAZER ISSO PARA O JOGO FINAL SO ADAPTAR PARA ESSE 
    arq.close()
    #teste se a matriz lida ja veio com problema
    if TestaMatrizLida(matriz):
        return matriz
    else:
        print("O jogo {} não esta correto".format(NomeArquivo.split(".")[0]))
        return []
    

def Sudoku(Mat, Lin, Col):
    global erro, contador
    erro = False
    
    #encontrar o zero 

    if Mat[Lin][Col] == 0:
        #verificar os numeros que posso colcoar aqui 
        x = DefineCandidatos(Mat,Lin,Col)
        if x == []:
            return erro
        for i in x:
            Mat[Lin][Col] = i
            if Col != 8:
                
                Sudoku(Mat,Lin,Col+1)
            else:
                if Lin != 8:
                    
                    Sudoku(Mat,Lin+1,0)

        if not erro:
            Mat[Lin][Col] = 0
        
        #baseado no digito fornecido PREENCHE se der nada 
        
    else:
        if Col != 8:
            
            Sudoku(Mat,Lin,Col+1)
        else:
            if Lin != 8:
            
                Sudoku(Mat,Lin+1,0)
            else:
                #TestaMatrizPreenchida(Mat)
                if TestaMatrizPreenchida(Mat):
                    contador += 1
                    print("* * * Matriz Completa - Solução {}".format(contador))
                    print()
                    ImprimaMatriz(Mat)
                    print()
                    print("* * * Matriz Completa e Consistente")
                    print()
                    return False
                else:
                    return False
                
    return erro

    #preciso de metodo de achar a ultima etapa e refazer dela 


def DefineCandidatos(Mat, L,C):
    candidatos = list(range(1, 10))

    #ver a linha e coluna e tirar ele mesmo
    for i in range(9):
        #achoq da para juntar os 2 ifs com or
        if Mat[L][i] in candidatos:
            #
            candidatos.remove(Mat[L][i])
        if Mat[i][C] in candidatos:
            candidatos.remove(Mat[i][C])
    linha_inicial = (L // 3) * 3
    coluna_inicial = (C // 3) * 3
    for i in range(3):
        for j in range(3):
            if Mat[linha_inicial + i][coluna_inicial + j] in candidatos:
                candidatos.remove(Mat[linha_inicial + i][coluna_inicial + j])
  
    return candidatos


def ImprimaMatriz(Mat):
    for i in range(9):
        for j in range(9):
            print(Mat[i][j], end=" ")
        print()


def TestaMatrizPreenchida(Mat):
    #metodo de verificar é saber seo numero já foi registrado em um set
    def duplicado(lista):
        armazenamento = set()
        for numero in lista:
            if numero in armazenamento:
                return True
            armazenamento.add(numero)
        return False
    
    for linha in Mat:
        if duplicado(linha):
            return False

    for i in range(0,9):
        col = [Mat[j][i] for j in range(0,9)]
        if duplicado(col):
            return False
        
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            quadrado = [Mat[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if duplicado(quadrado):
                return False
    return True

def TestaMatrizLida(Mat):
    #metodo de verificar é saber seo numero já foi registrado em um set
    def duplicado(lista):
        armazenamento = set()
        for numero in lista:
            if numero != 0:
                if numero in armazenamento:
                    return True
                armazenamento.add(numero)

        return False
    
    for linha in Mat:
        if duplicado(linha):
            return False

    for i in range(0,9):
        col = [Mat[j][i] for j in range(0,9)]
        if duplicado(col):
            return False
        
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            quadrado = [Mat[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if duplicado(quadrado):
                return False
    return True


'''for i in range(0,20):
    Mat = LeiaMatrizLocal(f"sudoku{i}.txt")
    if Mat != []:
        print(i)
    #teste para saber os validos e ver as respsotas
quit()'''

while True:
    nome_arquivo = input("Entre com o nome do arquivo:")
    Mat = LeiaMatrizLocal(nome_arquivo)
    start = time.time()
    if Mat != []:
        contador = 0
        print("* * * Matriz incial * * *")
        ImprimaMatriz(Mat)
        Sudoku(Mat,0,0)
        print("* * * - Tempo decorrido = ", time.time()-start," segundos")


