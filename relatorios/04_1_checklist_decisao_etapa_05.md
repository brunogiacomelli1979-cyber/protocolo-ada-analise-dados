# Checklist de Decisão para Etapa 05 — Criação dos Dados Finais

## 1. Objetivo

Este documento consolida as decisões pendentes antes da criação dos dados finais para Power BI na Etapa 05 do Protocolo ADA.

As decisões registradas aqui foram organizadas a partir das evidências documentadas nas etapas anteriores:

* `relatorios/02_plano_tratamento_dados.md`;
* `relatorios/03_relatorio_tratamento_padronizacao.md`;
* `relatorios/04_relatorio_validacao_dados_tratados.md`.

Python gera evidências. IA interpreta hipóteses. Humano valida decisões.

## 2. Contexto

As Etapas 01 a 04 foram concluídas com segurança:

* Etapa 01: inspeção dos dados brutos;
* Etapa 02: plano de tratamento;
* Etapa 03: tratamento e padronização dos dados;
* Etapa 04: validação dos dados tratados.

Algumas ressalvas foram registradas, mas não representam falhas críticas. Elas representam decisões necessárias antes da criação dos dados finais, especialmente sobre escopo, granularidade, relacionamentos, nulos operacionais, privacidade, taxas, agregações e preparação para uso no Power BI.

Este documento não aplica transformações. Ele apenas registra decisões humanas e metodológicas para liberar a próxima etapa com controle de risco.

## 3. Decisão sobre escopo da V1

A V1 dos dados finais usará o núcleo inicial:

* `customers_tratado.csv`;
* `loads_tratado.csv`;
* `trips_tratado.csv`;
* `delivery_events_tratado.csv`;
* `routes_tratado.csv`;
* `fuel_purchases_tratado.csv`;
* `trucks_tratado.csv`.

Tabelas complementares ficam fora da V1, mas não são descartadas:

* `drivers.csv`;
* `driver_monthly_metrics.csv`;
* `truck_utilization_metrics.csv`;
* `maintenance_records.csv`;
* `safety_incidents.csv`;
* `trailers.csv`;
* `facilities.csv`.

Justificativa:
Reduzir complexidade, evitar exposição de dados pessoais e estabilizar o modelo inicial antes de expandir escopo.

Status da decisão:

* [x] Aprovada para V1

## 4. Decisão sobre granularidade

A Etapa 05 deve criar tabelas finais separadas por granularidade, sem juntar tudo em uma única tabela.

Modelo previsto:

* `fato_cargas.csv` — granularidade: uma linha por carga;
* `fato_viagens.csv` — granularidade: uma linha por viagem;
* `fato_eventos_entrega.csv` — granularidade: uma linha por evento;
* `fato_abastecimentos.csv` — granularidade: uma linha por abastecimento;
* `dim_clientes.csv` — granularidade: uma linha por cliente;
* `dim_rotas.csv` — granularidade: uma linha por rota;
* `dim_caminhoes.csv` — granularidade: uma linha por caminhão;
* `dim_calendario.csv` — granularidade: uma linha por data.

Justificativa:
Evitar duplicação de medidas e preservar a leitura correta de cargas, viagens, eventos e abastecimentos.

Status da decisão:

* [x] Aprovada para V1

## 5. Decisão sobre relacionamentos

Os relacionamentos candidatos validados na Etapa 04 podem ser usados como base para a Etapa 05, pois não apresentaram valores sem correspondência.

Relacionamentos aceitos para V1:

* `loads.load_id` ↔ `trips.load_id`;
* `trips.trip_id` ↔ `delivery_events.trip_id`;
* `loads.customer_id` ↔ `customers.customer_id`;
* `loads.route_id` ↔ `routes.route_id`;
* `trips.truck_id` ↔ `trucks.truck_id`;
* `fuel_purchases.trip_id` ↔ `trips.trip_id`;
* `fuel_purchases.truck_id` ↔ `trucks.truck_id`.

Observação:
A cardinalidade observada não deve ser confundida com cardinalidade conceitual. A modelagem final no Power BI deve respeitar a granularidade de cada tabela.

Status da decisão:

* [x] Aprovada para V1

## 6. Decisão sobre nulos operacionais

Os nulos preservados em campos operacionais não devem ser preenchidos automaticamente, removidos ou substituídos por "Desconhecido" nesta fase.

Campos com nulos preservados:

* `trips.driver_id`;
* `trips.truck_id`;
* `trips.trailer_id`;
* `fuel_purchases.driver_id`;
* `fuel_purchases.truck_id`.

Decisão:
Preservar os registros com nulos nos dados finais, mantendo o valor nulo para análise posterior.

Justificativa:
Remover registros poderia distorcer volumes operacionais. Preencher automaticamente criaria informação artificial. A ausência de vínculo deve ser tratada como característica do dado, não como erro automático.

Status da decisão:

* [x] Aprovada para V1 com ressalva controlada

## 7. Decisão sobre dados sensíveis e mascarados

Campos já mascarados na Etapa 03 podem seguir para os dados finais, desde que permaneçam mascarados.

Campos:

* `customer_name` → manter mascarado em `dim_clientes.csv`;
* `vin` → manter mascarado ou avaliar remoção em `dim_caminhoes.csv`;
* `fuel_card_number` → preferencialmente remover de `fato_abastecimentos.csv`, pois não agrega valor analítico público.

Decisão recomendada:

* `customer_name`: manter mascarado para permitir segmentação sem exposição comercial;
* `vin`: remover dos dados finais ou manter mascarado apenas se houver justificativa analítica;
* `fuel_card_number`: remover dos dados finais.

Justificativa:
Reduzir risco de exposição e manter apenas campos úteis para análise pública.

Status da decisão:

* [x] Aprovada para V1

## 8. Decisão sobre percentuais, taxas e preços unitários

* `fuel_surcharge_rate` deve ser tratado como percentual/taxa em escala decimal, sem multiplicar por 100 no CSV final;
* `base_rate_per_mile` deve ser tratado como taxa monetária por milha, não percentual;
* `price_per_gallon` deve ser tratado como preço unitário por galão, não percentual.

Regras:

* Não alterar escala nos arquivos finais.
* Formatação percentual ou monetária deve ocorrer no Power BI.
* Não somar diretamente taxas, percentuais ou preços unitários.
* Agregações devem ser feitas com média simples ou ponderada conforme contexto do indicador.

Status da decisão:

* [x] Aprovada para V1

## 9. Decisão sobre agregações

A Etapa 05 não deve criar agregações finais complexas. Ela deve criar bases finais limpas e modeláveis.

Campos que não devem ser somados diretamente:

* `average_mpg`;
* `fuel_surcharge_rate`;
* `base_rate_per_mile`;
* `price_per_gallon`.

Decisão:
Preservar os campos nos fatos ou dimensões correspondentes e documentar que medidas agregadas devem ser criadas posteriormente no Power BI com regra explícita.

Status da decisão:

* [x] Aprovada para V1

## 10. Decisão sobre dimensão calendário

Criar `dim_calendario.csv` na Etapa 05.

A dimensão calendário deve ser criada com base no intervalo mínimo e máximo das datas presentes nas tabelas finais do núcleo V1.

Campos mínimos esperados:

* `data`;
* `ano`;
* `mes`;
* `nome_mes`;
* `trimestre`;
* `ano_mes`;
* `dia`;
* `dia_semana`;
* `nome_dia_semana`.

Justificativa:
Permitir análise temporal consistente no Power BI.

Status da decisão:

* [x] Aprovada para V1

## 11. Decisão sobre criação de KPIs

A Etapa 05 pode preparar campos necessários para KPIs, mas não deve criar KPIs finais complexos.

KPIs finais devem ser documentados e calculados posteriormente em etapa própria ou no Power BI.

Status da decisão:

* [x] Aprovada para V1

## 12. Decisão final de liberação da Etapa 05

Com base nas validações das Etapas 01 a 04 e nas decisões acima, a Etapa 05 está liberada para criação dos dados finais em `dados/finais/`.

Condições:

* não alterar dados brutos;
* não alterar dados tratados;
* criar apenas arquivos finais em `dados/finais/`;
* preservar granularidade;
* respeitar mascaramento/remoção de campos sensíveis;
* documentar todos os arquivos finais criados;
* não gerar dashboard.

Status:

* [x] Etapa 05 liberada
* [ ] Etapa 05 não liberada

## 13. Confirmações finais

* este documento não alterou dados;
* nenhum arquivo final foi criado;
* nenhum KPI final foi criado;
* nenhum dashboard foi criado;
* este documento apenas registra decisões humanas/metodológicas para liberar a próxima etapa.
