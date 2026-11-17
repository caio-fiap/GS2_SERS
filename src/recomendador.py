# compara alternativas para o mesmo uso e mesmo periodo

from energia import consumo_mes, custo_mensal, co2_kg, payback_mes
from dados import valor

def comparar(p, potencia_w = None, pessoas = None, min_banho = None, tarifa = None, fracao_solar = None):
    # retorna dicionario com alternativas A (base), B (melhor) e C (solar)
    potencia_w = potencia_w or valor(p, "potencia_chuveiro")
    pessoas = pessoas or valor(p, "pessoas_padrao")
    min_banho = min_banho or valor(p, "min_banho_padrao")
    tarifa = tarifa or valor(p, "tarifa_kwh")
    fracao_solar = fracao_solar if fracao_solar is not None else valor(p, "solar_fracao_economia")
    dias = valor(p, "dias_mes")
    anos = valor(p, "periodo_ref")
    fator = valor(p, "fator_co2")
    meses = anos * 12

    horas_dia = pessoas * min_banho / 60
    kwh_base = consumo_mes(potencia_w, horas_dia, dias)

    # B - reduzir tempo de banho
    meta = min(valor(p, "min_banho_meta"), min_banho)
    kwh_b = consumo_mes(potencia_w, pessoas * meta / 60, dias)

    # C - aquecedor solar cobre uma parte do consumo
    kwh_c = kwh_base * (1 - fracao_solar)
    inicial_c = valor(p, "solar_custo_inicial")
    manut_mes = valor(p, "solar_manutencao_ano") / 12

    def alt(nome, kwh, inicial = 0.0, manut = 0.0):
        mensal = custo_mensal(kwh, tarifa) + manut
        return{
            "nome": nome,
            "kwh_mes": kwh,
            "custo_mensal": mensal,
            "custo_inicial": inicial,
            "custo_total_periodo": inicial + mensal * meses,
            "co2_kg_periodo": co2_kg(kwh * meses, fator),
        }

    a = alt("A) Situação atual", kwh_base)
    b = alt("B) Reduzir tempo de banho", kwh_b)
    c = alt("C) Aquecedor solar", kwh_c, inicial_c, manut_mes)
    for x in (b, c):
        x["economia_mensal"] = a["custo_mensal"] - x["custo_mensal"]
        x["economia_periodo"] = a["custo_total_periodo"] - x["custo_total_periodo"]
        x["co2_evitado"] = a["co2_kg_periodo"] - x["co2_kg_periodo"]
        x["payback_mes"] = payback_mes(x["custo_inicial"], x["economia_mensal"]) if x["custo_inicial"] else 0
    a["economia_mensal"] = a["economia_periodo"] = a["co2_evitado"] = 0.0
    a["payback_mes"] = None

    return{
        "entrada": {
            "potencia_w": potencia_w,
            "pessoas": pessoas,
            "min_banho": min_banho,
            "tarifa": tarifa,
            "anos": anos,
            "fracao_solar": fracao_solar,
            "meta_min": meta
        },
        "A": a, "B": b, "C": c,
    }

def sensibilidade(p, **kw):
    # Payback do solar
    base_tarifa = kw.get("tarifa") or valor(p, "tarifa_kwh")
    linhas = []
    for f_t in (0.8, 1.0, 1.2):
        for fr in (0.5, 0.7, 0.8):
            kw2 = dict(kw, tarifa=base_tarifa * f_t, fracao_solar=fr)
            r = comparar(p, **kw2)
            linhas.append({"tarifa": base_tarifa * f_t, "fracao": fr, "payback_anos": (r["C"]["payback_mes"] / 12) if r["C"]["payback_mes"] else None})
    return linhas


def avisos_estimativa(p):
    # premissas marcadas como estimativa
    return [k for k, v in p.items() if v["estimativa"]]