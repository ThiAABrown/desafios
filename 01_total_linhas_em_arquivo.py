# Crie manualmente um arquivo chamado "notion.txt" no diretório atual, e copie o conteúdo de um dos seus posts no notion dentro dele.
# Esse script deve ler o arquivo e exibir na tela a quantidade de linhas nesse arquivo.
#OBS: Não ler as linhas em branco


Arquivo = open('notion.txt')

linhas = Arquivo.readlines()
total_linhas = len(linhas)
__import__('ipdb').set_trace()
for linha in linhas:
    if linha.strip() == '':
        total_linhas -= 1
        # print(linha)

print("Número de linhas no arquivo é:", total_linhas)