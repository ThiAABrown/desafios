# Usando o arquivo "notion.txt" criado no desafio 01,
# esse script deve ler o arquivo e exibir na tela a quantidade de palavras nesse arquivo.

Arquivo = open('notion.txt')
linhas = Arquivo.readlines()
__import__('ipdb').set_trace()
total_palavras = 0
for linha in linhas:
    palavras = linha.split()
    total_palavras_linha = len(palavras)
    total_palavras += total_palavras_linha


print(total_palavras)
