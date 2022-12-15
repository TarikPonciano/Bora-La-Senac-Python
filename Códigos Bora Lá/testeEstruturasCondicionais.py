# media = 8

# if (media > 6.9):
#     print("Você foi aprovado.")
# else:
#     print("Você não foi aprovado.")

#Teste if/elif/else

media = float(input("Insira sua nota: "))

if (media<5):
    print("Você foi reprovado com nota",media)
elif(media>=5 and media<7):
    print("Você ficou de recuperação com nota", media)
else:
    print("Você foi aprovado com nota",media)

# media = int(input("Insira sua nota: "))

# match media:
#     case 0:
#         print("Você foi reprovado.")
#     case 1:
#         print("Você foi reprovado.")
#     case 6:
#         print("Você ficou de recuperação.")
#     case 7:
#         print("Você foi aprovado.")
#     case _:
#         print("Este é um caso padrão.")