# tabela de comparacao e analise de sensibilidade

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
from dados import carregar_premissas
from recomendador import comparar, sensibilidade

p = carregar_premissas()
r = comparar(p)
print(f"Entradas: {r['entrada']}\n")
print(f"{'Alternativa':28}{'kWh/mes':>9}{'R$/mes':>9}{'Inicial':>9}{'Total 10a':>11}{'CO2 kg':>9}{'Payback':>10}")

for k in "ABC":
    a = r[k]
    pb = "-" if a["payback_mes"] in (None, 0) else f"{a['payback_mes']/12:.1f} a"
    print(f"{a['nome']:28}{a['kwh_mes']:9.0f}{a['custo_mensal']:9.0f}{a['custo_inicial']:9.0f} {a['custo_total_periodo']:11.0f}{a['co2_kg_periodo']:9.0f}{pb:>10}")

print("\nSensibilidade do payback do aquecedor solar (em anos):")
print(f"{'Tarifa':>8}{'Economia':>10}{'Payback':>10}")
for l in sensibilidade(p):
    pb = "-" if l["payback_anos"] is None else f"{l['payback_anos']:.1f}"
    print(f"{l['tarifa']:8.2f}{l['fracao']:10.0%}{pb:>10}")
