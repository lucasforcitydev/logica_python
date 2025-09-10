# Exercício: Jogo de Adivinhação de Número
   #Descrição:
# Você vai criar um programa que:
# O computador escolhe um número aleatório entre 1 e 50.
# O usuário tenta adivinhar esse número.
# A cada tentativa, o programa deve informar se o palpite é maior ou menor que o número escolhido.
# O jogo continua até o usuário acertar o número.
# No final, o programa mostra:
# Quantas tentativas o usuário levou para acertar.



import random

numaleatorio = random.randint(1, 50)
tentativas = 0

print("\n====== TENTE ADIVINHAR O NUMERO ENTRE 1 E 50 ======\n ")
while True:
    try:
        numdigitado = int(input("DIGITE SEU PALPITE: "))
        
    except ValueError:
        print("Digite um numero valido!")
        continue
    
    if numdigitado < 1 or numdigitado > 50:
        print ("Numero invalido, digite um numero entre 1 e 50!")
        continue
    
    tentativas += 1
    
    if numdigitado > numaleatorio:
        print("MENOS")
    elif numdigitado < numaleatorio:
        print("MAIS")
    else:
        print("VOCÊ ACERTO!!!!!!\n PARABENS!!!!!!")
        break

print(f"Você tentou {tentativas} vezes!")



