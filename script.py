from pint import UnitRegistry

# Inicializamos el registro de unidades
ureg = UnitRegistry()

def convertir_unidades(valor, unidad_origen, unidad_destino):
    try:
        # Creamos la cantidad con su unidad inicial
        cantidad = valor * ureg(unidad_origen)
        
        # Realizamos la conversión
        resultado = cantidad.to(unidad_destino)
        
        return resultado
    except Exception as e:
        return f"Error en la conversión: {e}"

# --- PRUEBAS DE INGENIERÍA ---
print("--- Resultados de la prueba ---")

# Ejemplo 1: Temperatura (de Celsius a Fahrenheit)
temp = convertir_unidades(25, "degC", "degF")
print(f"Temperatura: {temp}")

# Ejemplo 2: Longitud (de metros a kilómetros)
distancia = convertir_unidades(1500, "meters", "kilometers")
print(f"Distancia: {distancia}")

# Ejemplo 3: Masa (de kilogramos a miligramos - Muy usado en contaminantes)
masa = convertir_unidades(2, "kg", "mg")
print(f"Masa de sedimento: {masa}")

print("\n¡El script de ingeniería corrió con éxito!")