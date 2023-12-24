import re
t = "12.35 + 5.47 * ( 2 ** 5 - 21) + 0.821"
r = re.findall(r"(\b\d*[.]?\d+\b|\*\*|[\(\)\+\*\-\/\%])", t)

#t = " ( 3 + 4.8 ) / 39"
#r = re.findall(r"(\b\d*[.]?\d+\b|\*\*|[\(\)\+\*\-\/\%])", t)



def prioridade(operador):
    prioridade = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '**': 3}
    return prioridade.get(operador, 0)

def operacao(sinal,lista):
    b = lista.pop()
    a = lista.pop()
    if sinal == '+':
        lista.append(a + b)
    elif sinal == '-':
        lista.append(a - b)
    elif sinal == '*':
        lista.append(a * b)
    elif sinal == '/':
        lista.append(a / b)
    elif sinal == '**':
        lista.append(a**b)


pos_fixa = []
operadores = []

for i,j in enumerate(r):
    if (j.isdigit())|(j.replace('.', '', 1).isdigit()):
        pos_fixa.append(j)
    elif prioridade(j) not in [0,4,5]:
        
        while operadores and prioridade(operadores[-1]) >= prioridade(j):
            pos_fixa.append(operadores.pop())
        operadores.append(j)
    elif j == "(":
        operadores.append(j)
        
    elif j == ")":
        prioridade(operadores[-1])
        while operadores and operadores[-1] != "(":
            pos_fixa.append(operadores.pop())
        operadores.pop()
        
while operadores:
        pos_fixa.append(operadores.pop())



lista_pos = ['12.35', '5.47', '2', '5', '**', '21', '-', '*', '+', '0.821', '+']
#lista_pos = ["1","2","+","3","+"]
pilha_num = []

for i,j in enumerate(lista_pos):
    print(pilha_num)
    if prioridade(j) == 0:
        if (j.isdigit()):
            j = int(j)
        elif (j.replace('.', '', 1).isdigit()):    
            j = float(j)

        pilha_num.append(j)
    else:
        operacao(j,pilha_num)     
print(pilha_num)