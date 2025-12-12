somatotal = 0
somaimpar = 0
somapar = 0
num = 1

while num != 0:
    num = int(input("Digite aqui um numero: "))
    somatotal += num
    if num % 2 != 0:
        somaimpar += num
    else:  
        somapar += num

print(f"a soma dos numeros e {somatotal}, impares {somaimpar}, pares {somapar}")
