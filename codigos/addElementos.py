#adicionar elementos no vetor

L=[]
while True:
    n= str(input("Digite um nome (0 sai):"))
    if n == "0":
        break
    L.append(n)
x=0

while x < len(L):
    print(L[x])
    x=x+1