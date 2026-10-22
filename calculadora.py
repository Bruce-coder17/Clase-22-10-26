def sumar(a, b):
    return a + b

def multiplicar(a, b):
    return a * b

def main():
    print("--- CALCULADORA PRO ---")
    print("1. Sumar")
    print("2. Multiplicar")

    opcion = input("Elige una opción (1 o 2): ")

    if opcion in ('1', '2'):
        try:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))

            if opcion == '1':
                print(f"Resultado: {num1} + {num2} = {sumar(num1, num2)}")
            elif opcion == '2':
                print(f"Resultado: {num1} * {num2} = {multiplicar(num1, num2)}")
                
        except ValueError:
            print("Error: Por favor ingresa solo números válidos.")
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()