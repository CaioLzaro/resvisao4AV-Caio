n = input("Digite números para adcionar à função:")
n1 = n.split()
n2 = list(map(int,n1))

def maior(lista):
    return max(lista)

print("lista de número:", n2)
print("maior número da lista:", maior(n2))
