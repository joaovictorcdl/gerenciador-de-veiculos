veiculos = []
multas = []

def cadastrar_veiculos():
    guardando = []
    nomecarro = input('Informe o nome do veículo: ')
    placacarro = input('Insira a placa do veículo: ')
    ufcarro = str(input('Insira o UF do veículo: '))
    ano = int(input('Insira o ano do carro: '))
    guardando = [nomecarro, placacarro, ufcarro, ano]
    veiculos.append(guardando)
    pergunta_multas = str(input('Existem multas para serem cadastradas? y/n'))
    if pergunta_multas == 'y':
        cadastrar_multas()
        print('Veículo cadastrado com sucesso.')
    else:
        print('Veículo cadastrado com sucesso.')

def cadastrar_multas():
    print('Vamos cadastrar as multas do seu veículo, por favor insira: ')
    placa = str(input('Placa: '))
    data = str(input('Data: '))
    local = str(input('Local: '))
    valor = float(input('Valor: '))
    multas.append(placa, data, local, valor)

def ver_multas(iplaca):
    for carros in multas:
        if iplaca == multas[0]:
            print('Informações: ')
            print('Placa: ', carros[0])
            print('Data: ', carros[1])
            print('Local: ', carros[2])
            print('Valor: ', carros[3])
            print('-=' * 30)
            return
        else:
            print('Sem multas cadastradas.')

def listarveiculos():
    print('Confira todos os veículos cadastrados: ')
    for carroscadastrados in veiculos:
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
            print('Carros que constam com esse UF: ')
            print('Nome: ', carro[0])
            print('Placa: ', carro[1])
            print('UF: ', carro[2])
            encontrado = True # muda o valor para verdadeiro, ao menos um foi encontrado, então, ao percorrer e encontrar, o valor vai mudar para True e vai exibir o carro.
    if encontrado == False:
        print('Não foram encontrados veículos para esse UF.')
