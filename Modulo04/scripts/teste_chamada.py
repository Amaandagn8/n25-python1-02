"""
Programa de teste de chamada com parametros no python
Autor: Amanda Nascimnento
Version: 2025-04-03
"""
from click import clear
# definindo funções
def calculo_variaveis(a, b):
    ret = a + b
    a = 15
    b = 20
    return ret
def uso_lista(lst):
    lst.append(5)
    lst.append(6)
    return len(lst)
# Programa principal
d, e = 5, 6
lista = [1,2]
# Usando as funções
clear()
print(calculo_variaveis(d,e))
print(d,e)
print("Antes: ",lista)
print(uso_lista(lista))
print("Depois: ",lista)