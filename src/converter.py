from src.units import ureg

def ejecutar_conversion(valor, unidad_origen, unidad_destino):
    """
    Realiza la conversión de unidades usando la librería Pint.
    Ideal para cálculos de masa de sedimentos o concentraciones.
    """
    try:
        cantidad = valor * ureg(unidad_origen)
        resultado = cantidad.to(unidad_destino)
        return resultado
    except Exception as e:
        return f"Error en la conversión: {e}"