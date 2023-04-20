def ex1:
    return 
    m = float(input("valor em metros"))
    metros_centimetros(m)

    print("Seu valor em centimetros é", metros_centimetros, "centimetros")

def ex2:
    return 
    valor_hora = float(input("Quanto você ganha por hora? "))
    horas_trabalhadas = float(input("Quantas horas você trabalha por mês? "))
    salario_mensal = valor_hora * horas_trabalhadas
    print("Seu salário mensal é: R$", salario_mensal)

def ex3:
    return 
    altura = float(input("Qual é a sua altura em metros? "))
    peso = float(input("Qual é o seu peso em quilogramas? "))
    imc = peso / altura ** 2
    print("Seu IMC é:", imc)

def ex4:
    return 
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

def ex5:
    return 
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

def ex6:
    return 
    tamanho_area = float(input("Qual o tamanho da área a ser pintada (em metros quadrados)? "))

    litros_tinta = tamanho_area / 3
    latas_tinta = int(litros_tinta / 18) + 1
    preco_total = latas_tinta * 80

    print("Quantidade de latas de tinta: ", latas_tinta)
    print("Preço total: R$", preco_total)