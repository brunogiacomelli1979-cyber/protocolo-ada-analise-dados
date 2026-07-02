# Protocolo ADA — Metodologia

## Visão geral

O Protocolo ADA — Análise de Dados Assistida por IA é uma metodologia reutilizável para conduzir projetos de análise de dados com apoio de Python, IA e validação humana.

O protocolo organiza o trabalho em etapas rastreáveis, com separação clara entre exploração, tratamento, validação, definição analítica, especificação de BI e tomada de decisão. Ele pode ser aplicado a diferentes domínios, desde que exista uma base de dados a ser analisada e um compromisso explícito com governança, documentação e revisão humana.

Princípio central:

* Python gera evidências.
* IA interpreta hipóteses.
* Humano valida decisões.

## Objetivo

O objetivo do Protocolo ADA é reduzir improviso em projetos de dados, criando um fluxo claro para:

* entender a base disponível;
* preservar dados originais;
* tratar dados com rastreabilidade;
* validar qualidade e limitações;
* transformar dados em perguntas analíticas;
* preparar modelos para BI;
* registrar decisões humanas;
* manter documentação adequada para portfólio, auditoria e reutilização.

## Princípios fundamentais

* Preservar dados brutos.
* Separar dados brutos, tratados e finais.
* Documentar decisões e limitações.
* Evitar correções automáticas sem regra de negócio.
* Diferenciar evidência, hipótese e decisão.
* Não tratar IA como decisora autônoma.
* Exigir validação humana nos gates críticos.
* Manter reprodutibilidade por scripts e relatórios.
* Proteger dados sensíveis.
* Preparar a análise para uso responsável em BI.

## Papel do Python, da IA e da validação humana

### Python

Python é responsável por gerar evidências técnicas:

* leitura de arquivos;
* inspeção de estrutura;
* contagem de linhas e colunas;
* validação de chaves;
* verificação de nulos;
* identificação de duplicidades;
* padronização controlada;
* criação de arquivos derivados;
* geração de relatórios técnicos.

Python não decide sozinho o significado de anomalias, nulos, outliers ou regras de negócio.

### IA

A IA apoia a interpretação e organização:

* resume evidências;
* propõe hipóteses;
* organiza documentação;
* sugere perguntas analíticas;
* aponta riscos de interpretação;
* auxilia na especificação de métricas e modelos.

A IA não aprova decisões, não substitui especialistas e não deve inventar campos, regras ou conclusões sem base nos dados.

### Validação humana

A validação humana é obrigatória nos pontos de decisão:

* aprovação de tratamentos;
* aceitação de nulos preservados;
* decisão sobre campos sensíveis;
* aprovação de dados finais;
* definição de KPIs;
* validação de modelo BI;
* interpretação de resultados.

## Adaptação da metodologia Google Data Analytics

O Protocolo ADA usa como referência:

Data Discovery → Prepare → Process → Ask → Analyze → Share → Act

Adaptação aplicada:

| Referência | No Protocolo ADA |
| --- | --- |
| Data Discovery | Inspeção inicial da base, dicionário preliminar, riscos e hipóteses. |
| Prepare | Planejamento do tratamento, estrutura de pastas e critérios de qualidade. |
| Process | Padronização, tratamento e criação de dados finais. |
| Ask | Definição de perguntas analíticas e KPIs possíveis. |
| Analyze | Especificação de medidas, regras de agregação e análise. |
| Share | Preparação para BI, dashboard e comunicação. |
| Act | Decisão humana, recomendações e próximos passos. |

## Projeto orientado por problema e por base disponível

### Projeto orientado por problema

Começa com uma pergunta de negócio clara, por exemplo:

* Como reduzir churn?
* Por que a margem caiu?
* Quais clientes têm maior risco?

Nesse caso, os dados são buscados e preparados para responder ao problema.

### Projeto orientado por base disponível

Começa com dados já existentes, mas sem pergunta fechada. O fluxo é:

1. entender a base;
2. validar o que ela permite responder;
3. definir perguntas possíveis;
4. criar métricas com base segura;
5. evitar conclusões que a base não sustenta.

O estudo de caso logístico deste projeto segue essa abordagem.

## Etapas do protocolo

| etapa | objetivo |
| --- | --- |
| 01 | Inspecionar dados e registrar estrutura inicial. |
| 02 | Planejar tratamento e padronização. |
| 03 | Tratar e padronizar dados com scripts reprodutíveis. |
| 04 | Validar dados tratados. |
| 05 | Criar dados finais para análise e BI. |
| 06 | Validar dados finais. |
| 07 | Definir perguntas analíticas, métricas e KPIs candidatos. |
| 08 | Especificar modelo Power BI e medidas candidatas. |
| 09+ | Construir, revisar, comunicar e evoluir a solução, conforme escopo. |

## Relação com ETL

O Protocolo ADA se conecta ao ETL, mas adiciona camadas de documentação e validação humana.

* Extract: leitura e inspeção dos dados originais.
* Transform: tratamento, padronização, mascaramento e criação de tabelas finais.
* Load: preparação para consumo em BI ou outros ambientes analíticos.

A diferença é que o ADA exige relatórios, gates de decisão e registro explícito de limitações.

## Relação com BI

O protocolo prepara dados e decisões para BI:

* define tabelas fato e dimensão;
* valida chaves e relacionamentos;
* identifica campos não aditivos;
* recomenda medidas explícitas;
* evita agregações automáticas perigosas;
* documenta limitações antes da construção do dashboard.

BI é tratado como etapa posterior à validação dos dados e à definição das perguntas.

## Governança e validação humana

Governança no ADA significa manter controle sobre:

* origem dos dados;
* transformações aplicadas;
* decisões de tratamento;
* campos sensíveis;
* limitações conhecidas;
* critérios de aprovação;
* responsáveis pela validação.

Relatórios regeneráveis devem preservar seções de validação humana para evitar perda de decisões manuais.

## Limitações

O Protocolo ADA não garante automaticamente:

* qualidade da regra de negócio;
* causalidade;
* completude da base;
* validade estatística de inferências;
* ausência de vieses;
* segurança de dados sem políticas adequadas;
* sucesso de um dashboard sem revisão do usuário final.

Ele organiza o trabalho e reduz riscos, mas não substitui julgamento humano.

## Quando usar

Use o Protocolo ADA quando:

* houver dados a explorar, tratar e validar;
* for necessário documentar decisões;
* o projeto precisar de rastreabilidade;
* houver preparação para BI;
* a IA for usada como apoio, não como decisora;
* existir necessidade de governança e validação humana.

## Quando não usar

Não é a melhor escolha quando:

* o objetivo é apenas uma consulta rápida e descartável;
* não há permissão para acessar ou tratar os dados;
* não existe responsável humano para validar decisões;
* o projeto exige inferência estatística avançada sem equipe qualificada;
* a organização espera automação decisória sem revisão humana.

## Resumo final

O Protocolo ADA é uma metodologia em evolução para análise de dados assistida por IA. Ele combina evidências geradas por Python, interpretação assistida por IA e validação humana obrigatória. Sua principal contribuição é estruturar projetos de dados com rastreabilidade, governança e preparação responsável para BI.
