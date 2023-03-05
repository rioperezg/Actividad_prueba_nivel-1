import sys

DATABASE_PATH = "Vehiculos.csv"

if "pytest" in sys.argv[0]:
    DATABASE_PATH = "tests/Vehiculos_test.csv"