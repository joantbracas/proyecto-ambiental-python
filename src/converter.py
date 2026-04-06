from src.units import ureg, VOLUMEN_MOLAR_25C

def ejecutar_conversion_fisica(valor, origen, destino):
    """Conversiones de masa, volumen, longitud, etc."""
    try:
        return (valor * ureg(origen)).to(destino)
    except Exception as e:
        return f"Error físico: {e}"

def convertir_contaminante_aire(valor, mw, de_unidad="mg/m**3", a_unidad="ppm"):
    """
    Convierte concentraciones de gases bajo condiciones estándar.
    Fórmula: ppm = (mg/m3 * 24.45) / MW
    """
    try:
        if de_unidad == "mg/m**3" and a_unidad == "ppm":
            resultado = (valor * VOLUMEN_MOLAR_25C) / mw
            return round(resultado, 4)
            
        elif de_unidad == "ppm" and a_unidad == "mg/m**3":
            resultado = (valor * mw) / VOLUMEN_MOLAR_25C
            return round(resultado, 4)
            
        return "Unidades no compatibles para aire"
    except Exception as e:
        return f"Error químico: {e}"