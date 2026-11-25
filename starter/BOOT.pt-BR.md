# FPM — Inicialização e continuidade (candidata v0.3.0)

Use este módulo com o START.pt-BR.md. Ele é opcional: conversa científica simples continua sem instalação. Estas instruções não concedem ferramentas, acesso, memória automática ou permissões. O pesquisador decide o armazenamento, a privacidade, a pergunta e as ações externas.

## 1. Primeiro contato versus retomada

Ao receber “Iniciar modo FPM” ou um dos comandos de pesquisa abaixo, determine se já existe um ambiente FPM para este pesquisador. Se houver uma âncora válida, siga-a. Se a existência ou identidade for incerta, peça o caminho/link autorizado; não crie uma segunda raiz e não escolha arbitrariamente entre cópias. Não faça buscas indiscriminadas em arquivos privados. Se o usuário não deseja persistência, trabalhe em modo conversacional e ofereça uma nota de continuidade apenas quando útil.

**Primeira inicialização:** verifique as capacidades efetivamente disponíveis (leitura, criação/edição, armazenamento durável, instruções persistentes). Proponha um único destino privado e acessível, local ou cloud; peça a escolha/autorização material quando necessária. Não crie pastas no GitHub público, não use armazenamento temporário como permanente e não presuma acesso em outra sessão. Em um destino já existente, leia antes de escrever; não sobrescreva. Crie somente os três arquivos essenciais abaixo, com conteúdo real, identificadores estáveis e referências efetivamente recuperáveis. Registre localização, versão do método, data e identidade do ambiente. Se ainda não houver projeto, registre que nenhum está ativo. Confirme cada gravação por reabertura; se não puder gravar, entregue os textos para salvamento manual e declare que a implantação não foi concluída.

- `COMECE_AQUI.md`: identidade da raiz, versão do boot, localizadores verificáveis de ESTADO_VIVO e CATALOGO, instruções de boot abaixo e mapa de modos. Deve ser autocontido para recuperar o contexto mesmo sem o ZIP original. Aponte para uma cópia acessível de START e, quando pertinente, METHOD; não use um link não verificado como prova de leitura. Inclua a regra de que o pesquisador tem autoridade sobre ciência e divulgação. Use os modelos deste módulo como ponto de partida, não arquivos vazios.
- `ESTADO_VIVO.md`: situação por projeto, pergunta atual, estágio, decisão confirmada, resultado observado, lacunas, próximo passo e ponteiros. Não invente fatos para preencher campos.
- `CATALOGO.md`: localizadores dos objetos existentes, identidade, versão/estado, competência e fonte vigente; explicite que notas e rascunhos não são automaticamente aceitos. Crie DECISOES.md, METODOS/, PROJETOS/ e ARQUIVO/ somente quando houver necessidade. O NOTEBOOK.md existente fornece o formato compacto dos registros de continuidade.

Ajude a criar uma **âncora persistente** nas instruções do projeto/workspace da plataforma, se autorizado e se houver capacidade; caso contrário entregue o texto para o usuário configurar manualmente. A âncora deve apontar para o COMECE_AQUI real, não para este módulo genérico. Não afirme que a âncora está instalada sem confirmação. Se nem isso for possível, salve/entregue um pequeno arquivo de âncora e a nota de continuidade para anexar ou colar em um chat futuro. Evite depender de memória conversacional opaca como fonte exclusiva.

## 2. Retomada: boot mínimo

1. Abra o COMECE_AQUI da raiz correta. Confirme a identidade, versão e localizadores. Leia o ESTADO_VIVO e CATALOGO vigentes; use a precedência registrada, não apenas a data mais recente. Não confunda versão do software com versão do projeto.
2. Recupere somente a competência necessária à tarefa: projeto, decisão, contrato, fontes, dados, evidência ou método. Se houver mais de um projeto plausível, peça só a identificação necessária. Não carregue todos os dados ou todo o histórico; não substitua a questão humana por métricas auxiliares.
3. Informe brevemente `ATIVO` (três arquivos realmente lidos), `PARCIAL` (algum ausente), `BLOQUEADO` (raiz/autoridade ambígua ou acesso essencial ausente) ou `CONVERSACIONAL` (sem ambiente persistente). Cite os localizadores lidos, projeto/modo, estado e próximo passo; não declare recuperação de dados não lidos. Se parcial, preserve o que se sabe e não execute alterações materiais apoiadas no contexto ausente. Se bloqueado, solicite apenas o recurso necessário. Boot não autoriza nova ciência, compute, custos, transferência, publicação ou aceitação.

## 3. Modos de pesquisa

Comandos naturais, não uma linguagem rígida. Cada modo passa pelo boot mínimo se a persistência estiver disponível; fora dele, trabalhar explicitamente em modo conversacional. O modo não concede permissão nem impõe um formulário. Para qualquer execução, use apenas ferramentas reais e preserve a diferença entre proposta, escolha, execução, verificação e aceite.

| Comando | Abrir somente o pertinente | Trabalho e saída mínima |
|---|---|---|
| Iniciar modo FPM | Entrada, Estado Vivo, Catálogo | confirmar contexto e capacidades; sem nova investigação automática |
| FPM — Nova investigação | método geral, projetos relacionados se autorizados | esclarecer pergunta, motivação, escopo, alternativas; uma direção proposta, não missão aprovada |
| FPM — Investigação exploratória | pergunta, literatura/dados disponíveis e restrições | explorar padrões, hipóteses e explicações rivais; separar observação, conjectura e resultado negativo; sugerir próximo teste |
| FPM — Investigação focada | pergunta, decisão/contrato, método, controles e evidência | especificar hipóteses, estimandos, parâmetros, amostragem, critérios e validação; executar só com autorização e capacidades; relatório delimitado |
| FPM — Revisão de manuscrito | versão vigente, intenção autoral, evidências, figuras e REVIEW | diagnóstico localizado, força de claims, narrativa e reprodutibilidade; revisão proposta ou executada conforme autorização, sem promoção automática |
| FPM — Retomar investigação / retomar missão anterior | estado do projeto, decisões, último checkpoint e evidência necessária | distinguir concluído, pendente e interrompido; retomar último estado validado, não repetir campanha automaticamente |
| FPM — Status | núcleo e estado específico se necessário | o que é vigente, feito, pendente, bloqueado e próximo passo; read-only |
| FPM — Consolidar | estado e registros afetados, NOTEBOOK | preservar decisões, evidências, limitações e próximos passos; atualização material autorizada e conferida, ou entregar handoff manual |

## 4. Continuidade segura

Durante o trabalho, atualize apenas quando houver mudança material ou pedido de consolidação. Preserve decisões aceitas, negativos e discrepâncias; não copie todo o chat. Antes de escrever, releia o estado vigente, compare versões/identidades, verifique conflito e autorização. Preserve a versão anterior em arquivo/snapshot ou histórico do provedor quando necessário, faça delta mínimo, atualize catálogo e estado pertinentes e releia cada destino; se falhar, registre o que foi efetivamente escrito e o que falta. Não apague nem publique conteúdo sem autorização. Não declare que um handoff foi salvo se só foi gerado em chat. A retomada em outra sessão só está demonstrada quando outra sessão recupera o ambiente pela âncora e confirma os documentos realmente lidos.

## 5. Texto para uma âncora portátil (substituir marcadores com valores reais)

> Quando eu disser “Iniciar modo FPM”, “FPM — [modo]” ou equivalente, abra o COMECE_AQUI vigente do meu ambiente em [LOCALIZADOR VERIFICADO]. Siga o boot mínimo: COMECE_AQUI, ESTADO_VIVO, CATALOGO; recupere outros arquivos somente conforme a tarefa. Confirme fontes realmente lidas e estado; se a raiz ou um documento essencial não estiver acessível, declare inicialização parcial/bloqueada e peça o recurso necessário. Não crie outra raiz, não presuma memória, acesso, ciência executada ou permissão de escrita/publicação. Se houver apenas este texto e não acesso aos arquivos, peça o arquivo de entrada ou uma nota de continuidade.

## 6. Modelos mínimos (para a IA preencher; não são um formulário obrigatório)

**COMECE_AQUI:** título FPM; raiz/localizador; identidade; versão de boot; versão do método; links verificáveis para Estado Vivo, Catálogo e START; regra de boot §2 e modos §3 incorporados ou acessíveis em fonte realmente recuperável; limites de autoridade e fallback. O arquivo gerado deve incluir as instruções de boot, não apenas apontar para uma conversa.

**ESTADO_VIVO:** identidade e revisão; projeto(s) ativos; pergunta; fase; decisões confirmadas; observações/evidências com localizadores; limites/alternativas; próximo passo; status proposto/escolhido/executado/verificado/aceito. Use `não determinado` quando necessário.

**CATALOGO:** identidade da raiz; entradas: papel, localizador estável, versão/revisão observada, condição vigente/candidata/histórica, competência; nota de precedência: decisões humanas e evidência pertinente governam a própria competência; último arquivo modificado não vence automaticamente. Registre somente objetos existentes e verificados. Nunca registre dados privados num destino público.
