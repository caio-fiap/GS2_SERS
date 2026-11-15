# funcoes de calculo de energia

def consumo_mes(potencia_w, horas_dia, dias = 30):
    # Energia (kWh / mes) = Potencia (kW) * horas * dias
    return (potencia / 1000) * horas_dia * dias

def custo_mensal(kwh, tarifa):
    # custo (R$ / mes) = kWh * tarifa (R$/kWh)
    return kwh * tarifa

def co2_kg(kwh, fator):
    # Emissao (kg CO2) = kWh * fator de emissao
    return kwh * kg_por_kwh

def payback_mes(custo_inicial, econimia_mensal):
    # Meses para recuperar um investimento. Se não tiver economia, retorna None
    if economia_mensal <= 0:
        return None
    return custo_inicial / econimia_mensal