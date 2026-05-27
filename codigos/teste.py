i = 0
soma = 0

while True:
    n = int(input("Digite um número: "))
    if n == 0:
        break
    i += 1
    soma += n

print(f"Quantidade de números digitados: {i}")
print(f"Soma: {soma}")
print(f"Media aritmética: {soma/i}")