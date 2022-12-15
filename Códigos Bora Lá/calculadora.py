#Crie uma calculadora que recebe 2 números e 1 operador e realiza
#operações matemáticas

def soma(n1,n2):
    return n1 + n2

def subtracao(n1,n2):
    return n1 - n2

def multiplicacao(n1,n2):
    return n1 * n2

def divisao(n1,n2):
    if(n2 == 0):
        global repetir
        repetir = True
        return "Você tentou dividir por 0!"
    else:
        return n1/n2

repetir = True

while (repetir):

    num1 = input("Escreva o número1: ")
    operador = input("Escreva um operador [+,-,*,/]: ")
    num2 = input("Escrava o número2: ")

    if(num1.replace(".","",1).isdigit() or num1.isnumeric()):
        num1 = float(num1)

    if (num2.replace(".","",1).isdigit() or num2.isnumeric()):
        num2 = float(num2)

    if (type(num1) == float and type(num2) == float):
        if (operador == "+"):
            print("Soma:", soma(num1,num2))
            repetir = False
        elif (operador == "-"):
            print("Subtração:", subtracao(num1,num2))
            repetir = False
        elif (operador == "*"):
            print("Multiplicação:", multiplicacao(num1,num2))
            repetir = False
        elif (operador == "/"):
            repetir = False
            print("Divisão:", divisao(num1,num2))
        else:
            print("Você escreveu um operador inválido.")
    else:
        print("Você digitou algum número errado.")