#entrada 
#o usuario digitara o valor inferior do intervalo
inf = int(input("Digite o limite inferior: "))

#o usuario digitara o valor superior do intervalo 
sup = int(input("Digite o limite superior: "))
# variaveis 
soma = 0 
contador = inf 

#Processamneto, repetição 
while contador < sup: 
    if contador % 2 == 0: 
        soma += contador
        print(contador) 
    contador +=1  

#saída:
print(f"A soma dos núemros pares é:",soma)