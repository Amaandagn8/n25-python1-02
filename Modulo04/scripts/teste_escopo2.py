"""
Progrma de teste de escopo de variáveis - 2
Autor: Amanda Nascimento
Version: 2025-04-03
"""
from click import clear
def calculo():
    global c, d #aqui você diz que vai considerar o c do programa principal
    a = 5
    b = a + c
    c = 30
    d = 50
    return b
# Programa principal
c = 10
clear()
print(calculo())
print("Valor de c = ",c,"Valor de d = ",d)

#não é recomendado utilizar variáveis globais, pois pode ficar muito difícil de gerenciar