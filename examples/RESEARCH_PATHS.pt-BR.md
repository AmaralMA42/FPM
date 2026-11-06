# Dois percursos de mediação científica — exemplos editoriais

**Situações ilustrativas criadas para explicar o método.** Não são transcrições de pesquisadores reais, experimentos executados nem estudos de eficácia do FPM. Podem ser discutidas sem código, sem conta externa e sem conhecimento de física estatística. [English](RESEARCH_PATHS.en.md).

## 1. Pesquisadora de ensino com experiência na área, mas pouca prática com IA

**Intenção:** “Dou aulas de Física e gostaria de saber se um jogo ajuda meus estudantes a aprender melhor. Quero fazer uma pesquisa, mas não sei como usar IA nesse planejamento.”

**Uma resposta inadequada seria:** gerar imediatamente um código, um questionário ou um teste estatístico e apresentar isso como protocolo suficiente.

**Como o Companion deve ajudar:**

- **Compreensão:** o objetivo é investigar aprendizagem, não construir um agente ou aprender engenharia de prompts. Diferenciar ganho conceitual, motivação, participação e retenção; perguntar qual deles importa apenas se essa escolha mudar o desenho.
- **Alternativas reais:** estudo piloto de viabilidade, comparação entre intervenções ou análise da literatura. Explicar a diferença de custo e força de inferência, sem escolher causalidade por decreto.
- **Desenho condicional:** se houver comparação, definir unidade independente (estudante, turma, escola), seleção, medidas antes/depois, controles, possíveis contaminações e autorização ética/institucional quando aplicável. Não tratar automaticamente estudantes da mesma turma como observações independentes.
- **Próximo passo:** decidir *qual resultado de aprendizagem pretende estimar* e quais dados/instrumentos já possui; só depois propor o desenho apropriado.

**Limite:** nenhuma melhora pedagógica foi medida; um plano não demonstra efeito causal nem dispensa requisitos éticos locais.

## 2. Pesquisador computacional comparando duas campanhas

**Intenção:** “Tenho duas curvas parecidas obtidas em redes diferentes e quero juntá-las para aumentar a estatística. Será melhor rodar mais pontos?”

**Uma resposta inadequada seria:** concatenar os arquivos CSV, chamar todas as linhas de réplicas independentes e disparar mais simulações.

**Como o Companion deve ajudar:**

- **Recuperação:** primeiro verificar quais dados brutos, parâmetros, código, gráficos e identificadores de grafo estão acessíveis. A ausência de um arquivo na conversa atual não prova que a campanha original se perdeu.
- **Compatibilidade:** comparar dinâmica, inicialização, tamanho de rede, topologia, estimando, normalização, critérios de parada e hierarquia de réplicas por grafo. A semelhança visual não demonstra equivalência estatística.
- **Escolha científica:** curvas podem ser sobrepostas para contraste descritivo, complementar coordenadas medidas ou estimar uma quantidade conjunta — são decisões distintas, com requisitos de evidência distintos.
- **Verificação:** replay exato busca reproduzir uma execução específica; validação estocástica compara estimandos sob desenhos compatíveis. Nem sementes iguais nem sementes diferentes resolvem sozinhas a questão.
- **Próximo passo:** organizar uma tabela mínima de compatibilidade das campanhas e identificar a lacuna que alteraria a conclusão; simular mais apenas se ela persistir.

**Limite:** nenhum CSV foi recebido ou agrupado; não há conclusão de equivalência entre campanhas nem novas simulações.

## O princípio comum

O Companion não substitui o julgamento do pesquisador. Ajuda a reconhecer a pergunta realmente relevante, selecionar uma ação científica informativa e distinguir **orientação, execução e evidência**. Estas vinhetas são um recurso didático, não um benchmark comparativo contra outras IAs.
