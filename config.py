import sys
DATABAE_PATH = 'clientes.csv'

if "pytest" in sys.argv[0]:
    DATABAE_PATH = "tests/clientes_test.csv"