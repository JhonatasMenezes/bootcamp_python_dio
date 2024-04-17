from pathlib import Path

ROOT_PATH = Path(__file__).parent

try:
    with open(ROOT_PATH / 'novo.txt', 'r') as arquivo:
        print(arquivo.read())
except IOError as exc:
    print(f"\nErro ao abrir o arquivo: {exc}\n")


try:
    with open(ROOT_PATH / 'novo_arquivo.txt', 'w', encoding='utf-8') as arquivo:
        arquivo.write("Aprendendo a manipular arquivos com python.")
except IOError as exc:
    print(f"\nErro ao abrir o arquivo: {exc}\n")


try:
    with open(ROOT_PATH / 'novo_arquivo.txt', 'w', encoding='ascii') as arquivo:
        arquivo.write("Aprendendo a manipular arquivos com python.")
except IOError as exc:
    print(f"\nErro ao abrir o arquivo: {exc}\n")
except UnicodeDecodeError as exc:
    print(f"\nErro ao abrir o arquivo: {exc}\n")
