from src.converter import ejecutar_conversion_fisica, convertir_contaminante_aire
from src.units import PM_SO2, PM_NO2

def ejecutar_auditoria_ambiental():
    print("\n" + "="*40)
    print("=== SOFTWARE DE GESTION AMBIENTAL ===")
    print("="*40)
    
    # Prueba 1: Residuos
    residuos = ejecutar_conversion_fisica(1.5, "tonne", "kg")
    print(f"[RESIDUOS] 1.5 Toneladas -> {residuos}")

    # Prueba 2: Calidad del Aire (SO2)
    so2_ppm = convertir_contaminante_aire(100, PM_SO2)
    print(f"[AIRE] 100 mg/m3 de SO2 -> {so2_ppm} ppm")
    print("="*40 + "\n")

if __name__ == "__main__":
    ejecutar_auditoria_ambiental()
