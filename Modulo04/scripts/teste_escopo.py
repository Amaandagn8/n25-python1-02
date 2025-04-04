"""
Código para demonstrar escopo de variáveis no python
Autor: Amanda Nascimento
Version: 2025-04-03
"""
from click import clear
# Definindo uma função
def calculo():
    a = 5
    b = a + c
    # c = 30 # se descomentado dá erro porque a variável c passa a ser local
    return b
# Programa principal
c = 10 # primeiro você define a variável c e depois chama sua função
clear()
print(calculo())



