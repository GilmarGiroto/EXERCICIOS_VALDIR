#Exercício 4 - Zé Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (30 quilos) deve pagar uma multa de R$ 3,00 por quilo excedente. Zé precisa que você faça um algoritmo que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que Zé deverá pagar. Imprima os dados do algoritmo com as mensagens adequadas.

limite_peso = 30.0
peso_peixes = float(input("Quantos quilos de peixe Zé Papo-de-Pescador trouxe hoje? "))
if peso_peixes > limite_peso:
    excesso = peso_peixes - limite_peso
    multa = excesso * 3.0
else:
    excesso = 0.0
    multa = 0.0
print("Zé Papo-de-Pescador trouxe", peso_peixes, "quilos de peixe hoje.")

if excesso > 0.0:
    print("Ele excedeu o limite em", excesso, "quilos e terá que pagar uma multa de R$", multa)
else:
    print("Ele não excedeu o limite de peso permitido.")
