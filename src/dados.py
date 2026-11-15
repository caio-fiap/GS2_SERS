# carrega as premissas do csv

import csv
from pathlib import Path

CSV_PATH = Path(__file__).resolve().parent.parent / "dados" / "fontes_premissas.csv"

def carregar_premissas(caminho = CSV_PATH):
    premissas = {}
    with open(caminho, encoding = "utf-8", newline = "") as f:
        for linha in csv.DictReader(f):
            premissas[linha["id"]] = {
                "valor": float(linha["valor"]),
                "unidade": linha["unidade"],
                "fonte": linha["fonte"],
                "estimativa": linha["estimativa"].strip().lower() == "sim",
            }
    return premissas

def valor(premissas, chave):
    return premissas[chave]["valor"]