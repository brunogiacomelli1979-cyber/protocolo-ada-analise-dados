# Protocolo ADA - Análise de Dados Assistida por IA

Este projeto define a estrutura inicial do **Protocolo ADA**, um agente assistivo para apoiar projetos de análise de dados com Python e Power BI.

Neste momento, o projeto contém apenas pastas, documentos base e scripts iniciais. Ele não analisa dados, não transforma bases, não inventa métricas e não gera dashboards.

## Objetivo do projeto

Criar uma base organizada, simples e profissional para conduzir projetos de análise de dados com apoio de IA, mantendo controle humano sobre decisões sensíveis, preservando os dados brutos e documentando cada etapa relevante.

## O que é o Protocolo ADA

O Protocolo ADA - Análise de Dados Assistida por IA - é uma metodologia de trabalho para orientar projetos de dados de forma assistida, auditável e segura.

O protocolo organiza o trabalho em etapas:

- planejamento analítico;
- avaliação de privacidade e risco;
- inspeção e preparação dos dados;
- definição validada de métricas;
- análise;
- visualização;
- documentação;
- revisão e melhoria contínua.

## Papel da IA

A IA atua como apoio para organizar raciocínios, sugerir caminhos, revisar documentação, identificar possíveis riscos e ajudar na estruturação do projeto.

A IA não deve aplicar alterações críticas de forma autônoma. Antes de qualquer decisão sensível, o agente deve apresentar:

- problema identificado;
- proposta de ação;
- impacto esperado;
- exemplo de antes e depois, quando aplicável;
- pedido explícito de aprovação humana.

## Papel da validação humana

A validação humana é obrigatória para decisões sensíveis, incluindo:

- exclusão ou alteração relevante de dados;
- tratamento de valores ausentes ou inconsistentes;
- definição de métricas e KPIs;
- interpretação de resultados;
- publicação de relatórios e dashboards;
- qualquer decisão que possa afetar pessoas, áreas de negócio ou conformidade.

## Papel do Python

O Python será usado para inspeção, tratamento, padronização, validação e preparação dos dados antes da etapa de visualização.

Os dados brutos devem ser preservados e nunca alterados diretamente. Qualquer base tratada deve ser gerada em pastas separadas, com documentação das transformações aplicadas.

## Papel do Power BI

O Power BI será usado apenas para visualização, storytelling e análise interativa.

O tratamento principal dos dados deve acontecer antes do Power BI, preferencialmente em Python, para manter rastreabilidade, reprodutibilidade e melhor controle de qualidade.

## Relatórios

Relatórios gerados por scripts devem ficar na pasta `relatorios/`. Essa pasta é versionável para manter a estrutura do projeto, mas arquivos temporários ou de trabalho devem continuar fora do versionamento.

## Documentação pública do agente

O documento `documentos/visao_geral_agente_ada.md` apresenta uma visão geral pública do Agente ADA, sem revelar prompts internos, regras privadas ou templates sensíveis.

## Privacidade e LGPD

O projeto deve respeitar princípios de privacidade, minimização de dados e conformidade com a LGPD.

Dados sensíveis, dados pessoais, arquivos brutos, instruções privadas do agente e materiais internos não devem ser publicados em repositórios públicos.

## Público e privado

Conteúdo público esperado:

- estrutura do projeto;
- documentos metodológicos sem dados sensíveis;
- scripts base sem informações confidenciais;
- relatórios públicos aprovados, quando não contiverem dados sensíveis;
- exemplos anonimizados, quando existirem e forem aprovados.

Conteúdo privado:

- dados brutos;
- dados tratados ou finais com informações sensíveis;
- prompts internos;
- regras detalhadas de decisão;
- templates sensíveis do agente;
- arquivos Power BI com dados reais, quando aplicável.
