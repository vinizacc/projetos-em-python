escrito = "Parabéns"
print(escrito[1:3])
print(escrito[2:])
print(escrito[:3])

Lista = [ 1, True, 9.3, [1,2,3,], (3, "j")]
print(Lista[0])
print(Lista[4])
print(Lista[3][1])

#alterar valor de uma lista
Lista[2] = 10

#funções comuns para manipulacao de listas
ListaInteiros = [1,2,3,4,5,6,7,8,9,10]
print(len(Lista)) 
print(min(ListaInteiros)) 
print(max(ListaInteiros)) 
print(sum(ListaInteiros)) 
print(Lista.append(5)) 
print(Lista.extend([6,7,8]))

del Lista[0]
print(Lista)

print(3 in Lista) #verifica se o valor 3 está na lista

print(sorted(ListaInteiros)) 

ListaInteiros.reverse()
print(ListaInteiros)

# Operação com listas 

a = [1,2,3]
b = [4,5,6]
c = a + b
print(c)

L = [ 1, 4]
R = L * 4 
print(R)

# Fateando listas
# A função range() define um intervalo de valores inteiros.
#  Associada a list(), cria uma lista com os valores do intervalo.
# A função range() pode ter de 1 a 3 parâmetros: 
# - range(n) > gera um intervalo de 0 a n-1 
# - range(i , n) > gera um intervalo de i a n-1 
# - range(i , n, p) > gera um intervalo de i a n-1 com intervalo p entre os números 

L1 = list(range(5))
print(L1)
# [0, 1, 2, 3, 4]
L2 = list(range(3, 8))
print(L2)
# [3, 4, 5, 6, 7]
L3 = list(range(2,11,3)) #indice inicial, indice final, passo
print(L3) 
# [2, 5, 8]

