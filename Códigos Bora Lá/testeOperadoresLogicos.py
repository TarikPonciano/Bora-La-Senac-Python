num1 = int(input("Digite um número 1: "))
num2 = int(input("Digite um número 2: "))
num3 = int(input("Digite um número 3: "))

teste1 = num1 > 5 and num1 < 10

teste2 = num2 == num1 or num2 == num3

teste3 = not(num1 > 5 and num1 < 10)

print(teste1)
print(teste2)
print(teste3)