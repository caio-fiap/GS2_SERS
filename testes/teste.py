import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from energia import consumo_mes, custo_mensal, payback_mes, co2_kg
from assistente import entradas, responder


def teste_consumo():
    assert abs(consumo_mes(5500, 2/3, 30) - 110) < 0.01

def teste_custo_co2_payback():
    assert custo_mensal(100, 0.9) == 90
    assert abs(co2_kg(100, 0.06) - 6) < 1e-9
    assert payback_mes(5000, 100) == 50
    assert payback_mes(5000, 0) is None

def teste_extracao():
    e = entradas("Chuveiro de 5500 W, 4 pessoas, 10 min cada, tarifa R$ 0,85/kWh")
    assert e == {"potencia_w": 5500.0, "pessoas": 4, "min_banho": 10.0, "tarifa": 0.85}

def teste_limitacoes_fontes():
    r = responder("chuveiro de 5500 W")
    assert "estimativas" in r and "Fontes" in r

if __name__ == "__main__":
    for n, f in list(globals().items()):
        if n.startswith("teste_"):
            f(); print("ok", n)
