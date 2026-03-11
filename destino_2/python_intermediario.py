'''
exercicio 1
def reverte_palavra (palavra:str):
    palavra_reversa= palavra[::-1]
    return print(palavra_reversa)
reverte_palavra('elton')
'''
'''
exercicio 2
def gera_senha():
    import secrets
    import string
    caractere= string.ascii_letters + string.digits
    senha= ''.join(secrets.choice(caractere) for _ in range(8))
    return print(senha)
gera_senha()
'''
'''
exercicio 3
def gerar_intervalo (primeira_data,segunda_data):
    from datetime import date 
    primeira_data= date.strptime(primeira_data, '%d/%m/%Y')
    segunda_data= date.strptime(segunda_data, '%d/%m/%Y')

    resulta= segunda_data - primeira_data 

    return resulta.days

print(gerar_intervalo('01/02/2023', '01/02/2023'))
'''
'''
exercicio 4
def retorna_mes(resultado):
    meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
             'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezendo']
    if resultado >= 1 and resultado <= 12:
        return meses[resultado-1]
    else:
        return 'Erro'
print(retorna_mes(1))
''' 
'''
exercicio 5
def gerar_fibonacci (fib):
    n1=0
    n2=1
    fib_lista=[0]
    for _ in range(fib):
            n3= n1 + n2
            n2 = n1
            n1= n3
            fib_lista.append(n3)
            
    return print(fib_lista)
gerar_fibonacci(7)
'''
'''
exercicio 7
def adiciona_prefixo (palavra:str):
    if palavra.startswith('foto'):
        return  palavra 
    else:
        return 'foto' + palavra

    
print( adiciona_prefixo('Cachorro'))
'''
'''
exercicio 8

def conta_elementos (elemenoto_1:list,elemento_2):
    
    if elemento_2 in elemenoto_1:
        quantidade= elemenoto_1.count(elemento_2)
        return print(f'O elemento foi encontrado {quantidade} vezes na lista informada')
    else:
        return print('Não foi encontrado nenhum elemento na lista informada')

conta_elementos([5, 7, 'lapis', 10, 'avião', 5, 'lapis', 4,'lapis'], 65)
'''
'''
#exercicio 9
def interseccao_conjuntos (argumento_1, argumento_2):
    inter= argumento_1.intersection(argumento_2) #ou usar '&'
    return inter
print(interseccao_conjuntos({5, 'uva',  10, '20'}, {5, 'uva', 'arroz', 20, 10}))
'''
'''
exercicio 10
def soma_valores_diferentes(n1,n2,n3):
    if n1 == n2 == n3:
        return 0
    if n1 == n2 != n3:
        return n3
    if n1 == n3 != n2:
        return n2
    if n2 == n3 != n1:
        return n1
    else:
        return n1+n2+n3
    
print(soma_valores_diferentes(5,15,10))
'''
'''
exercicio 13
def get_typer (argumento):
    if type(argumento)== list:
        return "O atributo é uma lista."
    if type(argumento)== tuple:
        return "O atributo é uma tupla."
    if type(argumento)== set:
        return "O atributo é uma set."
    if type(argumento)== dict:
        return "O atributo é uma dicionario."
    else:
        return 'O atributo não é nem lista, nem set, nem tupla nem dicionário.'

print(get_typer((2,3,5,8)))
'''
'''
exercicio 14
def tabuada(numero):
    lista=[]
    
    for n in range(1,10):
        res= numero * n
        lista.append(res)
    return lista
    
print(tabuada(4.5))
''' 




'''
exercicio 15
def verifica_diferenca (lista:list):
        if len(lista) != len(set(lista)):
            return 'A lista possui valores iguais.'
        else:
            return 'A lista possui apenas valores únicos.'
print(verifica_diferenca(['abc', 10, 5, 'str', 8, 9]))
'''
'''
exercicio 16
def histograma (lista):
    nova_lista=[]

    for n in lista:
        res = n * '*'
        nova_lista.append(res)
        conver= '\n'.join(nova_lista)
       
    return print (conver)
  
histograma([1, 2, 3, 8,1])
'''           
'''
Exercicio 17
def mediana (lista:list):
    lista.sort()
    if len(lista) % 2==0:
        med_2= len(lista)//2
        med_1= med_2 - 1
        valor_1= lista[med_1]
        valor_2= lista[med_2]
        resultado= (valor_1 + valor_2) / 2
        return int(resultado)
    else:
        impa= len(lista)// 2 
        res= lista[impa]
        return res
    
print(mediana([1,20, 22, 12, 74, 36]))
'''  
'''
Exercicio 18 
def temperatura(Celsius ):
    Fahrenheit= (Celsius * 9/5) + 32
    Kelvin= Celsius + 273
    return print(f'{Fahrenheit} Fahrenheit e {Kelvin} Kelvin')
temperatura(-5)
'''
'''
exercicio 19
def divisores(numero):
    contador_divisores = 0

    for i in range(1, numero +1 ):
       
        if numero % i == 0:

            contador_divisores += 1  
    print(contador_divisores)

divisores(50)
'''

'''
exercicio 20
def ordena_dec(lista:list):
    lista.sort()
    lista.reverse()

    return print(lista)
ordena_dec([1, 2, 10, 11, 12, 99, 3, 4])

'''
'''
import re
texto = """
    A reunião está marcada para o dia 15/03/2023.
    Lembre-se de entregar o relatório até 28/02/2023.
    O evento acontecerá em 10/04/2023 no auditório principal
    """

padrao='[0-9]{2}/[0-9]{2}/[0-9]{4}'
datas= re.findall(padrao,texto)
print(datas)
'''

'''
#cadatsro de pessoas

lista_de_nomes=[]
indice_valor=[]
while True:
    cadastrar_pessoas= input('digite o nome: ')
    lista_de_nomes.append(cadastrar_pessoas)
    continue_ = input('desja conditunar[s/n]: ')
    if continue_=='s':        
        continue
    elif continue_ == 'n':
        break
for indice,itens in enumerate(lista_de_nomes,1):
    indice_valor.append(indice)
    cadastro_de_pessoas=dict(zip(lista_de_nomes,indice_valor))
print(cadastro_de_pessoas)
'''

print ('ola mundo ')


            









   

        



    

    
    












