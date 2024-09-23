
itens_sacola = []
quantidade_itens = int(input("Quantos itens você tem na sacola de compras? "))

for i in range(quantidade_itens):
    item = input(f"Digite o nome do item {i + 1}: ")
    itens_sacola.append(item)

while True:
    adicionar = input("Você gostaria de adicionar mais itens na sacola? (sim/não): ").strip().lower()
    
    if adicionar == 'sim':
        novo_item_sacola = input("Qual item você deseja adicionar? ")
        itens_sacola.append(novo_item_sacola)
    elif adicionar == 'não':
        break
    else:
        print("Resposta inválida. Por favor, digite 'sim' ou 'não'.")

print("\nItens na sacola de compras:")
for item in itens_sacola:
    print("-", item)
