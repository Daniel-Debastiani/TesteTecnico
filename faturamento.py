import json

file = open('files/dados.json', 'r')
dados = json.load(file)

BOLD = '\033[1m'
RESET = '\033[0m'

maiorValor = None
menorValor = None
acimaDaMedia = []
somaFaturamento = 0
diasFaturamento = 0

# Descobre o maior e o menor faturamento 
for relatorio in dados:
    valorAtual = relatorio["valor"]
    if valorAtual != 0:
        if maiorValor == None or valorAtual > maiorValor["valor"]:
            maiorValor = relatorio
        if menorValor == None or valorAtual < menorValor["valor"]:
            menorValor = relatorio
        somaFaturamento += valorAtual
        diasFaturamento += 1

# calcula a média e ve quem está acima dela
mediaFaturamento = somaFaturamento/diasFaturamento
for relatorio in dados:
    if relatorio["valor"] > mediaFaturamento:
        acimaDaMedia.append(relatorio)

# Mostra o resultado
print(f"A {BOLD}MÉDIA{RESET} de faturamento foi de {BOLD}RS: {mediaFaturamento:.2f}{RESET}")
print(f"O {BOLD}MAIOR{RESET} faturamento foi no dia {BOLD}{maiorValor["dia"]} RS: {maiorValor["valor"]:.2f}{RESET}")
print(f"O {BOLD}MENOR{RESET} faturamento foi no dia {BOLD}{menorValor["dia"]} RS: {menorValor["valor"]:.2f}{RESET}")
print(f"\nExistem {len(acimaDaMedia)} dia(s) acima da média, são eles:")
print("[")
for relatorio in acimaDaMedia:
    print(f"    {{ 'dia': {relatorio['dia']}, 'valor': {relatorio['valor']:.2f} }},")
print("]")