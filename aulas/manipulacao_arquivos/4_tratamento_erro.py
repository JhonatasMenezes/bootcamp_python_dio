from pathlib import Path


try:
    arquivo = open("meu_arquivo.py")
except FileNotFoundError as exception:
    print("Arquivo não encontrado!")
    print(exception)

ROOT_PATH = Path(__file__).parent

try:
    arquivo = open(ROOT_PATH / "novo_diretorio")
except IsADirectoryError as exception:
    print(f"Não foi possível abrir o arquivo: {exception}")
except IOError as exception:
    print(f"Não foi possível abrir o arquivo: {exception}")
except Exception as exception:
    print(f"Não foi possível abrir o arquivo: {exception}")
