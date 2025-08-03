#Vamos testar se uma palavra é um palíndromo?! Uma dica é: Utilize conceitos de manipulação de strings para inverter a palavra e comparar com a original.
'''
strip() → remove espaços extras no início e fim da palavra.
lower() → transforma tudo em minúsculas.
replace(" ", "") → remove todos os espaços internos.
'''

txt = input("Digite a palavra: ").strip().lower().replace(" ", "")

#inverte a palavra
txt_invertida = txt[::-1]

if txt == txt_invertida:
    print(f"A palavra {txt} é um palíndromo.")
else:
    print(f"A palavra {txt} não é um palíndromo.")