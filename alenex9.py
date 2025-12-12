texto = input("Digite seu texto: ")
vogal = 0
for letra in texto:
    if letra in "a,e,i,o,u":
        vogal += 1
        print(letra)
print(f"O número de vogais é {vogal}")