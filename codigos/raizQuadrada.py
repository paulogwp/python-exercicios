# Exercício 5.25 Escreva um programa que calcule a raiz quadrada de um número.
# Utilize o método de Newton para obter um resultado aproximado. Sendo n o número 
# a obter a raiz quadrada, considere a base b=2. Calcule p usando a fórmula
# p=(b+(n/b))/2. Agora, calcule o quadrado de p. A cada passo, faça b=p e recalcule
# p usando a fórmula apresentada. Pare quando a diferença absoluta entre n e o
# quadrado de p for menor que 0,0001.


while True:
    n = int(input("Digite um número (0 para sair): "))
    if n == 0:
        break
    flag = True
    
    def raizQuadrada(n): #método de Newton
        if n == 1:
            return n
        else:
            b = 2
            p = (b + n / b) / 2
            b = p
        while abs(n - p**2) > 0.00001:
           p = (b + n / b) / 2
           b = p
        return p
    
    if n < 0:
        print("Número inválido.")
    else:
        print(f"A raiz quadrada de {n} é {raizQuadrada(n):.2f}")