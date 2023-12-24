class Produto:
 '''Define a classe Produto.'''
 # Construtor da classe Produto
 def __init__(self, nome, codigo, preco, quantidade):
    '''Cria uma instância de Produto.'''
    self._nome = nome
    self._codigo = codigo
    self._preco = preco
    self._quantidade = quantidade
 # Retorna com o nome do produto
 def obtem_nome(self):
    return self._nome
 # Retorna com o código do produto
 def obtem_codigo(self):
    return self._codigo
 
 # Retorna com o preço corrente do produto
 def obtem_preco(self):
    return self._preco
 
 # Devolve True se novo preço maior que o anterior
 def altera_preco(self, novo_preco):
    pp = self._preco
    self._preco = novo_preco
    if novo_preco > pp: return True
    return False
 # Devolve False se a quantidade de produtos requerida não está disponível
 def altera_quantidade(self, novo_pedido):
    if novo_pedido > self._quantidade: return False
    self._quantidade -= novo_pedido
    return True
# testes da classe

p1 = Produto("Camisa Social", 123456, 45.56, 1000)
p2 = Produto("Calça Jeans", 423564, 98.12, 500)
print("Oferta do dia:", p1.obtem_nome())
print("Oferta da semana:", p2.obtem_nome())
# altera o preço
if p1.altera_preco(40.00): print("Preço alterado hoje")
else: print("Atenção - baixou o preço")
# verifica se pode fazer uma venda
if p2.altera_quantidade(100):
    print("Pode fazer a venda - valor total = ", p2.obtem_preco() * 100)
else: print("Não tem produto suficiente para esta venda")

