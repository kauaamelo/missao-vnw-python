# Missão 7: Organizando a Lista📋
# Os números estão misturados e precisam ser organizados!
# Para resolver isso, você deve pegar os seguintes números: 8, 3, 10, 1 e 5,
# armazená-los em uma lista e depois exibi-los em ordem crescente.
# Isso ajudará a colocar tudo em ordem corretamente!

# 1
numeros = [8, 3, 10, 1, 5]
ordenada = sorted(numeros)
print(f"Primeira lista: {ordenada} \n")

# 2

numeros = [23, 6, 2, 11, 50] 
quantidade = len(numeros)

for contador in range(quantidade):  
    for vizinhos in range(0, quantidade - contador - 1):  
        if numeros[vizinhos] > numeros[vizinhos + 1]:
            numeros[vizinhos], numeros[vizinhos + 1] = numeros[vizinhos + 1], numeros[vizinhos]
print(f"Segunda lista: {numeros}")