print('numero secreto')

numero=int(10)

descobriu= False

for n in range (3):
    if not descobriu:
        dig=int(input('digite um numero: '))

    if dig>numero:
            print('numero alto')
    elif dig<numero:
            print('numero baixo')
    else:
            print('desciobriu')
            descobriu=True


if descobriu==True:
     print('parabens voce ganhou')
else:
    print(f'o numero secreto era {numero}')     


print('\n\n\n')


while True:
    num=input(' digite um numero; [digie "sair" para sair]: ')

    if num== 'sair':
        print('finalizado')
        break
   
    elif num not in('1','2','3'):
        print(' opção invalida')
        continue
    else:
        print(f' voce escolheu: {num}')

print('\n\n\n\n')

texto= """
   Python é uma linguagem de programação de alto nível,[11] interpretada de script, imperativa, orientada a objetos,
     funcional, de tipagem dinâmica e forte. Foi lançada por Guido van Rossum em 1991.[1] Atualmente, possui um modelo 
     de desenvolvimento comunitário, aberto e gerenciado pela organização sem fins lucrativos Python Software Foundation. 
     Apesar de várias partes da linguagem possuírem padrões e especificações formais, a linguagem, como um todo, não é 
     formalmente especificada. O padrão na pratica é a implementação CPython. """

for n in texto:
    texto.lower()
print(f'ha '  +str(texto.lower().count('a'))+' letras A no texto')
print(f'ha '  +str(texto.lower().count('e'))+' letras E no texto')
print(f'ha '  +str(texto.lower().count('i'))+' letras I no texto')
print(f'ha '  +str(texto.lower().count('o'))+' letras O no texto')
print(f'ha '  +str(texto.lower().count('u'))+' letras U no texto')


print('\n\n\n')


    


    
import sys
print(' rejuste de salarios ')

salario_atual=float(input(' digite seu salario atual: '))

genero=input('digite seu sexo[masc/fem]: ')

if genero!= 'fem'and genero!='masc':
    print('opção invalida')
    sys.exit()
tempo=int(input(' digite quanto tempo trablha na empresa: '))

if genero== 'fem' and tempo < 15:
    novosal15= salario_atual + ((salario_atual*5)/100)
    print(f'seu salario reajustado é de: {novosal15}')

elif genero== 'fem' and tempo > 15 and tempo<=20:
    novosal20= salario_atual + ((salario_atual*12)/100)
    print(f'seu salario reajustado é de: {novosal20}')

elif genero== 'fem' and tempo>20:
    novosal23= salario_atual + ((salario_atual*23)/100)
    print(f'seu salario reajustado é de: {novosal23}')

elif genero== 'masc' and tempo < 20:
    novosalm3= salario_atual + ((salario_atual*3)/100)
    print(f'seu salario reajustado é de: {novosalm3}')

elif genero== 'masc' and tempo >= 20 and tempo<=30:
    novosalm13= salario_atual + ((salario_atual*13)/100)
    print(f'seu salario reajustado é de: {novosalm13}')

elif genero== 'masc' and tempo>30:
    novosalm25= salario_atual + ((salario_atual*25)/100)
    print(f'seu salario reajustado é de: {novosalm25}')

    

    print(' analise de idades ')

maior_idade=0
menor_idade_femenina= float('inf')
quantidade_masculina=0
soma=0
media_soma=0


import sys

while True:
    sexo=input(' digite seu genero [f/m]: ')
 
        
    idade= int(input(' digite a sua iadade: '))
    
    

    #maior idade lida 
    if idade > maior_idade:
        maior_idade = idade

    #quantos homens foram cadastrados
    if sexo=='m':
        quantidade_masculina = quantidade_masculina  +1
        soma = soma + idade
      
    #qual a idade da mullher mais jovem
    if sexo == 'f':
        if idade < menor_idade_femenina:
            menor_idade_femenina = idade

    #idade media dos homens 
    if sexo=='m':
        
        media_soma = soma / quantidade_masculina 

    #  fim do lupim
    desejo=(input('deseja continuar s/n? '))
    if desejo =='s':
        continue
    elif desejo == 'n':
        break
    else:
        print(' opção invalida')
        sys.exit()

print(' resultados finais\n ')

print(f' a maior idade lida é: {maior_idade}')
print(f'total de homens cadastrados: {quantidade_masculina}')
print(f'a mulher mais jovem tem a idade de :{menor_idade_femenina}')
print(f'a media de idade entre os homens é de: {media_soma}')



pessoa_mais_velha=0
mulher_mais_joven= float('inf')
media_idade=0
soma=0
quantidade_de_pessoas=0
mais_30=0
mulher_menos18= 0
nome_mulher_joven=''
nome_pessoa_mais_velha=''
#inicialização de programa 
import sys

while True:
#coleta de dados:
    nome= input(' digite seu nome: ')

    idade= int(input(' digite a sua idade: '))

    genero= input('qual seu genero [m/f]: ')
#quantidade de pessoas:
    if idade > 0: 
        quantidade_de_pessoas= quantidade_de_pessoas + 1
#calculo de media de idade de grupo:
        soma= soma + idade

        media_idade= soma/ quantidade_de_pessoas 
#nome da pessoa mais velha:
    if idade>pessoa_mais_velha:
        pessoa_mais_velha=idade
        nome_pessoa_mais_velha=nome
#nome da mulher mais joven       
    if genero=='f':
        if idade < mulher_mais_joven:
            mulher_mais_joven=idade
            nome_mulher_joven=nome
#quantidade de homens quem tem idade maior que 30 anos:           
    if genero=='m':
        if idade > 30:
            mais_30 = mais_30 + 1
#quantidade de mulheres que tem idade menor que 18 anos :
    if genero=='f':
        if idade < 18:
            mulher_menos18= mulher_menos18 + 1
    
#perguntar se vai continuar programa 
    desejo=input('deseja continuar [s/n]') 

    print('\n') 

    if desejo== 's':
        continue
    elif desejo=='n':
        break
    else:
        sys.exit()
#exipição de resultados finais;
print(f' resultados finais \n')

print(f'O idade da pessoa mais velha: {nome_pessoa_mais_velha}')
print(f'O idade da mulher mais jovem: {nome_mulher_joven}')
print(f'A média de idade do grupo: {media_idade}')
print(f'Quantos homens tem mais de 30 anos: {mais_30}')
print(f'Quantas mulheres tem menos de 18 anos: {mulher_menos18}')







 # calculos para terreno
anual=0

soma=0
while True:
     ano= float(int(input(' quanto a parcela do ano: ')))

     anual= ano * 12

     soma= soma + anual

     desejo= input('deseja continuar?[s/n] ')

     if desejo=='s':
          continue
     elif desejo=='n':
          break

print('resultado final\n ')

print(soma)



#jogos de quesão de capital
capitais={'Paraiba':'João Pessoa',
          'Acre':'Rio Branco',
          'Alagoas':'Maceio',
          'Pernambuco':'Recife',
          'São Paulo':'São Paulo',
          'Rio de Janeiro':'Rio de Janeiro',
          'Bahia':'Salvador',
          'Minas Gerais':'Belo Horizonte',
          'Santa Catarina':'Floranopolis',
          'Rio Grando do Sul':'Porto Alegre',
          'Rio Grando do Norte':'Natal',
          'Para':'Belem',
          'Amapa':'Macapa',
          'Amazonas':'Manaus',
          'Fortaleza':'Ceara',
          'Distrito Federal':'Brasilia',
          'Espirito Santo':'Vitoria',
          'Goias':'Goiania',
          'Maranhão':'São Luiz',
          'Mato Grosso':'Cuiaba',
          'Mato Grosso do Sul':'Campo Grando',
          'Parana':'Curitiba',
          'Piaui':'Teresina',
          'Sergipe':'Aracaju',
          'Roraima':'Boa Vista',
          'Rondonia':'Porto Velho',
          'Tocantins':'Palmas',
        } 
# delaração de variaveis
acertos=0

erros= 0

total= 0

porcentagem= 0

quer_continuar=True

#esqueleto ta operaão
for estado in capitais:

    if not quer_continuar:
        break
            
    capital= capitais [estado]
#preenchimento de dados           
    resposta=input(f'qual a capital de {estado}? ')
#condição de respostas e contabilidade de acertos erros                                   
    if resposta.upper() == capital.upper():
        print('parabens! resposta correta')
        acertos= acertos + 1
    else:
        print(f'resposta errada! a capitadl de {estado} é {capital}')
        erros=erros + 1        
#condição se pretende continuar
    while True:
         desejo=input(' deseja continuar? [s/n]').lower()

         if desejo not in ['s','n']:
             print(' escolha "s" para sim e "n" para não! ')
             continue
         elif desejo=='s':
             break
         elif desejo == 'n':
            quer_continuar=False
            break
             

#ctotado de acertos e erros 
total= acertos + erros
#calculos de porcentagem
porcentagem= (acertos/total)*100
#impressão de resultados 
print(f' parabens! voçê acertou {acertos} questões.')
print(f' sua procentagem de acertos fou de {porcentagem} %')
                