
print('======================')
print('Bem vindo a locadora de carro')
print('=========================')
import os 
portfolio= [    ' chevrolet Tracker - R$ 120 / dia',
                    ' chevrolet Onix - R$ 90 / dia',
                    ' chevrolet Spin - R$ 150 / dia',
                    ' Hyunday Hb20 - R$ 85 / dia',
                    ' Hyunday Tucson - R$ 120 / dia',
                    ' Fiat Uno - R$ 60 / dia',
                    ' Fiat Mobi - R$ 70 / dia',
                    ' Fiat Pulse - R$ 120 / dia' ] 
 
escolha_carro=[]
while True:
    print(' O que deseja fazer? ')
    print('0 - mostrar portfolio | 1 - Alugar um carro | 2 - Devolver um carro')
    desejo = input('')
     
    if desejo == '0':
        for indice, carros in enumerate(portfolio):
            print(f'[{indice}] {carros}')
    if desejo == '1':
        for indice, carros in enumerate(portfolio):
            print(f'[{indice}] {carros}')
        print('=========================')    
        print('Escolha o codigo do carro')
        codigo_carro = int(input(''))
        print('Esolha por quantos dias pretende alugar:')
        dias = int(input(''))
        
       
        if codigo_carro == 0:
            total_Pagar= dias * 120
            print(f'voce escolheu chevrolet Tracker por {dias} dias.')
            print(f'O aluguel totalizaria R$ {total_Pagar}. deseja confirmar o aluguel?')
            print('0 - sim | 1 - não ')
            confirmar=input('')
            if confirmar == '0':
                print(f'Parabens você alugou chevrolet Tracker por {dias} dias. ')
                escolha_carro.append(portfolio.pop(codigo_carro))

            elif confirmar == '1':
                continue
       
        elif codigo_carro == 1:
            total_Pagar= dias * 90
            print(f'voce escolheu chevrolet Onix por {dias} dias.')
            print(f'O aluguel totalizaria R$ {total_Pagar}. deseja confirmar o aluguel?')
            print('0 - sim | 1 - não ')
            confirmar=input('')
            if confirmar == '0':
                print(f'Parabens você alugou chevrolet Onix por {dias} dias. ')
                escolha_carro.append(portfolio.pop(codigo_carro))
            elif confirmar == '1':
                continue
        
        elif codigo_carro == 2:
            total_Pagar= dias * 150
            print(f'voce escolheu chevrolet  Spin por {dias} dias.')
            print(f'O aluguel totalizaria R$ {total_Pagar}. deseja confirmar o aluguel?')
            print('0 - sim | 1 - não ')
            confirmar=input('')
            if confirmar == '0':
                print(f'Parabens você alugou cchevrolet  Spin por {dias} dias. ')
                escolha_carro.append(portfolio.pop(codigo_carro))
            elif confirmar == '1':
                continue
       
        elif codigo_carro == 3:
            total_Pagar= dias * 85
            print(f'voce escolheu Hyunday Hb20 por {dias} dias.')
            print(f'O aluguel totalizaria R$ {total_Pagar}. deseja confirmar o aluguel?')
            print('0 - sim | 1 - não ')
            confirmar=input('')
            if confirmar == '0':
                print(f'Parabens você alugou Hyunday Hb20 por {dias} dias. ')
                escolha_carro.append(portfolio.pop(codigo_carro))
            elif confirmar == '1':
                continue
       
        elif codigo_carro == 4:
            total_Pagar= dias * 120
            print(f'voce escolheu Hyunday Tucson por {dias} dias.')
            print(f'O aluguel totalizaria R$ {total_Pagar}. deseja confirmar o aluguel?')
            print('0 - sim | 1 - não ')
            confirmar=input('')
            if confirmar == '0':
                print(f'Parabens você alugou Hyunday Tucson por {dias} dias. ')
                escolha_carro.append(portfolio.pop(codigo_carro))
            elif confirmar == '1':
                continue
      
        elif codigo_carro == 5:
            total_Pagar= dias * 60
            print(f'voce escolheu Fiat Uno por {dias} dias.')
            print(f'O aluguel totalizaria R$ {total_Pagar}. deseja confirmar o aluguel?')
            print('0 - sim | 1 - não ')
            confirmar=input('')
            if confirmar == '0':
                print(f'Parabens você alugou Fiat Uno por {dias} dias. ')
                escolha_carro.append(portfolio.pop(codigo_carro))
            elif confirmar == '1':
                continue

        elif codigo_carro == 6:
            total_Pagar= dias * 70
            print(f'voce escolheu Fiat Mobi por {dias} dias.')
            print(f'O aluguel totalizaria R$ {total_Pagar}. deseja confirmar o aluguel?')
            print('0 - sim | 1 - não ')
            confirmar=input('')
            if confirmar == '0':
                print(f'Parabens você alugou Fiat Mobi por {dias} dias. ')
                escolha_carro.append(portfolio.pop(codigo_carro))
            elif confirmar == '1':
                continue

        elif codigo_carro == 7:
            total_Pagar= dias * 120
            print(f'voce escolheu Fiat Pulse por {dias} dias.')
            print(f'O aluguel totalizaria R$ {total_Pagar}. deseja confirmar o aluguel?')
            print('0 - sim | 1 - não ')
            confirmar=input('')
            if confirmar == '0':
                print(f'Parabens você alugou Fiat Pulse por {dias} dias. ')
                escolha_carro.append(portfolio.pop(codigo_carro))
            elif confirmar == '1':
                continue      

    if desejo == '2':
        if not escolha_carro:
            print(' Não existe carros alugados')
        else:
            for i , carros in enumerate(escolha_carro):
                print(f'[{i}] {carros}')
            print('digite o codigo do carro que deseja devolver:')
            cod=int(input())
            portfolio.append(escolha_carro.pop(cod))
            print('Carro de volvido com sucesso')
    print('====================================')
    print('Deseja continuar ? 1- Sim | 2 - Não ')
    continua=input('')
    if continua ==  '1':
        os.system('cls')
    elif continua == '2':
        break






    

