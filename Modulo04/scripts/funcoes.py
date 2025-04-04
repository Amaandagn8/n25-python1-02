"""
Arquivo que conterá funções úteis ao sistema
Autor: Amanda Nascimento
Version: 2025-04-03
"""
def cabecalho(titulo="Olá mundo!",colunas=60): #segundo argumento é opcional, se não colocar nada vem como 60, mas o usuário pode informar outro número também
    # colunas = 60
    espacos = (colunas-len(titulo))//2 #centralizando o título
    texto = " " * espacos + titulo + " " * espacos
    print(texto)

def fatorial(valor):
    ret=1
    for i in range(valor,1,-1): #o laço vai do valor que eu informar até o 1, e descrescendo. Ex: 3! = 3*2*1
        ret *= i
    return ret # retorna o valor

def fatorial_rec(valor): #fatorial usando recursividade
    if valor == 1: return 1
    return valor * fatorial_rec(valor - 1)


if __name__ == "__main__": # só executa quando chamar o funcoes.py, ou seja, não vai executar esse teste quando eu importar a função em outro código
    cabecalho("Olá turma!",20)

