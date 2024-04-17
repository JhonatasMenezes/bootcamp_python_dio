import os


arquivo = open(os.path.abspath("aulas/manipulacao_arquivos/lorem.txt"), "r")

print(arquivo.read())
print(arquivo.readline())
print(arquivo.readlines())

# tip 
# while len( linha := arquivo.readline()):
#     print(linha) 

arquivo.close()