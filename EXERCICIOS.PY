#Exercício 1 - Crie um algoritmo que receba um valor em metros e converta para centímetros.

from FUNCOES import metros_centimetros

m = float(input("valor em metros"))
metros_centimetros(m)

print("Seu valor em centimetros é", metros_centimetros, "centimetros")


#Exercício 2 - Crie um algoritmo que pergunte quanto você ganha por hora e o número de horas que você trabalha por mês, o algoritmo deve calcular e mostrar qual seu salário naquele mês


valor_hora = float(input("Quanto você ganha por hora? "))
horas_trabalhadas = float(input("Quantas horas você trabalha por mês? "))
salario_mensal = valor_hora * horas_trabalhadas
print("Seu salário mensal é: R$", salario_mensal)


#Exercício 3 - Crie um algoritmo que receba a altura e o peso de uma pessoa e mostre seu Índice de Massa Corporal (IMC)

altura = float(input("Qual é a sua altura em metros? "))
peso = float(input("Qual é o seu peso em quilogramas? "))
imc = peso / altura ** 2
print("Seu IMC é:", imc)


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


#Exercício 5 - Crie um algoritmo que receba quanto você ganha por hora e quantas horas trabalhou no mês. O algoritmo deve calcular e mostrar o seu salário no referido mês, sabendo que serão descontados 11% do Imposto de Renda (IR) e mais 8% do INSS. No final o algoritmo deve apresentar:

valor_hora = float(input("Quanto você ganha por hora? "))
horas_mes = float(input("Quantas horas você trabalhou no mês? "))


salario_bruto = valor_hora * horas_mes
imposto_renda = 0.11 * salario_bruto
inss = 0.08 * salario_bruto
salario_liquido = salario_bruto - imposto_renda - inss


print("Salário bruto: R$", salario_bruto)
print("Desconto de Imposto de Renda (11%): R$", imposto_renda)
print("Desconto de INSS (8%): R$", inss)
print("Salário líquido: R$", salario_liquido)


#Exercício 6 - Você foi contratado pela UNIMAR para ajudar na reforma dos blocos, o seu papel é apoiar e facilitar as tomadas de decisões. Você vai ajudar a otimizar os gastos para pintura, crie um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

tamanho_area = float(input("Qual o tamanho da área a ser pintada (em metros quadrados)? "))

litros_tinta = tamanho_area / 3
latas_tinta = int(litros_tinta / 18) + 1
preco_total = latas_tinta * 80

print("Quantidade de latas de tinta: ", latas_tinta)
print("Preço total: R$", preco_total)


