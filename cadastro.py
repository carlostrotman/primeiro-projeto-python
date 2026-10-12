# Sistema Simples de Cadastro de Suporte
print("--- Cadastro de Novo Chamado ---")

# Recebendo os dados do usuário
cliente = input("Digite o nome do cliente: ")
equipamento = input("Qual o equipamento com defeito? ")
problema = input("Descreva o problema: ")

# Exibindo os dados organizados
print("\n--- Resumo do Chamado Gerado ---")
print(f"Cliente: {cliente}")
print(f"Equipamento: {equipamento}")
print(f"Status: Aguardando Suporte")
print(f"Descrição: {problema}")
print("--------------------------------")

input("\nPressione Enter para sair...")