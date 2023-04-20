#Exercício 6 - Você foi contratado pela UNIMAR para ajudar na reforma dos blocos, o seu papel é apoiar e facilitar as tomadas de decisões. Você vai ajudar a otimizar os gastos para pintura, crie um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

tamanho_area = float(input("Qual o tamanho da área a ser pintada (em metros quadrados)? "))

litros_tinta = tamanho_area / 3
latas_tinta = int(litros_tinta / 18) + 1
preco_total = latas_tinta * 80

print("Quantidade de latas de tinta: ", latas_tinta)
print("Preço total: R$", preco_total)