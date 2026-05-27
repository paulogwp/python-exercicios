#calcular número primo

n = int(input("Digite um número: "))

def numeroPrimo(n):
    i = 1
    qtd = 0
    if n <= 1:
        return False
    while i <= n :
        if n % i == 0:
            qtd += 1
        i += 1
    if (qtd > 2):
        return False
    return True

if numeroPrimo(n):
    print(f"{n} é um número primo.")
else:    
    print(f"{n} não é um número primo.")