import re

class Pilha:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

def TraduzPosFixa(exp):
    pilha_operadores = Pilha()
    lista_exp_pos_fixa = []
    operadores = {'+': 1, '-': 1, '*': 2, '/': 2, '%': 2, '**': 3, '//': 2}
    unarios = {'+': 'unario+', '-': 'unario-'}

    tokens = re.findall(r"(\b\d*[\.]?\d+\b|[\(\)\+\*\-\/\%])", exp)

    for token in tokens:
        if token.isnumeric() or (token[0] == '-' and len(token) > 1 and token[1:].isnumeric()):
            # Token é um número ou número negativo
            lista_exp_pos_fixa.append(float(token))
        elif token in operadores:
            # Token é um operador
            while (not pilha_operadores.is_empty() and
                   pilha_operadores.peek() in operadores and
                   (operadores[token] <= operadores[pilha_operadores.peek()] or
                    (token in unarios and unarios[token] == 'unario-' and pilha_operadores.peek() == '**'))):
                lista_exp_pos_fixa.append(pilha_operadores.pop())
            pilha_operadores.push(token)
        elif token == '(':
            # Token é um parêntese esquerdo
            pilha_operadores.push(token)
        elif token == ')':
            # Token é um parêntese direito
            while (not pilha_operadores.is_empty() and pilha_operadores.peek() != '('):
                lista_exp_pos_fixa.append(pilha_operadores.pop())
            if not pilha_operadores.is_empty() and pilha_operadores.peek() == '(':
                pilha_operadores.pop()

    while not pilha_operadores.is_empty():
        lista_exp_pos_fixa.append(pilha_operadores.pop())

    return lista_exp_pos_fixa

def CalcPosFixa(listaexp):
    pilha_operandos = Pilha()

    for token in listaexp:
        if isinstance(token, float):
            # Token é um operando (número)
            pilha_operandos.push(token)
        else:
            # Token é um operador
            if token == '+':
                operand2 = pilha_operandos.pop()
                operand1 = pilha_operandos.pop()
                pilha_operandos.push(operand1 + operand2)
            elif token == '-':
                operand2 = pilha_operandos.pop()
                operand1 = pilha_operandos.pop()
                pilha_operandos.push(operand1 - operand2)
            elif token == '*':
                operand2 = pilha_operandos.pop()
                operand1 = pilha_operandos.pop()
                pilha_operandos.push(operand1 * operand2)
            elif token == '/':
                operand2 = pilha_operandos.pop()
                operand1 = pilha_operandos.pop()
                if operand2 == 0:
                    return None  # Divisão por zero
                pilha_operandos.push(operand1 / operand2)
            elif token == '%':
                operand2 = pilha_operandos.pop()
                operand1 = pilha_operandos.pop()
                pilha_operandos.push(operand1 % operand2)
            elif token == '**':
                operand2 = pilha_operandos.pop()
                operand1 = pilha_operandos.pop()
                pilha_operandos.push(operand1 ** operand2)
            elif token == '//':
                operand2 = pilha_operandos.pop()
                operand1 = pilha_operandos.pop()
                if operand2 == 0:
                    return None  # Divisão de piso por zero
                pilha_operandos.push(operand1 // operand2)

    if pilha_operandos.size() == 1:
        return pilha_operandos.pop()
    else:
        return None  # Erro de expressão

# Função principal para ler e avaliar expressões
def main():
    while True:
        exp = input(">>> ")
        if exp.lower() == 'fim':
            break
        lista_exp_pos_fixa = TraduzPosFixa(exp)
        resultado = CalcPosFixa(lista_exp_pos_fixa)
        if resultado is not None:
            print(resultado)
        else:
            print("Erro na expressão.")

if __name__ == "__main__":
    main()
