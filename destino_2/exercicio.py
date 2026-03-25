'''
#exercicio 1
def inverter(texto):
    invert= ''.join(reversed(texto))
    return print(invert)
inverter()

#exercicio 2
def polimdromo(texto):
    if texto == texto[::-1]:
        return print(f'a palavra {texto} é um polindromo')
    else:
        return print(f'a palavra {texto} não é um polindromo')

polimdromo()
'''
'''
#exercicio 3

def quantidade_de_litras(texto,letras):
    numero_letras= texto.lower().count(letras)
    return print(numero_letras)


texto='converte palavras para letras maiúsculas / minúsculas, respectivamente'
quantidade_de_litras(texto, 'a')



'''
# exercicio 4
'''
def subs_por_ast(texto):    
    ast= texto.replace('a','*').replace('e','*').replace('i','*').replace('o','*').replace('u','*')
    return ast

print(subs_por_ast('O documento apresenta uma lista abrangente de 100'))

'''
# exercicio 5
'''
def caratere(nomes):
    maior_letras = 0
    for nome in nomes:
        sem_repetir_letra = set(nome)
        numero_letras= len(sem_repetir_letra)
        if numero_letras> maior_letras:
            maior_letras= numero_letras
    return print(f'o nome mais logo contem {maior_letras} letras sem repetir ') 

nomes='elton','elivelton','selma','danila','daila'

caratere(nomes)
'''
# exercicio 6
'''
def letras_unicas(string):

    nova_string= ''.join(dict.fromkeys(string))

    return print(nova_string)
letras_unicas('elivelton')
'''
# exercicio 7
'''
def anagrama(palavra_1,palavra_2):
    p1_lista=[]
    p2_lista=[]

    for p1 in palavra_1:
        p1_lista.append(p1)
    for p2 in palavra_2:
        p2_lista.append(p2)
    if set(p1_lista) == set(p2_lista):
        return print('as palavras são anagramas')
    else:
        return print('as palavras não são anagramas')
    
anagrama('danila','lidani')
'''
# exercicio 8
'''
def permutando(palavra):
    from itertools import permutations
    
    permuta= permutations(palavra)
    for permutacao in permuta:
        res=''.join(permutacao)        
        print(res)


permutando('elton')
'''
# exercicio 9
'''
def substring_comun(palavra_1,palavra_2):
    import itertools    
    lista_1=[]
    lista_2=[]
    sequencia=0
    for p1 in palavra_1:
        lista_1.append(p1)       
    for p2 in palavra_2:
        lista_2.append(p2)
    for l1,l2 in itertools.zip_longest(lista_1,lista_2):
        if l1 == l2:
            sequencia=sequencia + 1
    return print(sequencia)
    
substring_comun('abacate','abacaxi')
'''
# exercicio 10
'''
def contaagem_letra(palavra):
    from collections import Counter
    contagem = Counter(palavra)
    resultado=[]
    for letra,num in contagem.items():
        resultado.append(letra)
        resultado.append(num)
    return print(resultado)
contaagem_letra('aaabbbcce')
 '''  



   
    
 