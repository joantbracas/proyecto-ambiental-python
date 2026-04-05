from src.converter import ejecutar_conversion

def test_conversion_masa():
    # Verificamos que 1kg sea igual a 1.000.000 mg
    resultado = ejecutar_conversion(1, "kg", "mg")
    assert resultado.magnitude == 1000000

def test_conversion_distancia():
    # Verificamos que 1000m sea 1km
    resultado = ejecutar_conversion(1000, "meter", "kilometer")
    assert resultado.magnitude == 1