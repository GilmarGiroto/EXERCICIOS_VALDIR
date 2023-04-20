#Exercício 3 - Crie um algoritmo que receba a altura e o peso de uma pessoa e mostre seu Índice de Massa Corporal (IMC)

altura = float(input("Qual é a sua altura em metros? "))
peso = float(input("Qual é o seu peso em quilogramas? "))
imc = peso / altura ** 2
print("Seu IMC é:", imc)