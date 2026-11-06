# Método científico do FPM

[English](METHOD.md)

**A intenção do pesquisador precede as ferramentas e o fluxo de trabalho.** Uma conversa científica pode terminar com uma explicação, amadurecer uma pergunta ou avançar para análise e experimentação; não existe uma sequência universal obrigatória. O Companion auxilia a explicitar hipóteses rivais, métodos e evidências, preservando o julgamento do pesquisador.

## Vocabulário compartilhado mínimo

| Estado | Significado |
|---|---|
| Ideia | Curiosidade, mecanismo ou hipótese ainda exploratória |
| Proposto | Plano ou previsão possível, ainda não executada |
| Escolhido | Direção explicitamente decidida pelo pesquisador |
| Executado | Trabalho realmente realizado com recursos identificáveis |
| Observado | Resultado efetivamente obtido |
| Verificado | Exame delimitado com um critério definido |
| Interpretado | Inferência proporcional às evidências e ao domínio |
| Aceito | Aprovação humana específica para um determinado escopo |

## Julgamento metodológico transferível

As lições abaixo são **generalizações seletivas de práticas metodológicas internas já ratificadas no FPM**. Aplicam-se quando pertinentes; **não são gates automáticos** impostos a toda pergunta.

1. **Pergunta antes da implementação.** Identificar o fenômeno, o objetivo humano, explicações concorrentes, pressupostos, observáveis e a menor previsão capaz de discriminar hipóteses. Um experimento é útil se puder alterar uma decisão científica.
2. **Recuperação antes de recomputação.** Verificar quais artigos, dados, códigos, análises e figuras existem e estão acessíveis. Reanalisar pode ser mais informativo do que simular novamente. Um arquivo inacessível constitui uma lacuna de acesso, não evidência de perda definitiva.
3. **Não misturar dados incompatíveis silenciosamente.** Antes de agrupar resultados, conferir dinâmica/modelo, estimando, denominadores, normalizações, condições iniciais, parâmetros, população, topologia, estrutura de amostragem, dependência e censura, quando aplicáveis. Mostrar curvas juntas não as torna réplicas estatísticas.
4. **Distinguir replay de validação independente.** Reprodução com mesmo código, entradas e sementes testa rastreabilidade. Experimentos estocásticos independentes podem comparar estimandos sob um desenho compatível e incertezas adequadas. Nenhuma modalidade, isoladamente, prova validade geral; mudar sementes também não basta para validá-la.
5. **Incerteza depende da unidade de amostragem.** Identificar se um intervalo descreve trajetórias em grafos fixos, variação entre grafos, participantes, turmas ou outras populações. Respeitar correlação, seleção, pareamento e condicionamento. Zero eventos observados ou intervalos degenerados não demonstram incerteza populacional nula.
6. **Figuras carregam alegações.** Vincular o papel científico da figura aos dados de origem, análise e ativo visual. Distinguir medições, transformações, interpolação e seleção de exemplos. Trajetória ilustrativa não estima frequência populacional; um overlay de imagem não equivale à regeneração integral a partir dos dados.
7. **Revisar argumentos, não apenas palavras.** Preservar terminologia, intenção autoral, comparadores, domínios de validade e força das afirmações. Preferir diagnóstico localizado e correções proporcionais a reescrever tudo. Manter resultados negativos relevantes e discrepâncias abertas.
8. **Verificações têm alcances distintos.** Hash de arquivo, execução de código, replay de análise, reconstrução gráfica, controle científico, revisão semântica, replicação independente e aceite humano sustentam afirmações diferentes. Descrever o alcance real; não transformar QA técnico em certificação científica, nem revisão assistida por IA em parecer independente.
9. **Continuidade com economia de contexto.** Para investigações longas, registrar decisões, evidências, limitações e próximo passo em nota transferível enxuta. Em mudanças pequenas, revisar apenas a superfície materialmente afetada; ampliar a verificação quando houver mudança científica relevante.

**A disciplina importa:** em estudos educacionais, a unidade independente pode ser a turma ou escola, não cada aluno isoladamente; em investigação qualitativa, a evidência pode ser documental, interpretativa ou empírica sem repetições numéricas. Aplicar o princípio epistemológico, e não transportar mecanicamente uma checklist de Monte Carlo para qualquer área.

## Ferramentas e evolução do método

Ferramentas de IA são **meios substituíveis**, disponíveis somente se o ambiente da conversa oferecer acesso real. Um arquivo Markdown não concede acesso a artigos, Python, arquivos privados ou memória automática. Veja a [orientação sobre ferramentas](../starter/TOOLS_AND_CHOICES.md), a [revisão crítica](../starter/REVIEW.md) e a [nota de continuidade](../starter/NOTEBOOK.md).

Este guia público é uma **projeção seletiva e acessível** do método do FPM, não uma cópia de suas regras completas de governança, dados privados ou registros brutos de missão. Um aprendizado interno aceito deve ser examinado quanto a generalidade, evidência, permissões e utilidade para o pesquisador; a atualização pública é preparada como mudança incremental, revisada e autorizada antes de publicada. Isso **não constitui sincronização automática**. Recomendações surgidas no público não se tornam decisões canônicas internas sem o devido aceite.

O [Ising 2D](../examples/ising2d/README.pt-BR.md) é um exemplo didático. O projeto separado [Quarantine Games](https://github.com/AmaralMA42/quarantine_games_network) ilustra uma investigação científica longa, mas nenhum dos dois representa demonstração independente da eficácia comparativa do Companion.
