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
