# Daniel Debastiani - Desafio 01

BOLD = '\033[1m'
RESET = '\033[0m'

# Requisição de numero + verificação se é inteiro
while True:
    try:
        num = int(input("Digite um número inteiro: "))
        break
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

#loop para verificar se i numero esta na sequencia de Fibonacci
i=0
prox = 0
seq = [0, 1]

while num >= prox:
    prox = seq[i] + seq[i+1]
    seq.append(prox) # .append() insere a variavel prox na lista.
    i+=1
    if num == 0 or num == 1 or num == prox:
        print(f"\nO numero {BOLD}{num} ESTÁ{RESET} na sequencia de Fibonacci!\nNumeros anteriores {seq[-3:-1]}")
        break
else:
    print(f"\nO número {BOLD}{num} NÃO{RESET} está na sequência de Fibonacci!\nNumeros proximos {seq[-2:-1]}, {BOLD}{num}{RESET}, {seq[-1:]}")