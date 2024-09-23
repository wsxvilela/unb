def desenhar_casinha(tamanho):

    if tamanho < 3:
        print("O tamanho deve ser maior ou igual a 3.")
        return

    for i in range(tamanho):
        espacos = '  ' * (tamanho - i - 1)
        telhado = '*' * (4 * i + 2)
        print(espacos + telhado + espacos)

    largura = 4 * tamanho - 2
    for i in range(tamanho):
        if i == tamanho - 1:
            print('|' + ' ' * (largura - 2) + '|')
        else:
            print('|' + ' ' * (largura - 2) + '|')


    print('|' + '_' * (largura - 2) + '|')

tamanho = 4
desenhar_casinha(tamanho)