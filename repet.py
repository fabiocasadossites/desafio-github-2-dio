# Recebe um número inteiro como entrada do usuário
numero = int(input("Digite um número inteiro: "))

# Verifica se o número é par ou ímpar utilizando o operador de módulo (%)
if numero % 2 == 0:
    print("O número", numero, "é par.")
else:
    print("O número", numero, "é ímpar.")
