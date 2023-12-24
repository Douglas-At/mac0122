import re
class Pilha:
    def prioridade(self,operador):
        #grau de prioridade igual na aula de pilha 
        prioridade = {'+': 1, '-': 1, '*': 2, '/': 2,'//': 2, '^': 3, '**': 3}
        return prioridade.get(operador, 0)

    def operacao(self,sinal,lista):
        #tradtor do sinal de str 
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
        elif sinal == '//':
            lista.append(int(a / b))    
        elif sinal == '**':
            lista.append(a**b)

    def TraduzPosFixa(self,infixa):
        #uso do comando mt parecido com o dado em aula 
        lista_infixa = re.findall(r"(\b\d*[.]?\d+\b|\*\*|\/\/|[\(\)\+\*\-\/\%])", infixa)
        
        pos_fixa = []
        operadores = []
        #mesma logica dado na aula de pilha 
        for j in lista_infixa:
            if (j.isdigit())|(j.replace('.', '', 1).isdigit()):
                pos_fixa.append(j)
            elif self.prioridade(j) not in [0,4,5]:
                
                while operadores and self.prioridade(operadores[-1]) >= self.prioridade(j):
                    pos_fixa.append(operadores.pop())
                operadores.append(j)
            elif j == "(":
                operadores.append(j)
                
            elif j == ")":
                self.prioridade(operadores[-1])
                while operadores and operadores[-1] != "(":
                    pos_fixa.append(operadores.pop())
                operadores.pop()
                
        while operadores:
                pos_fixa.append(operadores.pop())
        return pos_fixa
    
    def CalcPosFixa(self, posfixa):
        pilha_num = []
        
        for i,j in enumerate(posfixa):
            #empilha tudo q é nmero
            if self.prioridade(j) == 0:
                #trata float e int
                if (j.isdigit()):
                    j = int(j)
                elif (j.replace('.', '', 1).isdigit()):    
                    j = float(j)
                pilha_num.append(j)
            # trata os sinais e faz as contas
            else:
                self.operacao(j,pilha_num)     
        return pilha_num[0]


pilhas = Pilha()
#testes
print(pilhas.CalcPosFixa(pilhas.TraduzPosFixa("12.35 + 5.47 * ( 2 ** 5 - 21) + 0.821")))
print(pilhas.CalcPosFixa(pilhas.TraduzPosFixa(" ( 3 + 9 ) // 12 ")))