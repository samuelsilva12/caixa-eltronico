print("------ CAIXA ELETRONICO BANCO CHATGPT --------\n\n")
valor_saque = int(input("Digite o valor que deseja sacar: \n"))
nota100 = nota50 = nota20 = nota5 = nota1 = 0
saque = valor_saque
if valor_saque < 10 or valor_saque > 600:
    print("Valor digitado é invalido, saques disponiveis apenas de 10R$ até 600R$ (tente novamente)")
else:
    # calculo das notas
    nota100 = valor_saque//100
    valor_saque = valor_saque % 100

    nota50 = valor_saque // 50
    valor_saque = valor_saque % 50

    nota20 = valor_saque // 20
    valor_saque = valor_saque % 20

    nota5 = valor_saque // 5
    valor_saque = valor_saque % 5

    nota1 = valor_saque // 1
    valor_saque = valor_saque % 1
    
    print(f"\n Você sacou {saque}R$ \n")
if nota100 != 0:
    print(f"{nota100} Notas de 100R$\n")
if nota50 != 0:
    print(f"{nota50} Notas de 50R$\n")
if nota20 != 0:
    print(f"{nota20} Notas de 20R$\n")
if nota5 != 0:
    print(f"{nota5} Notas de 5R$\n")
if nota1 != 0:
    print(f"{nota1} Notas de 1R$\n")





