entrada = input().split(" ")

distancia = int(entrada[0])
diametro1 = int(entrada[1])
diametro2 = int(entrada[2])

imc = distancia / (diametro1 + diametro2)

print(f"O valor do IMC: {imc:.2f}")
# print(entrada)
