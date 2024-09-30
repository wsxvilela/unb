
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def interpretar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidade"

def main():
    print("Calculadora de IMC")
    
    try:
        peso = float(input("Digite seu peso em kg: "))
        altura = float(input("Digite sua altura em metros: "))
        
        if peso <= 0 or altura <= 0:
            print("Peso e altura devem ser positivos.")
            return
        
        imc = calcular_imc(peso, altura)
        resultado = interpretar_imc(imc)
        
        print(f"\nSeu IMC é: {imc:.2f}")
        print(f"Classificação: {resultado}")
    
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")

if __name__ == "__main__":
    main()
