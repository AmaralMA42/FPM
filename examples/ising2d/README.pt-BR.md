# Ising 2D — de uma pergunta a um experimento

**Objetivo:** mostrar uma investigação simples: como a ordem magnética de spins numa rede quadrada responde ao aquecimento? O interesse do FPM é também o **processo de escolher as medições**, não apenas gerar código.

## Uma conversa possível

Comece com *“Quero visualizar e medir quando uma rede de spins perde a ordem.”* O Companion pode sugerir o Ising ferromagnético 2D, visualização de configurações e medição de magnetização; depois pode explicar por que comparar tamanhos, controles e resultados analíticos é útil. Um pesquisador experiente pode ir diretamente a autocorrelações e cumulante de Binder, sem uma introdução obrigatória. Veja [exemplos editoriais](EXAMPLE_CONVERSATIONS.md); não são transcrições de usuários reais.

## O modelo e a referência física

Na rede quadrada periódica, cada spin assume `s_i ∈ {−1,+1}`. Com `J=k_B=1`, sem campo:

`H = − J Σ_{<i,j>} s_i s_j`.

A transição exata **no limite termodinâmico** ocorre em `T_c = 2 / ln(1+√2) ≃ 2,269185`. Sistemas finitos apresentam resposta arredondada e flutuações; os gráficos rápidos **não são estimativas precisas de T_c**.

## Como usar o laboratório opcional

É necessário Python, NumPy e Matplotlib. No diretório `examples/ising2d`:

```bash
python -m pip install -r requirements.txt
python -m unittest discover -p 'test_*.py' -v
python ising2d.py --profile quick --out ising_results
```

O programa usa Metropolis com atualização **checkerboard alternada**, condições periódicas, `L` par, e exporta CSV, imagens e `metadata.json`. No perfil rápido: `L=8,16,24`, seis temperaturas, três réplicas por condição e um protocolo curto; ele **não** fundamenta extrapolação de tamanho infinito. Um modo `study` mais longo existe, mas não é necessário para experimentar o Companion.

As [saídas ilustrativas incluídas](sample/README.md) são uma execução local anterior, identificada por metadados; usar o perfil `quick` no próprio computador é opcional. Sem Python, o Companion ainda pode discutir desenho e interpretação, mas não deve dizer que executou a simulação.

## Leituras adequadas dos observáveis

- `m_abs`: média da magnitude da magnetização por spin; ajuda a evitar cancelamento de sinais em volume finito.
- `energy`: energia por spin.
- `chi_connected`: susceptibilidade por flutuações com magnetização assinada; pode ser sensível a reversões de sinal.
- `chi_abs`: **proxy modificada** baseada em `|m|`, não a suscetibilidade termodinâmica estrita.
- `binder`: cumulante de Binder; um estudo de cruzamentos exige termalização, controle de autocorrelação e amostras adequadas.

Há oito testes unitários do código, incluindo casos limites e comparação estatística delimitada com enumeração exata de 4×4. Esses testes **não** certificam a física de todas as campanhas, nem fornecem estimativas de incerteza rigorosas para a região crítica.

O exemplo Ising é independente do [código e dados de Quarantine Games](https://github.com/AmaralMA42/quarantine_games_network). O artigo é um caso de pesquisa mais longo, não um requisito para usar o Companion.
