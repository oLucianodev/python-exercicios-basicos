somapar = 0
somaimpar = 0
soma = 0 
for i in range(0,101):
    soma += i
    if (i %2 ==0):
        somapar+=i
    else:
        somaimpar+=i
print(soma)
print(somapar)
print(somaimpar)
