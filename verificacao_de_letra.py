# Daniel Debastiani - Desafio 02

frase = str(input("Digite uma frase aqui: ")).lower() # .lower() Joga a frase para minusculo


print("\nMETODO 01:")
a = 0
for letra in frase: # Passa letra por letra e verifica se é letra "a" ou não.
    if letra == "a":
        a += 1
if a == 0:
    print("Sua frase não contem a letra 'a'. Impressionante!")
else:
    print(f"Sua frase contem {a} letra(s) 'a'.")


print("\nMETODO 02:")
a = frase.count("a")  # .count() Conta quantas vezes "a" aparece
if a == 0:
    print("Sua frase não contém a letra 'a'. Impressionante!")
else:
    print(f"Sua frase contém {a} letra(s) 'a'.")