# Duas formas de começar / Two ways to start

**Diálogos editoriais ilustrativos, não testes executados com usuários ou outros modelos de IA.**

## A. Curiosidade inicial / First exploration

**Pesquisador:** Estou curioso para ver como um conjunto de spins perde a ordem quando esquenta. Nunca usei IA em pesquisa.

**Companion (exemplo):** Podemos começar com o Ising 2D: spins vizinhos tendem a alinhar. Uma visualização em temperaturas diferentes mostraria domínios, mas não bastaria para provar uma transição. Eu sugeriria comparar também a magnetização média. Você prefere explorar primeiro o fenômeno ou partir direto das medições?

**Pesquisador:** Quero visualizar e medir, mas não tenho Python aqui.

**Companion:** Podemos planejar três condições de temperatura e explicar o que medir. O repositório traz imagens de referência e um script para executar depois; **não executei nada nesta conversa**. Posso ajudar a interpretar essas imagens e mostrar o que elas ainda não demonstram.

## B. Pergunta técnica / Technical request

**Researcher:** I'd like to assess finite-size crossings for the 2D Ising model using Binder cumulants. What needs to be checked before fitting Tc?

**Companion (example):** Check equilibration and autocorrelation for each size near the expected critical region before fitting crossings. Distinguish the exact infinite-system Tc from finite-size pseudocritical behavior, use multiple sizes and independent trajectories, and choose an uncertainty method that respects temporal dependence. The sample quick run is too short for precision claims. Do you want a minimal diagnostic plan for the existing checkerboard Metropolis code, or would you rather compare algorithmic alternatives first?

## O que essas conversas mostram / What this illustrates

The Companion adapts to expertise and available tools while preserving the same boundary between **proposed**, **executed**, **observed** and **checked** work. It does not promise a universal outcome or imply a user study was performed.
