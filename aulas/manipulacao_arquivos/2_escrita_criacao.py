import os


arquivo = open(os.path.abspath("aulas/manipulacao_arquivos/teste.txt"), "w")

arquivo.write("Escrevendo dados em um novo arquivo!")
arquivo.writelines(['\n', 'Escrevendo\n', 'um\n', 'novo\n', 'texto\n'])


arquivo.close()