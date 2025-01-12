# conversor_temperatura_mejorado.py

"""
Conversor de Unidades de Temperatura

Este programa permite convertir temperaturas entre diferentes unidades
(Celsius, Fahrenheit y Kelvin). Incorpora mejoras en modularidad,
validación y claridad de código.

Autor: [Tu Nombre]
Fecha: 11/01/2025
"""

# Constantes
CERO_ABSOLUTO_C = -273.15  # En grados Celsius
CERO_ABSOLUTO_F = -459.67  # En grados Fahrenheit
CERO_ABSOLUTO_K = 0        # En Kelvin

# Funciones de Conversión
def celsius_a_fahrenheit(temp_celsius: float) -> float:
    return (temp_celsius * 9/5) + 32

def celsius_a_kelvin(temp_celsius: float) -> float:
    return temp_celsius + 273.15

def fahrenheit_a_celsius(temp_fahrenheit: float) -> float:
    return (temp_fahrenheit - 32) * 5/9

def kelvin_a_celsius(temp_kelvin: float) -> float:
    return temp_kelvin - 273.15

# Función para Validar Temperatura
def validar_temperatura(temperatura: float, tipo: str) -> bool:
    if tipo == 'C' and temperatura < CERO_ABSOLUTO_C:
        print("Error: La temperatura en Celsius no puede ser menor al cero absoluto (-273.15°C).")
        return False
    if tipo == 'F' and temperatura < CERO_ABSOLUTO_F:
        print("Error: La temperatura en Fahrenheit no puede ser menor al cero absoluto (-459.67°F).")
        return False
    if tipo == 'K' and temperatura < CERO_ABSOLUTO_K:
        print("Error: La temperatura en Kelvin no puede ser menor a 0.")
        return False
    return True

# Función para Solicitar y Validar la Entrada del Usuario
def obtener_temperatura_valida(mensaje: str) -> float:
    while True:
        try:
            temperatura = float(input(mensaje))
            return temperatura
        except ValueError:
            print("Error: Por favor ingrese un número válido.")

# Menú Principal
def mostrar_menu() -> None:
    print("\n=== Conversor de Temperatura ===")
    print("1. Celsius a Fahrenheit")
    print("2. Celsius a Kelvin")
    print("3. Fahrenheit a Celsius")
    print("4. Kelvin a Celsius")
    print("5. Salir")

# Lógica de Opción de Conversión
def manejar_conversion(opcion: str) -> bool:
    if opcion == "1":
        temp = obtener_temperatura_valida("Ingrese temperatura en Celsius: ")
        if validar_temperatura(temp, 'C'):
            resultado = celsius_a_fahrenheit(temp)
            print(f"\n{temp:.2f}°C = {resultado:.2f}°F")
            return True

    elif opcion == "2":
        temp = obtener_temperatura_valida("Ingrese temperatura en Celsius: ")
        if validar_temperatura(temp, 'C'):
            resultado = celsius_a_kelvin(temp)
            print(f"\n{temp:.2f}°C = {resultado:.2f}K")
            return True

    elif opcion == "3":
        temp = obtener_temperatura_valida("Ingrese temperatura en Fahrenheit: ")
        if validar_temperatura(temp, 'F'):
            resultado = fahrenheit_a_celsius(temp)
            print(f"\n{temp:.2f}°F = {resultado:.2f}°C")
            return True

    elif opcion == "4":
        temp = obtener_temperatura_valida("Ingrese temperatura en Kelvin: ")
        if validar_temperatura(temp, 'K'):
            resultado = kelvin_a_celsius(temp)
            print(f"\n{temp:.2f}K = {resultado:.2f}°C")
            return True

    elif opcion == "5":
        return False

    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")
    return True

# Función Principal
def main():
    programa_activo = True
    total_conversiones = 0

    while programa_activo:
        mostrar_menu()
        opcion = input("\nSeleccione una opción (1-5): ")
        if opcion == "5":
            print(f"\nTotal de conversiones realizadas: {total_conversiones}")
            print("¡Gracias por usar el conversor de temperatura!")
            programa_activo = False
        elif manejar_conversion(opcion):
            total_conversiones += 1

# Punto de Entrada del Programa
if __name__ == "__main__":
    main()
