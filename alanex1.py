# variáveis
contador = 1 
num = 0 
maior = 0
menor = 0
# repetição para digitar apenas 10 vezez 
while contador <= 10:
# entrada
    num = int(input("Digite um número: "))
# Processamento 
    if num > 20:
        # primeira saida, caso seja maior que 20
        print("maior") 
        maior +=1
    else:
        # primeira saida, caso seja menor que 20
        print("menor") 
        menor += 1 
    contador += 1 
# Saída final
print("dos 10 numeros digitados,",maior,"foram maiores que 20 e",menor,"menores")
