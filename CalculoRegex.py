import sys
import re

regex = r'(-?\d+)([-+x/])(-?\d+)'

def soma (n1 ,n2):
    return print(int(n1)+int(n2))

def divisao(n1,n2):
    return print(int(n1)/int(n2))

def sub (n1,n2):
    return print(int(n1)-int(n2))

def mult (n1, n2):
    return print(int(n1)*int(n2))

def checar(n1,n2):
    if x[0][1] == "+":
        soma(n1, n2)
    elif x[0][1] == "-":
        sub(n1,n2)
    elif x[0][1] == "x":
        mult(n1,n2)
    elif x[0][1] == "/":
        divisao(n1,n2)

if __name__ == '__main__':

    try:
        string = ''.join(sys.argv[1:])
        x = re.findall(regex, string)
        n1 = x[0][0]
        n2 = x[0][2]
        checar(n1,n2)
    except:
        print("Digite uma operação válida")