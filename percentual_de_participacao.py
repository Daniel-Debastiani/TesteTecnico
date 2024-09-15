relatorios = [
    {"estado": "SP", "faturamento": 67836.43},
    {"estado": "RJ", "faturamento": 36678.66},
    {"estado": "MG", "faturamento": 29229.88},
    {"estado": "ES", "faturamento": 27165.48},
    {"estado": "Outros", "faturamento": 19849.53}
]

faturamento_total = sum([relatorio["faturamento"] for relatorio in relatorios])
# faturamento_total = 0
# for relatorio in relatorios:
#     faturamento_total += relatorio["faturamento"]

for relatorio in relatorios:
    relatorio["percentual"] = (relatorio["faturamento"]/faturamento_total)*100

print("[")
for relatorio in relatorios:
    print(f"    {{ 'estado': '{relatorio['estado']}', 'faturamento': {relatorio['faturamento']}, 'percentual': {relatorio['percentual']:.0f}% }},")
print("]")

