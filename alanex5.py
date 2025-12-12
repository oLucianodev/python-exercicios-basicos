#variáveis 
cat1 = 0
cat2 = 0 
cat1idade = 0
cat2idade = 0
continu = "s"

#entrada, de repetição
while continu.lower() == "s":
 nome = input("Nome : ")
 idade= int(input("Idade: "))
 peso = float(input("Peso: "))

#processamento
 if 20 <= idade <= 30: 
    if peso < 80:
         cat1 += 1 
         cat1idade += idade
    else: 
        cat2 += 1
        cat2idade += idade 
 else: 
     print("Incrição invalida, o usuario nao tem a idade permetida para participar")

# deseja continuar
 continu = input("usuario cadastrado, deseja cadastrar outro participante? (s/n): ")

#calculo das idades médias 
if cat1 > 0:
    mediacat1 = cat1idade/cat1
else: 
    mediacat1 = 0

if cat2 > 0:
    mediacat2 = cat2idade/cat2
else: 
    mediacat2 = 0

#saída, mostra quantos incritos e a idade média nas categorias
print(f"Categoria de menores de 80kg: {cat1} inscritos, idade média: {mediacat1} anos")
print(f"Categoria de 80kg ou mais: {cat2} inscritos, idade média: {mediacat2} anos")