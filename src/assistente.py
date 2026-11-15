# compara alternativas para o mesmo uso e mesmo periodo

import energia
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
    kwh_base = consumo_kwh_mes(potencia_w, horas_dia, dias)

    # B - reduzir tempo de banho
    meta = min(valor(p, "min_banho_meta"), min_banho)
    kwh_b = consumo_kwh_mes(potencia_w, pessoas * meta / 60, dias)

    # C - aquecedor solar cobre uma parte do consumo
    kwh_c = kwh_base * (1 - fracao_solar)
    inicial_c = valor(p, "solar_custo_inicial")
    manut_mes = valor(p, "solar_manutencao_ano") / 12