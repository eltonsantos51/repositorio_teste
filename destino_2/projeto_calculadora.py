import os

while True:
    print('0 : soma')
    print('1 : subtração')
    print('2 : multiplicação')
    print('3 : divisão')
    print('4 : exponeciação')
    print('\n')
    escolha= input('Escolha a operação que deseja realizar: ')
    n1=float(input('escolha o primeiro valor: '))
    n2= float(input('esolha o segundo valor: ')) 
    print('\n')  
   
    if escolha == '0':
        print('>>>>> + escolhida')     
        res= n1 + n2
        print(f'{n1} + {n2} = {res}')        
       
    if escolha == '1':
        print('>>>>> - escolhida')           
        res= n1 - n2
        print(f'{n1} - {n2} = {res}')
        
    if escolha == '2':
        print('>>>>> * escolhida')
        res= n1 * n2
        print(f'{n1} * {n2} = {res}')
       
    if escolha == '3':
        print('>>>>> / escolhida')        
        res= n1 / n2
        print(f'{n1} / {n2} = {res}')
       
    if escolha == '4':
        print('>>>>> ^^ escolhida')           
        res= n1 ** n2
        print(f'{n1} ^^ {n2} = {res}')
    
    desejo= input('Deseja fazer outra operação? 0 - sim, 1 - não ')
    if desejo == '0':
        
        os.system('cls')

    if desejo =='1': 
        break

            

