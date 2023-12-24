def precedence(operator):
    precedence_map = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    return precedence_map.get(operator, 0)

def infix_to_postfix(expression):
    output = []
    operators = []
    i = 0

    while i < len(expression):
        print(output)
        print(operators)
        if expression[i].isdigit():
            j = i
            while j < len(expression) and (expression[j].isdigit() or expression[j] == '.'):
                j += 1
            output.append(expression[i:j])
            i = j
        elif expression[i] in "+-*/^":

            while operators and precedence(operators[-1]) >= precedence(expression[i]):
                output.append(operators.pop())
            operators.append(expression[i])
            i += 1
        elif expression[i] == '(':
            operators.append(expression[i])
            i += 1
        elif expression[i] == ')':
            while operators and operators[-1] != '(':
                output.append(operators.pop())
            operators.pop()
            i += 1
        else:
            i += 1

    while operators:
        output.append(operators.pop())

    return ' '.join(output)

# Exemplo de uso
infix_expression = "1235+531*(42123*5-21)+0821"
postfix_expression = infix_to_postfix(infix_expression)
print("Expressão infixa:", infix_expression)
print("Expressão posfixa:", postfix_expression)
