# frutas = ["Banana", "Maçã", "Laranja", "Abacate", "Graviola", "Uva", "Pêssego"]

# for fruta in frutas:
#     print(fruta)

# texto = "Meu Texto"

# for letra in texto:
#     print(letra)
#     if letra == "t":
#         print("Esta palavra contém a letra t")

frutas = ["Banana", "Maçã", "Laranja", "Abacate", "Graviola", "Uva", "Pêssego"]
print(frutas)

for i in range(5):
    if (i % 2) == 0:
        frutas[i] = ""
    print(frutas[i])
else:
    print("O nosso for acabou")

print(frutas)

