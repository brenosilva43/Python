import sys


def soma (n1 ,n2):
    return print(int(n1)+int(n2))

def divisao(n1,n2):
    return print(int(n1)/int(n2))

def sub (n1,n2):
    return print(int(n1)-int(n2))

def mult (n1, n2):
    return print(int(n1)*int(n2))

def check(string):
    if string.find("+") >= 0:
        tipo = string.find('+')
        n1 = string[:tipo]
        n2 = string[tipo+1:]
        soma(n1, n2)
    elif string.find("-") >= 0:
        tipo = string.find('-')
        n1 = string[:tipo]
        n2 = string[tipo + 1:]
        sub(n1,n2)
    elif string.find("x") >= 0:
        tipo = string.find('x')
        n1 = string[:tipo]
        n2 = string[tipo + 1:]
        mult(n1,n2)
    elif string.find("/") >= 0:
        tipo = string.find('/')
        n1 = string[:tipo]
        n2 = string[tipo + 1:]
        divisao(n1,n2)

if __name__ == '__main__':

    string = ''.join(sys.argv[1])
    check(string)










