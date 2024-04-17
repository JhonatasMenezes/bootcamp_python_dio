import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent

os.mkdir(ROOT_PATH / 'novo_diretorio')

arquivo = open(ROOT_PATH / 'novo.txt', 'w')
arquivo.close()

# os.rename(ROOT_PATH / 'novo.txt', ROOT_PATH/'alterado.txt')

# os.rmdir(ROOT_PATH/'novo_diretorio/')
# shutil.move(ROOT_PATH/'alterado.txt', ROOT_PATH/'novo_diretorio'/'alterado.txt')
# os.remove(ROOT_PATH/'alterado.txt')
