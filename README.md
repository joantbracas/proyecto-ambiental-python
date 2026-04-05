# 🌿 Convertidor de Unidades Ambientales
Herramienta modular en Python para cálculos precisos de ingeniería (Masa, Temperatura, Longitud) usando la librería `Pint`.

## Estructura
- `src/`: Lógica principal del convertidor.
- `tests/`: Pruebas unitarias de precisión.
# 🌿 Convertidor de Unidades de Ingeniería Ambiental

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

Este proyecto es una herramienta modular diseñada para automatizar y asegurar la precisión en las conversiones de unidades utilizadas en la ingeniería ambiental (gestión de residuos, emisiones atmosféricas y vertimientos).

## 🚀 Características
- **Precisión Científica:** Utiliza la librería `Pint` para el manejo de dimensiones físicas.
- **Estructura Modular:** Separación clara entre lógica de cálculo, interfaz y pruebas.
- **Escalable:** Fácil de añadir nuevos factores de conversión específicos (ej. densidades de RCD).

## 📁 Estructura del Proyecto
- `src/converter.py`: Lógica principal de conversión.
- `src/units.py`: Configuración del registro de unidades.
- `src/cli.py`: Interfaz de línea de comandos para el usuario.
- `tests/`: Pruebas unitarias para validar los cálculos.

## 🛠️ Instalación
1. Clonar el repositorio:
   ```bash
   git clone [https://github.com/joantbracas/proyecto-ambiental-python.git](https://github.com/joantbracas/proyecto-ambiental-python.git)
   