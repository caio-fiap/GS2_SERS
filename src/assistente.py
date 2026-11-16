# assistente de energia

import re
import sys
from dados import carregar_premissas
from recomendador import comparar

REFERENCIAS = ("ANEEL (tarifas e bandeiras); Procel/Inmetro-PBE (potência e eficiência); MCTI (fator de emissão do SIN)")

def num(txt):
    return float(txt.replace(".", "").replace(",",".")) if "," in txt else float(txt)

def entradas(pergunta):
    #extrair potencia, pessoas, minutos e tarifa
    t = pergunta.lower()
    e = {}
    if m := re.search(r"(\d[\d\.]*)\s*w\b", t):
        e["potencia_w"] = num(m.group(1))
    if m := re.search(r"(\d+)\s*pessoas?", t):
        e["pessoas"] = int(m.group(1))
    if m := re.search(r"(\d+)\s*min", t):
        e["min_banho"] = float(m.group(1))
    if m := re.search(r"r\$\s*(\d+[\.,]?\d*)\s*(?:/|por)?\s*kwh", t):
        e["tarifa"] = num(m.group(1))
    return e

def meses(m):
    return "sem retorno" if m is None else f"{m / 12:.1f} anos"

def responder(pergunta, p = None):
    p = p or carregar_premissas()
    ent = entradas(pergunta)
    r = comparar(p, **ent)
    i, A, B, C = r["entrada"], r["A"], r["B"], r["C"]
    usados_padrao = [k for k in ("potencia_w", "pessoas", "min_banho", "tarifa") if k not in ent]

    linhas = [
        f"Seu consumo estimado com banho: {A['kwh_mes']:.0f} kWh/mes (cerca de R$ {A['custo_mensal']:.0f}/mes).",
        "",
        f"Opcao B - reduzir o banho para {i['meta_min']:.0f} min por pessoa (sem custo): "
        f"economia de ~R$ {B['economia_mensal']:.0f}/mes, ou ~R$ {B['economia_periodo']:.0f} em {i['anos']:.0f} anos.",
        f"Opcao C - aquecedor solar (renovavel): custo inicial estimado R$ {C['custo_inicial']:.0f}; "
        f"economia de ~R$ {C['economia_mensal']:.0f}/mes; retorno em ~{meses(C['payback_mes'])}; "
        f"economia em {i['anos']:.0f} anos de ~R$ {C['economia_periodo']:.0f}.",
        f"CO2 evitado em {i['anos']:.0f} anos: B ~{B['co2_evitado_kg']:.0f} kg; C ~{C['co2_evitado_kg']:.0f} kg "
        "",
        "Recomendacao: comece pela opcao B (custo zero) e avalie a C se voce for dono do imovel, "
        "tiver telhado com sol e puder investir.",
        "",
        "ATENCAO: sao estimativas, nao garantias. Mudam com tarifa, bandeira, clima, dimensionamento e orcamento real.",
    ]
    if usados_padrao:
        linhas.append("Valores padrão usados (você não informou): " + ", ".join(usados_padrao) + ". Informe-os para um resultado mais preciso.")
    linhas.append("Fontes: " + REFERENCIAS)
    return "\n".join(linhas)

if __name__ == "__main__":
    pergunta = " ".join(sys.argv[1:]) or input("Pergunte: ")
    print(responder(pergunta))