# Justificativas das recomendações
**Por que recomendar B primeiro:** custo zero, economia imediata, sem obra nem dependência de imóvel próprio.
**Por que avaliar C:** única alternativa renovável, reduz a energia comprada da rede. Só compensa se o payback ficar abaixo da vida útil do equipamento.

## Custos
Ver `analise/comparacao.py`: custo total em 10 anos de cada alternativa.
## Viabilidade
- B: depende de comportamento. - C: imóvel próprio, telhado, orientação solar, obra.
## Impactos ambientais
Cálculo de CO₂ com fator do SIN (MCTI). Como a matriz elétrica brasileira é composta principalmente por fontes renováveis (energia hídrica representa mais de 50% da geração do país, seguida por eólica), a redução de emissão não é tão evidente. 
## Sensibilidade
O payback do solar varia bastante com a tarifa e a fração solar. Tratar como faixa, não como valor único.
