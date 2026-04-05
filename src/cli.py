from src.converter import ejecutar_conversion

def mostrar_pruebas():
    print("--- Sistema de Conversión de Ingeniería Ambiental ---")

    # Ejemplo 1: Temperatura
    temp = ejecutar_conversion(25, "degC", "degF")
    print(f"Temperatura: {temp}")

    # Ejemplo 2: Masa de contaminantes
    masa = ejecutar_conversion(2, "kg", "mg")
    print(f"Masa de sedimento: {masa}")

if __name__ == "__main__":
    mostrar_pruebas()