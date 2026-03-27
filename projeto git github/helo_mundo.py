print('helo git ')
print ('ola tudo bem?')


print('mais uma alteração ')

def soma (a,b):
    return a+b


print(soma(5,8))

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