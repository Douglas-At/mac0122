def f(z):
    for k in range(len(z)):
        z[k] = 0
#lista é mutável se vc altera os elementos ele fica mudado
w =  [-1,-1,2,2,3]
f(w)
print(w)

def f(x,y):
    #aqui crio outros objetos
    x = -1
    y = 32
#elementos imutaveis 
#nao tem como alterar se nao receber em outra variável
a=b=5
f(a,b)
print(a,b)