alturas = []
generos = []

for i in range(5):

    print("\nPessoas", )

    generos.append(input(f"Digite o genero da pessoa M/F {i + 1}: ", ))
    alturas.append(float(input(f"Digite a altura da pessoa {i+1}: ", )))

maior_altura = max(alturas)
menor_altura = min(alturas)

soma = 0
contador = 0

for i in range(5):

    if generos[i] == "M":
        soma += alturas[i]
        contador += 1

if contador > 0:
    media = soma / contador
else:
    media = 0

quantidade_feminino = generos.count("F")

print("\nResultados Finais")
print("Maior Altura:", maior_altura)
print("Menor Altura:", menor_altura)
print("Média Masculino:", media)
print("Quantidade de Mulhers:", quantidade_feminino)