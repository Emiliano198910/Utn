"""Muestren un número en binario y desafíen al usuario a adivinar su equivalente decimal, o viceversa, reforzando la conversión entre ambos sistemas."""
import random
def decimal_a_binario(n): # Función para convertir decimal a binario
    if n == 0:
        return "0"  
    binario = ""
    while n > 0:
        binario = str(n % 2) + binario
        n //= 2 
    return binario
def binario_a_decimal(b): # Función para convertir binario a decimal
    decimal = 0
    for i, digito in enumerate(reversed(b)):
        decimal += int(digito) * (2 ** i)   
    return decimal  
def main(): # Función principal
    print("Juego de conversión entre decimal y binario")
    while True:
        tipo = random.choice(["decimal_a_binario", "binario_a_decimal"])
        if tipo == "decimal_a_binario":
            numero_decimal = random.randint(0, 255) # Generar un número decimal aleatorio
            numero_binario = decimal_a_binario(numero_decimal)
            respuesta = input(f"¿Cuál es el equivalente binario de {numero_decimal}? ")
            if respuesta == numero_binario:
                print("¡Correcto!")
            else:
                print(f"Incorrecto. La respuesta correcta es {numero_binario}.")
        else:
            numero_decimal = random.randint(0, 255) # Generar un número decimal aleatorio
            numero_binario = decimal_a_binario(numero_decimal)
            respuesta = input(f"¿Cuál es el equivalente decimal de {numero_binario}? ")
            if respuesta.isdigit() and int(respuesta) == numero_decimal:
                print("¡Correcto!")
            else:
                print(f"Incorrecto. La respuesta correcta es {numero_decimal}.")
        jugar_otra_vez = input("¿Quieres jugar otra vez? (s/n): ").lower()
        if jugar_otra_vez != 's':
            break
    main() # Llamada a la función principal
# Fin del programa