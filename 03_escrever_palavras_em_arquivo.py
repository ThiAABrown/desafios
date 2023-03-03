# Usando o arquivo "notion.txt" criado no desafio 01,
# esse script deve ler o arquivo e gravar um novo arquivo "saida.txt",
# escrevendo uma linha nesse arquivo para cada palavra que começa com a letra "c".

#Criando um novo arquivo e escrevendo as palavras.
def escrever(palavra):
    with open('saida.txt', 'a') as Novo_Arquivo:
        Novo_Arquivo.write(palavra + '\n')

#pegar palavras de uma linha
def pegar_palavras(linha):
    palavras = linha.split(' ')
    return palavras
__import__('ipdb').set_trace()
#Abrir e ler o arquivo notion.
Arquivo = open('notion.txt', 'r')
linhas = Arquivo.readlines()
#Procurar cada palavra que começa com a letra "c".
for linha in linhas:
    # pegar palavras de uma linha
    palavras = pegar_palavras(linha)

    # para cada palavra, ver se comeca com a letra c. (for)
for palavra in palavras:
    if palavra.startswith('c'):
        escrever(palavra)

    # se comeca, chamar a funcao que escreve a palavra no arquivo (if)
    
