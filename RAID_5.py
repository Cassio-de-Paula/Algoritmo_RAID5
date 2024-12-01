arquivo = [
    [1, 0, 1],
    [0, 1, 1],
    [1, 1, 0],
    [0, 0, 1],
    [1, 1, 1],
    [0, 0, 0],
    [1, 0, 0],
    [0, 1, 0],
    [1, 1, 1],
    [0, 0, 1],
]
def calcula_paridade(linha):
    return (linha[0] != linha[1]) != linha[2]

def raid_5(arquivo):
    cont = 0

    for linha in arquivo:
        # calcula o bit de paridade
        paridade = calcula_paridade(linha)

        # coloca a paridade e os bits em uma mesma lista, na ordem para a impressão
        dados_escrita = linha[:cont] + [paridade] + linha[cont:]

        print(dados_escrita)

        for index, dado in enumerate(dados_escrita):
            # escreve os dados no arquivo de texto na posição do index do dado + 1, já que o nome dos  arquivos começa com disco1.txt
            with open(f'disco{index + 1}.txt', 'a') as disco:
                # usa o modo de escrita append para não sobrescrever os dados do disco a cada looping
                disco.write(f'{dado}\n')
        
        # soma + 1 caso o contador seja menor que 3 ou zera caso contrário para continuar a alternação rotativa entre os discos
        if cont < 3:
            cont += 1
        else:
            cont = 0


raid_5(arquivo)
