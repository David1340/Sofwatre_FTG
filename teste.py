lista = []

id_Totem = '5'

with open('Configuração dos totens.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
            lista.append(linha.strip().split(" ")[1])

print(lista)
print(lista.index(id_Totem))