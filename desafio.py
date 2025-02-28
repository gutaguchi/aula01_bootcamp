constante_bonus = 10000

nome_usuario = input("Digite o seu nome: ")

salario = float(input("Digite o seu salario: "))


bonus_usuario = float(input("Digite o seu bonus: "))

valor_do_bonus = constante_bonus + salario + bonus_usuario

print(f"O usuario {nome_usuario} possui o bonus de {valor_do_bonus}")

