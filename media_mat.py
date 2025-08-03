#vamos calcular a média de três notas fornecidas na entrada do usuário. Uma dica é: Utilize operadores aritméticos para realizar o cálculo da média.
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

media_notas = ((n1+n2+n3)/3)

print(f"As notas são {n1}, {n2} e {n3} e a média delas é : {media_notas:.2f}")