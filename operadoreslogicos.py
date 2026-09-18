


idade = int(input("Digite a idade: "))

resposta1 = input("Está acompanhado de um responsável? (sim/não): ").strip().lower()
acompanhado = True if resposta1 == "sim" else False

resposta2 = input("Está com convite? (sim/não): ").strip().lower()
tem_convite = True if resposta2 == "sim" else False

if (idade >= 18 and tem_convite) or (idade < 18 and acompanhado and tem_convite):
    print("Pode entrar na festa")
else:
    print("Não pode entrar")
