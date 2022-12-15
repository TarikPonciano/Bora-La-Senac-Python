# def hello(nome):
#     print("Olá", nome)

# hello("Tarik")

# hello("Adriano")

# hello("Carla")

def calcular_pagamento(qtd_horas, valor_hora):
    horas = float(qtd_horas)
    taxa = float(valor_hora)

    if horas<=40:
        salario = horas * taxa
    else:
        horaExtra = horas - 40
        salario = 40*taxa + (horaExtra*(1.5*taxa))
    return salario

horasTrabalhadas = input("Número de horas que trabalhou: ")
taxaDeTrabalho = input("Insira seu valor hora: ")

print(calcular_pagamento(horasTrabalhadas, taxaDeTrabalho))

print(calcular_pagamento("20", "30"))