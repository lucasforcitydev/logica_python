# funcoes.py

def saudacao(nome):
    return f"Olá, {nome}!"

def soma_lista(lista):
    total = 0
    for numero in lista:
        total += numero
    return total

def numeros_pares(n):
    pares = []
    for i in range(1, n+1):
        if i % 2 == 0:
            pares.append(i)
    return pares
