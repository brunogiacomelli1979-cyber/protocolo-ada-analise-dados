# Fluxo Operacional do Protocolo ADA

## Objetivo

Este documento descreve o fluxo operacional do Protocolo ADA, etapa por etapa, indicando entradas, processamentos, saídas, gates de validação e responsabilidades.

Uma regra central do protocolo é que uma etapa não deve executar a responsabilidade da etapa seguinte. Cada fase deve entregar evidências suficientes para a próxima, sem antecipar decisões que ainda precisam de validação.

## Tipos de etapa

| tipo | descrição |
| --- | --- |
| Técnica | Executa leitura, tratamento, validação ou geração de evidências com Python. |
| Documental | Registra decisões, planos, limitações e especificações. |
| Analítica | Define perguntas, métricas, hipóteses e interpretações possíveis. |
| Visual | Constrói ou especifica dashboards, relatórios e comunicação visual. |

## Fluxo passo a passo

### Etapa 01 — Inspeção inicial

* Entrada: dados brutos.
* Processamento: leitura, estrutura, dimensões, colunas, amostras e riscos iniciais.
* Saída: relatório de inspeção.
* Tipo: técnica e documental.
* Gate: humano confirma que a base foi compreendida o suficiente para planejar tratamento.

### Etapa 02 — Plano de tratamento

* Entrada: relatório de inspeção.
* Processamento: definição de regras de padronização, privacidade e qualidade.
* Saída: plano de tratamento.
* Tipo: documental.
* Gate: humano aprova regras antes de modificar qualquer dado derivado.

### Etapa 03 — Tratamento e padronização

* Entrada: dados brutos e plano de tratamento.
* Processamento: padronização, mascaramento, tipos, nomes de colunas e limpeza controlada.
* Saída: dados tratados e relatório de tratamento.
* Tipo: técnica.
* Gate: humano revisa se as transformações foram aceitáveis.

### Etapa 04 — Validação dos dados tratados

* Entrada: dados tratados e relatórios anteriores.
* Processamento: validação de chaves, nulos, duplicidades, datas, relacionamentos e campos sensíveis.
* Saída: relatório de validação.
* Tipo: técnica e documental.
* Gate: humano decide se os dados tratados podem avançar para dados finais.

### Etapa 05 — Criação dos dados finais

* Entrada: dados tratados aprovados.
* Processamento: seleção de colunas, separação em fatos e dimensões, criação de calendário.
* Saída: dados finais e relatório de criação.
* Tipo: técnica.
* Gate: humano confirma que a estrutura final está adequada ao uso analítico.

### Etapa 06 — Validação dos dados finais

* Entrada: dados finais.
* Processamento: validação de existência, leitura, estrutura, chaves, relacionamentos, calendário e riscos de agregação.
* Saída: relatório de validação final.
* Tipo: técnica e documental.
* Gate: humano decide se os dados finais estão aptos para perguntas analíticas e BI.

### Etapa 07 — Perguntas analíticas e KPIs

* Entrada: dados finais validados.
* Processamento: definição de perguntas possíveis, métricas, KPIs candidatos e limitações.
* Saída: relatório analítico de perguntas e KPIs.
* Tipo: analítica e documental.
* Gate: humano aprova escopo analítico antes da modelagem BI.

### Etapa 08 — Especificação do modelo Power BI

* Entrada: perguntas e KPIs aprovados.
* Processamento: especificação de modelo, relacionamentos, medidas candidatas, páginas e cuidados.
* Saída: relatório de especificação Power BI.
* Tipo: documental, analítica e visual.
* Gate: humano aprova construção manual ou automatizada do dashboard.

## Gates de validação

| gate | decisão esperada |
| --- | --- |
| Após inspeção | A base é compreensível e pode ser planejada. |
| Após plano | As regras de tratamento estão aprovadas. |
| Após tratamento | As transformações são aceitáveis. |
| Após validação dos tratados | Os dados tratados podem virar finais. |
| Após criação dos finais | A estrutura final é adequada. |
| Após validação dos finais | A base está pronta para perguntas e BI. |
| Após perguntas e KPIs | O escopo analítico está aprovado. |
| Após especificação BI | O dashboard pode ser construído. |

## Separação de responsabilidades

* A inspeção não deve tratar dados.
* O plano não deve executar transformação.
* O tratamento não deve criar KPIs finais.
* A validação não deve alterar CSVs.
* A criação de dados finais não deve construir dashboard.
* A definição de KPIs não deve criar medidas DAX definitivas.
* A especificação Power BI não deve criar `.pbix`.

Essa separação protege rastreabilidade e reduz decisões implícitas.

## Exemplo aplicado ao estudo de caso logístico

No estudo de caso atual, os dados logísticos foram organizados em:

* clientes;
* rotas;
* caminhões;
* cargas;
* viagens;
* eventos de entrega;
* abastecimentos;
* calendário.

O protocolo permitiu:

* preservar dados brutos;
* criar dados tratados;
* criar dados finais em fatos e dimensões;
* validar chaves e relacionamentos;
* documentar nulos operacionais;
* identificar campos que não devem ser somados;
* definir perguntas sobre receita, rotas, viagens, entregas e combustível;
* especificar um modelo Power BI antes da construção do dashboard.

## Quadro resumido das Etapas 01 a 08 executadas

| etapa | nome | principal entrega | status metodológico |
| --- | --- | --- | --- |
| 01 | Inspeção de dados | Relatório inicial de estrutura e riscos. | Concluída. |
| 02 | Plano de tratamento | Critérios de limpeza, padronização e governança. | Concluída. |
| 03 | Tratamento e padronização | Dados tratados e relatório técnico. | Concluída. |
| 04 | Validação dos tratados | Evidências de qualidade dos dados tratados. | Concluída. |
| 05 | Criação dos finais | Tabelas finais para BI. | Concluída. |
| 06 | Validação dos finais | Confirmação estrutural e relacional dos dados finais. | Concluída. |
| 07 | Perguntas e KPIs | Catálogo analítico e limitações. | Concluída. |
| 08 | Especificação Power BI | Modelo, medidas candidatas e páginas. | Concluída. |

## Encerramento

O fluxo operacional do ADA deve ser executado com disciplina. A qualidade do resultado depende menos de automação isolada e mais da sequência correta entre evidência técnica, interpretação assistida e validação humana.
