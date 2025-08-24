#parte 2 de herramientas para manejar errores

import logging
import unittest

# -------------------------
# CONFIGURACION DE LOGGING
# -------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="app.log",  #guarda registros en un archivo
    filemode="w"
)

# -------------------------
# FUNCION CON MANEJO DE ERRORES
# -------------------------
def dividir(a, b):
    """Divide dos numeros con manejo de excepciones"""
    try:
        resultado = a / b
        logging.info(f"Division exitosa: {a} / {b} = {resultado}")
        return resultado
    except ZeroDivisionError as e:
        logging.error("Error: division entre cero")
        return "Error: No se puede dividir entre cero"
    except Exception as e:
        logging.exception("Ocurrio un error inesperado")
        return f"Error: {e}"

# -------------------------
# DEMOSTRACION DE DEPURACION
# -------------------------
def ejemplo_debug():
    x = 10
    y = 0
    
    #breakpoint()  
    return dividir(x, y)

# -------------------------
# PRUEBAS UNITARIAS
# -------------------------
class TestDividir(unittest.TestCase):
    def test_division_normal(self):
        self.assertEqual(dividir(10, 2), 5)

    def test_division_por_cero(self):
        self.assertEqual(dividir(10, 0), "Error: No se puede dividir entre cero")

    def test_division_decimal(self):
        self.assertAlmostEqual(dividir(7, 2), 3.5)

# -------------------------
# PROGRAMA PRINCIPAL
# -------------------------
if __name__ == "__main__":
    print("Ejemplo de manejo de errores, registros, depuracion y pruebas unitarias.\n")

    # Ejecucion normal
    print("-----------------------------------")
    print("Resultado de 10 / 2:", dividir(10, 2))
    print("Resultado de 10 / 0:", dividir(10, 0))
    print("-----------------------------------")

    # Simulacion de depuracion
    print("\nSimulacion de depuracion (revisar app.log):")
    ejemplo_debug()

    # Ejecutar pruebas unitarias
    print("\n-----------------------------------")
    print("\nEjecutando pruebas unitarias...\n")
    unittest.main(exit=False)
