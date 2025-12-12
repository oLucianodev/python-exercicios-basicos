#contador 
contador = 1 

#entrada, repetição
while contador<= 5:
    print(f"Funcionário {contador}")
    nome = input("Nome do funcionário: ")
    salario = float(input("Salário base: "))
    horas = int(input("Total de horas trbalhadas por dia: "))

#processamento
    if horas > 8: 
        horasext = horas - 8 
        if horasext > 2 and horasext < 4: 
            salariofinal += horasext * salario * 0.20
        elif horasext >= 4:
            salariofinal += horasext * salario * .30
    else: 
        salariofinal = salario 

#saída, salário final do funcionário
    print(f"Salário final = {salariofinal}")
    contador += 1