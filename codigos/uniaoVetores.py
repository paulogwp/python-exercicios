#codigo para unir dois vetores em um só

L=[]
while True:
    n= int(input("Digite um numero (0 sai):"))
    if n == 0:
        break
    L.append(n)


V = []
print("\n")
while True:
    n= int(input("Digite um numero (0 sai):"))
    if n == 0:
        break
    V.append(n)
x=0

C = []
#C.append(L) Isso pega a lista inteira como um elemento e adiciona em C
#C.append(V)
C = L + V #une os dois vetores em um só 
print(C)