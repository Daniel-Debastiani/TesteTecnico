palavra = input("Digite uma palavra: ")

# inverte a palavra
inverso = ""
for letra in range(len(palavra) -1, -1, -1):
    inverso += palavra[letra]

if inverso == palavra:
    print ("\nUau! Essa palavra é um palíndromo! Mesmo sendo invertida ela continua a mesma!")
else:
    print(f"\nEsse é o inverso da sua palavra: {inverso}")


# usando slice
# inverso = palavra[::-1] 