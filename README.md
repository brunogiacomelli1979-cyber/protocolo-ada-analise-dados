# Protocolo ADA — Análise de Dados Assistida por IA

## Descrição curta

O Protocolo ADA é uma metodologia reutilizável para projetos de análise de dados com apoio de ferramentas técnicas, IA e validação humana. O projeto organiza o ciclo de trabalho desde a inspeção inicial dos dados até a preparação para BI, com foco em rastreabilidade, governança, qualidade de dados e documentação.

O estudo de caso atual usa dados logísticos para demonstrar o protocolo em um cenário prático de clientes, rotas, cargas, viagens, entregas, abastecimentos e preparação de modelo Power BI.

## Princípio central

* Python gera evidências.
* IA interpreta hipóteses.
* Humano valida decisões.

A IA atua como apoio à análise, documentação e organização do raciocínio. Ela não é apresentada como decisora autônoma. Decisões sensíveis, interpretações finais, aprovação de tratamentos e validação de KPIs dependem de revisão humana.

## Objetivo do projeto

O objetivo do projeto é documentar e demonstrar uma metodologia profissional para conduzir análises de dados de forma assistida, auditável e responsável.

O protocolo busca:

* preservar dados brutos;
* separar dados brutos, tratados e finais;
* gerar evidências técnicas com Python;
* documentar decisões e limitações;
* validar qualidade antes de avançar;
* definir perguntas analíticas com base nos dados disponíveis;
* preparar estrutura para modelagem dimensional e Power BI;
* reforçar governança, privacidade e validação humana.

## Contexto do estudo de caso

O estudo de caso atual utiliza uma base logística. A análise foi orientada por base disponível: primeiro os dados foram inspecionados, tratados e validados; depois foram definidas as perguntas analíticas e os KPIs candidatos que a base permite responder com segurança.

Os dados finais foram organizados em tabelas de clientes, rotas, caminhões, cargas, viagens, eventos de entrega, abastecimentos e calendário. O objetivo não é apresentar uma conclusão operacional definitiva, mas demonstrar um fluxo metodológico completo e reutilizável.

## Metodologia aplicada

O Protocolo ADA usa como referência principal a metodologia Google Data Analytics, adaptada para projetos orientados por base disponível:

Data Discovery → Prepare → Process → Ask → Analyze → Share → Act

No projeto:

| Fase | Aplicação no Protocolo ADA |
| --- | --- |
| Data Discovery | Inspeção inicial dos dados, estrutura, riscos e entendimento da base. |
| Prepare | Planejamento do tratamento, privacidade, padronização e critérios de qualidade. |
| Process | Tratamento, padronização, validação e criação dos dados finais. |
| Ask | Definição de perguntas analíticas e KPIs candidatos com base na evidência disponível. |
| Analyze | Especificação de métricas, regras de agregação e medidas candidatas. |
| Share | Preparação para construção de dashboard e comunicação em Power BI. |
| Act | Validação humana, recomendações e próximos passos. |

## Estrutura do projeto

```text
.
├── dados/
│   ├── brutos/
│   ├── tratados/
│   └── finais/
├── documentos/
├── imagens/
├── powerbi/
├── relatorios/
├── scripts/
├── requirements.txt
└── README.md
```

Principais pastas:

* `dados/brutos/`: dados originais preservados.
* `dados/tratados/`: dados padronizados e tratados por scripts.
* `dados/finais/`: tabelas finais preparadas para análise e BI.
* `scripts/`: scripts Python usados para inspeção, tratamento, validação e criação dos dados finais.
* `relatorios/`: relatórios técnicos e analíticos gerados ao longo das etapas.
* `documentos/`: documentação metodológica, boas práticas e evolução do protocolo.
* `powerbi/`: espaço reservado para artefatos relacionados ao Power BI.

## Etapas concluídas

| etapa | nome | entrega principal |
| --- | --- | --- |
| 01 | Inspeção de dados | Relatório inicial de estrutura, colunas, tipos, riscos e observações. |
| 02 | Plano de tratamento | Plano documentado para tratamento, padronização e governança. |
| 03 | Tratamento e padronização | Dados tratados e relatório das transformações aplicadas. |
| 04 | Validação dos dados tratados | Validação técnica dos dados tratados antes da criação dos finais. |
| 05 | Criação dos dados finais | Tabelas finais organizadas para análise e Power BI. |
| 06 | Validação dos dados finais | Validação de arquivos finais, chaves, relacionamentos, calendário e riscos de agregação. |
| 07 | Definição de perguntas analíticas e KPIs | Perguntas, métricas e KPIs candidatos com limitações documentadas. |
| 08 | Especificação do modelo Power BI | Modelo recomendado, relacionamentos, medidas DAX candidatas e páginas sugeridas. |

## Documentação principal

Documentos metodológicos finais:

* `documentos/protocolo_ada_metodologia.md`
* `documentos/fluxo_operacional_ada.md`
* `documentos/checklist_qualidade_ada.md`
* `documentos/boas_praticas_ada.md`
* `documentos/evolucao_futura_ada.md`

Relatórios principais do estudo de caso:

* `relatorios/01_relatorio_inspecao_dados.md`
* `relatorios/02_plano_tratamento_dados.md`
* `relatorios/03_relatorio_tratamento_padronizacao.md`
* `relatorios/04_relatorio_validacao_dados_tratados.md`
* `relatorios/05_relatorio_criacao_dados_finais.md`
* `relatorios/06_relatorio_validacao_dados_finais.md`
* `relatorios/07_definicao_perguntas_kpis.md`
* `relatorios/08_especificacao_modelo_powerbi.md`

## Boas práticas aplicadas

* Preservação dos dados brutos.
* Separação entre dados brutos, tratados e finais.
* Uso de scripts Python para reprodutibilidade.
* Documentação de decisões e limitações.
* Validação humana entre etapas.
* Campos sensíveis removidos ou mascarados quando necessário.
* Nulos operacionais preservados e documentados.
* Outliers e valores incomuns não removidos automaticamente.
* Métricas e KPIs derivados apenas de campos existentes.
* Diferenciação entre métrica, KPI e dimensão de análise.
* Alerta para campos não aditivos, como médias, taxas e preços unitários.
* Preparação para modelo estrela no Power BI.
* Uso de tabela calendário.
* Recomendação de medidas explícitas em vez de agregações automáticas.

## Status atual

O Protocolo ADA v1.0 está concluído como metodologia documentada e aplicada ao estudo de caso logístico até a etapa de especificação do modelo Power BI.

As Etapas 01 a 08 foram concluídas:

O projeto possui:

* dados tratados e finais organizados;
* relatórios técnicos e analíticos;
* documentação metodológica do Protocolo ADA;
* especificação para construção manual do modelo Power BI;
* medidas DAX candidatas documentadas;
* limitações e riscos registrados.

O dashboard Power BI ainda não foi construído. Ele faz parte da próxima fase do estudo de caso aplicado, não da conclusão metodológica da v1.0.

## Próximos passos

* Construção manual do dashboard Power BI para o estudo de caso logístico.
* Validação do modelo no Power BI com base na especificação da Etapa 08.
* Documentação das medidas efetivamente implementadas.
* Revisão visual e narrativa do dashboard.
* Validação humana dos resultados apresentados antes de qualquer publicação.
* Possível evolução futura para agente assistivo especializado no Protocolo ADA.

## Tecnologias e conceitos utilizados

* Python
* Pandas
* Markdown
* Git/GitHub
* Power BI
* ETL
* Qualidade de dados
* Modelagem dimensional
* Governança de dados
* Validação humana

## Limitações

Este projeto não promete automação completa da análise de dados. O Protocolo ADA organiza o fluxo, gera evidências e apoia decisões, mas não substitui validação humana nem conhecimento de negócio.

Limitações importantes:

* KPIs sem meta são métricas candidatas, não KPIs oficiais.
* Relações observadas nos dados não provam causalidade.
* Nulos operacionais não devem ser tratados automaticamente como erro.
* Campos como médias, taxas e preços unitários exigem regras de agregação específicas.
* Não há garantia de que a base disponível responda a todas as perguntas de negócio.
* O estudo de caso logístico demonstra a metodologia, mas não representa uma solução universal pronta para qualquer domínio sem adaptação.

## Como reproduzir o fluxo de alto nível

1. Organizar os dados nas pastas do projeto.
2. Executar a inspeção inicial dos dados.
3. Criar e revisar o plano de tratamento.
4. Executar tratamento e padronização com Python.
5. Validar os dados tratados.
6. Criar os dados finais para análise.
7. Validar os dados finais.
8. Definir perguntas analíticas e KPIs candidatos.
9. Especificar modelo Power BI e medidas.
10. Validar decisões humanas antes de construir ou publicar o dashboard.

Os scripts em `scripts/` e os relatórios em `relatorios/` documentam a execução aplicada ao estudo de caso atual.

## Privacidade e dados sensíveis

O projeto considera privacidade e governança como partes do fluxo de análise.

Diretrizes adotadas:

* dados brutos devem ser preservados e protegidos;
* dados sensíveis não devem ser expostos sem necessidade;
* campos sensíveis devem ser removidos, mascarados ou documentados;
* prompts privados, regras internas sensíveis e materiais confidenciais não devem ser publicados;
* decisões sobre privacidade devem passar por validação humana;
* arquivos privados ou sensíveis devem ser protegidos por `.gitignore` quando aplicável.

O Protocolo ADA trata IA como apoio metodológico e técnico. A responsabilidade por decisões, publicação e uso dos resultados permanece humana.
