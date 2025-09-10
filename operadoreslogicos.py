"""Exercício: Sistema de Acesso a uma Festa

      Descrição:
Você vai criar um programa que determina se uma pessoa pode entrar em uma festa com base em algumas regras:
Pergunte ao usuário:
Idade (número inteiro)
Está acompanhado de um responsável? (sim/não)
Tem convite? (sim/não)
         As regras de entrada são:
A pessoa entra se tiver convite, ou se for maior de 18 anos.
Menores de 18 só entram se estiverem acompanhados de um responsável e tiverem convite.
Pessoas sem convite e menores de 18 não entram.
         O programa deve imprimir:
"Pode entrar" ou "Não pode entrar"""


idade = int(input("Digite a idade: "))

resposta1 = input("Está acompanhado de um responsável? (sim/não): ").strip().lower()
acompanhado = True if resposta1 == "sim" else False

resposta2 = input("Está com convite? (sim/não): ").strip().lower()
tem_convite = True if resposta2 == "sim" else False

if (idade >= 18 and tem_convite) or (idade < 18 and acompanhado and tem_convite):
    print("Pode entrar na festa")
else:
    print("Não pode entrar")
