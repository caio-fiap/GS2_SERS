# Global Solution 2 - Soluções em Energias Renováveis e Sustentáveis 
## Citizen Assist AI - Análise Energética e Sugestões

**Integrantes:**
* Caio Marinho Pereira - RM: 572873

---

## Público e Problema
- **Público:** Famílias de São Paulo que buscam reduzir o consumo energético durante o banho.  
- **Necessidade energética:** reduzir o gasto com o chuveiro elétrico, geralmente um dos maiores consumidores domésticos.   
- **Como o assistente ajuda:** O usuário descreve seu uso energético e recebe: consumo estimado, comparação de alternativas e fontes, e limitações.  

## Funcionalidades
1. Cálculo de consumo (kWh/mês), custo (R$/mês) e emissões (kg CO₂).
2. Comparação para o mesmo uso e mesmo período.
3. Payback, economia acumulada, CO2 evitado e análise de sensibilidade.
4. Resposta com premissas, limitações e fontes. Valores não informados pelo usuário são avisados.

## Execução
Requerimento: Python 3.8
```bash
python src/assistente.py "5500 W, 4 pessoas, 10 min cada, tarifa R$ 0,90/kWh" # exemplo de descrição de uso
python analise/comparacao.py # tabela comparativa e sensibilidade
```

## Estrutura do Projeto
```
├── src/
│   ├── assistente.py
│   ├── dados.py
│   ├── energia.py
│   └── recomendador.py
├── dados/
│   └── fontes_premissas.csv
├── analise/
│   └── comparacao.py
└── docs
    ├── referencias.md
    └── testes_usuarios.md
```

## Fórimulas

* Energia (kWh/mês) = potência (W) * horas/dia * dias
* Custo (R$/mẽs) = kWh * tarifa (R$/kWh)
* CO2 (kg) = kWh * fator de emissão (kg CO2/kWh)
* Payback (meses) = custo inicial + economia mensal
* Custo total no período = custo inicial + custo mensal * meses

## Resultado padrão

|Alternativa|kWh/mês|R$/mês|Inicial|Total em 10 anos|CO2 kg|Payback|
|--------|---|---|---|---|---|---|
|A) Atual | 90 | 70 | 0 | 8424 | 756 | - |
|B) Banho de 7 min | 63 | 49 | 0 | 5897 | 529 | - |
|C) Aquecedor solar | 27 | 38 | 4500 | 227 | 9027 | ~11.5 anos|

## Limitações
- Valores são estimativas, não garantias. Variam com tarifa, bandeira tarifária, clima, intalação, etc.
- Tarifa e custos foram considerados contantes nos 10 anos (sem reajuste de inflação, por exemplo).
- O aquecedor exige imóvel próprio (ou permissão do proprietário), telhado com sol e investimento inciial.
- O assistente trata apenas do chuveiro elétrico.

## Referências, justificativas e testes
