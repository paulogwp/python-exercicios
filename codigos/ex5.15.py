# Exercício 5.15 Escreva um programa para controlar uma pequena máquina registradora. 
# Você deve solicitar ao usuário que digite o código do produto e a quantidade
# comprada.Seu programa deve exibir o total das compras depois que o usuário digitar 0.
# Qualquer outro código deve gerar a mensagem de erro “Código inválido”.

total = 0
while True:
    c = int(input("Digite o codigo do produto (0 para sair): "))
    if c == 0:
        break
    qtd = int(input("Digite a quantidade comprada: "))
    match c:
        case 1:
            valor = 0.5 * qtd
        case 2:            
            valor = 1.0 * qtd
        case 3:
            valor = 4.0 * qtd
        case 5:
            valor = 7.0 * qtd
        case 9:
            valor = 8.0 * qtd
        case _:
            print("Codigo invalido")
    total += valor
            
# print com o f dentro é para colocar uma variavel dentro
print(f"Valor a pagar: R$ {total:.2f}")