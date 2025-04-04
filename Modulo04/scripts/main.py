"""
Programa principal
Autor: Amanda Nascimento
Version: 2025-04-03
"""
import funcoes
from click import clear # importando somente a função clear
clear() # limpa o console
#funcoes.cabecalho(colunas=50,titulo="Bem vindo!")
#funcoes.cabecalho(titulo="Bem vindo!",50) # se eu nomeio um argumento, tenho que nomear todos, senão dá erro
funcoes.cabecalho("Olá turma, boa noite!",30)
funcoes.cabecalho()
funcoes.cabecalho(colunas=15)

print("Fatorial de 5 =",funcoes.fatorial(5))
print("Fatorial de 5 =",funcoes.fatorial_rec(5)) #esse tem limite de encadeamento, se colocar 1000 por exemplo não irá funcionar
