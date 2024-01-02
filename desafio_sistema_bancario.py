menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
Limite = 500
extrato = ""
numero_saques = 0
LIMITE_Saques = 3

while True:
	
	opcao = input(menu)
	
	if opcao == "d":
		valor = float(input("Informe o valor do dépósito: "))
		if valor > 0:
			saldo += valor
			extrato += f"Depósito: R$ {valor:.2f}\n"
		else:
			print("Operação falhou! O valor informado é inválido.")

	elif opcao == "s":
		valor = float(input("Informe o valor do saque: "))
		
		excedeu_saldo = valor > saldo
		
		excedeu_limite = valor > Limite
		
		excedeu_saques = numero_saques >= LIMITE_Saques
		
		if excedeu_saldo:
			print("Operação fahou! Você não tem saldo suficiente.")

		elif excedeu_limite:
			print("Operação fahou! O valor do saque escede o limite.")

		elif excedeu_saques:
			print("Operação fahou! Número máximo de saques excedido.")

		elif valor > 0:
			saldo -= valor
			extrato += f"Saque: R$ {valor:.2f}\n"
			numero_saques += 1
		else:
			print("Operação falhou! O valor informado é inválido.")

	elif opcao == "e":
		print("============== EXTRATO ==============")
		print("Não foram realizadas movimentações." if not extrato else extrato)
		print(f"\nSaldo: R$ {saldo:.2f}")
		print("=====================================")

	elif opcao == "q":
		break

	else:
		print("Operação inválida! Por favor, selecione novamente a operação desejada.")
