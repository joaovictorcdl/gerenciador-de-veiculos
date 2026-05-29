veiculos = []

def cadastrar_veiculos():
    guardando = []
    nomecarro = input('Informe o nome do veículo: ')
    placacarro = input('Insira a placa do veículo: ')
    ufcarro = str(input('Insira o UF do veículo: '))
    guardando = [nomecarro, placacarro, ufcarro]
    veiculos.append(guardando)
    print('-=' * 30)

def listarveiculos():
    print('Confira todos os veículos cadastrados: ')
    for carroscadastrados in veiculos:
        print('-=' * 30)
        print('Nome do veiculo: ', carroscadastrados[0])
        print('Placa do veículo: ', carroscadastrados[1])
        print('UF: ', carroscadastrados[2])
        print('-=' * 30)

def procurandoporplaca(achandoplaca):
    for carros in veiculos:
        if achandoplaca == carros[1]:
            print('Veículo encontrado!!')
            print('Nome: ', carros[0])
            print('Placa: ', carros[1])
            print('UF: ', carros[2])
            return
        else:
            print('Não encontrado.')

def procurandoporuf():
    encontrado = False # Vai servir como "controlador"
    uf = input('Informe o UF: ')
    for carro in veiculos:
        if carro[2] == uf:
            print('-=' * 30)
            print('Carros que constam com esse UF: ')
            print('Nome: ', carro[0])
            print('Placa: ', carro[1])
            print('UF: ', carro[2])
            encontrado = True # muda o valor para verdadeiro, ao menos um foi encontrado, então, ao percorrer e encontrar, o valor vai mudar para True e vai exibir o carro.
    if encontrado == False:
        print('Não foram encontrados veículos para esse UF.')