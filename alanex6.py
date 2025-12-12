#variáveis 
total = 0 
multas = 0 
carteiramoto = 0
continuar = "s"

#entrada, de repetição
while continuar.lower() == "s":
    nome = input("Digite o nome: ")
    carteira = input("Digite o número da carteira de mostorista: ")
    nummultas = int(input("Digite o número de multas: "))

    totalcondutor = 0
    registro = 1 

#processamento, de repetição para o valor da multa 
    while registro <= nummultas: 
        valor = float(input(f"Digite o valor da multa {registro}: "))
        totalcondutor += valor
        registro += 1

#total de quanto o condutor deve 
    print(f"Dívida total do motorista {nome}: R$ {totalcondutor}")

    total += totalcondutor

#verifica o motorista com mais multas, mantendo o com maior número 
    if nummultas > multas: 
        multas = nummultas
        carteiramoto = carteira

#pergunta se deseja cadastrar outro condutor 
    continuar = input("Deseja cadastrar outro motorista? (s/n): ")

#saída: mostra na tela o total arrecado com multas e o motorista que tem mais multas  
print(f"Total arrecadado com multas: R$ {total}")
print(f"Motorista com mais multas: Carteira nº {carteiramoto} ({multas} multas)")