# Global Solution 2  
## Citizen Assist AI - Soluções em Energias Renováveis e Sustentáveis

**Integrantes:**
* Caio Marinho Pereira - RM: 572873

## Público e Problema
**Público:** [??]  
**Necessidade energética:** [??]  
**Como o assistente ajuda:** O usuário descreve seu uso energético e recebe: consumo estimado, comparação de alternativas e fontes, e limitações.  

## Funcionalidades
1. Cálculo de consumo (kWh/mês), custo (R$/mês) e emissões (kg CO₂).
2. Comparação para o mesmo uso e mesmo período.
3. Payback, economia acumulada, CO2 evitado e análise de sensibilidade.
4. Resposta com premissas, limitações e fontes. Valores não informados pelo usuário são avisados.
5. ```montar_prompt_llm()```: LLM que explica os números calculados pelo código, apenas.

## Execução
Requerimento: Python 3.8
```bash
python src/assistente.py "5500 W, 4 pessoas, 10 min cada, tarifa R$ 0,90/kWh" # exemplo de descrição de uso
python analise/comparacao.py # tabela comparativa e sensibilidade
python tests/test_energia.py # testes dos cálculos
```

## Estrutura do Projeto
```

```

## Fórimulas

* Energia (kWh/mês) = potência (W) * horas/dia * dias
* Custo (R$/mẽs) = kWh * tarifa (R$/kWh)
* CO2 (kg) = kWh * fator de emissão (kg CO2/kWh)
* Payback (meses) = custo inicial + custo mensal * meses

## Resultados

|Alternativa|kWh/mês|R$/mês|Inicial|Total em x anos|Payback|
|---|---|---|---|---|---|
|A|1|1|1|1|1|
|B|2|2|2|2|2|
|C|3|3|3|3|3|

## Limitações

* Valores são estimativas, não garantias. Variam com tarifa, bandeira tarifária, clima, intalação etc.
* Tarifa e custos foram considerados contantes nos X anos (a definir) (sem reajuste de inflação, por exemplo).

## Referências, justificativas e testes
