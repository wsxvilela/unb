def collatz_number(n):  # sourcery skip: assign-if-exp
    result = [n]  # Lista para armazenar a sequência

    while n != 1:  # A condição para parar é quando n se tornar 1
        if n % 2 == 0:  # Se n for par
            n = n // 2  # Divide n por 2
        else:  # Se n for ímpar
            n = 3 * n + 1  # Aplica 3n + 1
        result.append(n)  # Adiciona o novo valor de n à lista

    return result  # Retorna a sequência completa

# Solicita ao usuário para inserir um número
try:
    num = int(input("Digite um número inteiro para iniciar a Conjectura de Collatz: "))
    
    # Chama a função e imprime a sequência gerada
    print("Sequência da Conjectura de Collatz para", num, ":", collatz_number(num))
    
except ValueError:
    print("Por favor, insira um número inteiro válido.")
