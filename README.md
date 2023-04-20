# EXERCICIOS_VALDIR

Exercício 1 - Crie um algoritmo que receba um valor em metros e converta para centímetros.

print("valor em metros")
m = int(input())

centimetros = (m * 100)

print("Seu valor em centimetros é", centimetros, "centimetros")


Exercício 2 - Crie um algoritmo que pergunte quanto você ganha por hora e o número de horas que você trabalha por mês, o algoritmo deve calcular e mostrar qual seu salário naquele mês



print("Ganho por hora")
gh = float(input())
print("Horas trabalhadas por mês")
hm = float(input())

ganho_mensal = (gh * hm)

print("Você ganha", ganho_mensal, "reais por mês")

Exercício 3 - Crie um algoritmo que receba a altura e o peso de uma pessoa e mostre seu Índice de Massa Corporal (IMC)

print("Temperatura em Fahrenheit")
temp_Fahren = int(input())

temp_Celsius = 5 * ((temp_Fahren-32) / 9)

print("São", temp_Celsius, "Graus Celsius")

Exercício 4 - Zé Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (30 quilos) deve pagar uma multa de R$ 3,00 por quilo excedente. Zé precisa que você faça um algoritmo que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que Zé deverá pagar. Imprima os dados do algoritmo com as mensagens adequadas.

print("Altura")
m = float(input())
print("Peso")
kg = float(input())

imc = m / kg **2

print("Seu Índice de Massa Corporal (IMC) é:", imc)

Exercício 5 - Crie um algoritmo que receba quanto você ganha por hora e quantas horas trabalhou no mês. O algoritmo deve calcular e mostrar o seu salário no referido mês, sabendo que serão descontados 11% do Imposto de Renda (IR) e mais 8% do INSS. No final o algoritmo deve apresentar:

Salário bruto
Valor do imposto de renda
Valor do INSS
Salário líquido

print("Digite o peso dos peixes")
kg = float(input())
limite = 30
excesso = kg - limite
multa = 3

if excesso > 0:
    multa = excesso * 3 
    print("Peso excedeu: ",  excesso, "kg") 
    print("Valor da multa: R$", multa) 
else: 
    print("Não excedeu o peso.")

Exercício 6 - Você foi contratado pela UNIMAR para ajudar na reforma dos blocos, o seu papel é apoiar e facilitar as tomadas de decisões. Você vai ajudar a otimizar os gastos para pintura, crie um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

print("Ganho por hora")
gh = float(input())
print("Horas trabalhadas por mês")
hm = float(input())

ganho_mensal = (gh * hm)
imposto_de_renda = ganho_mensal - (ganho_mensal * 11 / 100)
inss = ganho_mensal - (ganho_mensal * 8 / 100)
salario_liquido = ganho_mensal - (ganho_mensal * 11 / 100 + (ganho_mensal * 8 / 100))

print("Salário bruto: R$",ganho_mensal)
print("Valor + imposto de renda: R$",imposto_de_renda)
print("Valor + inss: R$",inss)
print("Salário líquido: R$",salario_liquido)


Exercício 7


metro_litro = 3
litro_lata = 18
preco_lata = 80

print("Digite o tamanho da área em metros quadrados: ")
area = float(input())

litros = area / metro_litro
latas = (litros / litro_lata)
preco_total = latas * preco_lata

print("Você precisa comprar", latas, "latas de tinta, totalizando R$",preco_total)
