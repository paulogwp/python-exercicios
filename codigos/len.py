L=[1,2,3,4] #posso alterar o tamanho do vetor e o programa continuara funcionando
x=0
while x < len(L): 
    print(L[x])
    x+=1

L.append(5) #adiciona um elemento no final da lista
print(L[4]) 