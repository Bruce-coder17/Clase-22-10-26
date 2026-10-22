def restar(a, b):
    return a - b

def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero."
    return a / b

# Implementar la función de suma
def sumar(a, b):
    pass 

# Implementar la función de multiplicación
def multiplicar(a, b):
    pass

def mostrar_menu():
    print("--- Calculadora  ---")
    print("1. Restar")
    print("2. Dividir")
    print("3. Sumar")
    print("4. Multiplicar")
    print("5. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-5): ")

        if opcion == '5':
            print("Cerrando la calculadora...")
            break

        if opcion in ['1', '2']:
            try:
                num1 = float(input("Ingresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))
            except ValueError:
                print("Error: Por favor, ingresa valores numéricos válidos.")
                continue

            if opcion == '1':
                print(f"Resultado: {num1} - {num2} = {restar(num1, num2)}")
            elif opcion == '2':
                print(f"Resultado: {num1} / {num2} = {dividir(num1, num2)}")
                
        elif opcion in ['3', '4']:
            print("Aviso: Podra utilizar esta función proximamente")
        else:
            print("Opción no válida. Intenta de nuevo.")
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