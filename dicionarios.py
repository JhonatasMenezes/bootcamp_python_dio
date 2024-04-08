# Métodos Dict

meu_dicionario = {
    "chave1": "valor1",
    "chave2": ["valor2, valor2_1"],
    "chave3": {
        "chave3_1": "valor3_1"
    }
}

# clear() - limpa todos os dados do dicionario
meu_dicionario_2 = meu_dicionario.clear()
print(meu_dicionario_2)

# copy() - copia os valores em outra variável
meu_dicionario_2 = meu_dicionario.copy()
print(meu_dicionario_2)

# fromkeys() - cria várias chaves de maneira mais rápida e também pode incluir valores (tipo INSERT INTO)
meu_dicionario_2 = meu_dicionario.fromkeys(["chave4", "chave5"], "valor4", "valor5")
print(meu_dicionario_2)

# get() - retorna None se a chave for inexistente sem keyerror
exemplo = meu_dicionario.get("chave6") # get(chave, if is not retorna 2° arg)
print(exemplo)

# items() - retorna uma lista de tuplas com os valores do dict, bom pra iterar
itens = meu_dicionario.items()

# keys() - retorna as chaves em uma lista
lista_de_chaves = meu_dicionario.keys()

# pop() - remove uma chave informada ou um 2° arg
resposta = meu_dicionario.pop("chave7", "ou isso")

# setdefault() - adiciona chave valor caso já não exista
meu_dicionario.setdefault("chavve1", "valor3")

# update() - atualiza valor de uma chave ou adiciona caso nãio exista ainda
meu_dicionario.update("chave6", "valor")

# values() - retorna uma lista com os valores do dict
meu_dicionario.values()

# in - consegue iterar sobre uma lista e verificar se existe o valor solicitado 
existe_chave = "chave3" in  meu_dicionario
existe_valor = "valor2_1" in meu_dicionario["chave2"]

# del - deleta uma chave ou um valor
del meu_dicionario["chave3"]
del meu_dicionario["chave6"]
print(meu_dicionario)

