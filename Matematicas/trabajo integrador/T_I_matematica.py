# T.I Matematica
import random

def decimal_a_binario(n):
    """Función para convertir un número decimal a binario."""
    if n == 0:
        return "0"
    binario = ""
    while n > 0:
        binario = str(n % 2) + binario
        n //= 2
    return binario

def binario_a_decimal(b):
    """Función para convertir un número binario a decimal."""
    decimal = 0
    # enumerate(reversed(b)) recorre el string binario de derecha a izquierda
    # 'i' será la posición (0, 1, 2,...) y 'digito' será el carácter ('0' o '1')
    for i, digito in enumerate(reversed(b)):
        decimal += int(digito) * (2 ** i)
    return decimal

def main():
    """Función principal del juego."""
    print(" ¡Bienvenido al Juego de Conversión Binario-Decimal! ")

    while True:
        # Elige aleatoriamente el tipo de conversión
        tipo_conversion = random.choice(["decimal_a_binario", "binario_a_decimal"])
        
        # Genera un número aleatorio entre 1 y 100 para el desafío
        numero_a_convertir = random.randint(1, 100)

        if tipo_conversion == "decimal_a_binario":
            # --- Desafío: Convertir de Decimal a Binario ---
            respuesta_correcta = decimal_a_binario(numero_a_convertir)
            pregunta = f"¿Cuál es el equivalente binario de {numero_a_convertir}? "
            
            respuesta_usuario = input(pregunta)
            
            if respuesta_usuario == respuesta_correcta:
                print(" ¡Correcto! ¡Muy bien!")
            else:
                print(f" Incorrecto. La respuesta correcta era: {respuesta_correcta}")

        else: # tipo_conversion == "binario_a_decimal"
            # --- Desafío: Convertir de Binario a Decimal ---
            numero_binario = decimal_a_binario(numero_a_convertir)
            respuesta_correcta = numero_a_convertir
            pregunta = f"¿Cuál es el equivalente decimal de {numero_binario}? "

            try:
                # Intentamos convertir la respuesta del usuario a entero
                respuesta_usuario = int(input(pregunta))
                if respuesta_usuario == respuesta_correcta:
                    print(" ¡Correcto! ¡Excelente trabajo!")
                else:
                    print(f" Incorrecto. La respuesta correcta era: {respuesta_correcta}")
            except ValueError:
                # Esto se ejecuta si el usuario no introduce un número válido
                print(f" Entrada no válida. La respuesta correcta era: {respuesta_correcta}")

        # Preguntar al usuario si quiere jugar otra vez
        jugar_de_nuevo = input("¿Quieres jugar otra vez? (s/n): ").lower()
        if jugar_de_nuevo != 's':
            print("¡Gracias por jugar! ")
            break # Rompe el bucle while y termina el juego

# Ejecutar la función principal solo si el script se corre directamente
if __name__ == "__main__":
    main()
 