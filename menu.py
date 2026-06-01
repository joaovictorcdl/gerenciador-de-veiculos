from functions import *

def menu():
    while True:
        print('-=' * 30)
        print(' BOAS-VINDAS À CENTRAL DE VEÍCULOS ')
        print('[1] - Cadastrar veículo')
        print('[2] - Listar veículos')
        print('[3] - Pesquisar por placa')
        print('[4] - Listar veículos por UF')
        print('[5] - Consultar multas')
        print('[6] - Sair')
        print('-=' * 30)
        opcao = int(input('Selecione uma opção: '))
        if opcao == 1:
            cadastrar_veiculos()
        elif opcao == 2:
            listarveiculos()
        elif opcao == 3:
            informep = input('Informe a placa do veículo que você quer procurar: ')
            procurandoporplaca(informep)
        elif opcao == 4:
            procurandoporuf()
        elif opcao == 5:
            informeplaca = str(input('Por favor, informe a placa para consultar as multas: '))
            ver_multas(informeplaca)
        elif opcao == 6:
            break
        else:
            print('Opção não encontrada. Tente novamente.')