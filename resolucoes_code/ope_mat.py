# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.
num1 = float(input("Insira o primeiro número: "))
num2 = float(input("Insira o segundo número: "))

operacao = input("Insira a Operação que deseja realizar ( +, -, *, /): ")

if operacao == '+':
    resposta = num1 + num2
    print(f"A soma de {num1} com {num2} é de : {resposta}")
elif operacao == '-':
    resposta = abs(num1 - num2)
    print(f"A subtração de {num1} com {num2} é de : {resposta}")
elif operacao == '*':
    resposta = num1 * num2
    print(f"A multiplicação de {num1} com {num2} é de : {resposta}")
elif operacao == '/':
    resposta = num1 / num2
    print(f"A Divisão de {num1} com {num2} é de : {resposta}")
else:
    print("Operação Inválida!")


if resposta % 2 == 0:
    print("Este número é par.")
else:
    print("Este número é ímpar")