# variáveis  
contador = 1 
soma = 0
# entrad e processamento
while contador < 8:
    num = float(input("Digite um número: "))
    soma += num 
    contador += 1 
# saída
print("A soma de todos os números digitados é:",soma)