# Relatório da Etapa 03 — Tratamento e Padronização dos Dados

Gerado em: 2026-06-13 07:18:51

## 1. Objetivo da etapa

Esta etapa aplica os tratamentos aprovados na Etapa 02 para gerar dados tratados, preservando integralmente os dados brutos.

Python gera evidências. IA interpreta hipóteses. Humano valida decisões.

## 2. Confirmação de segurança

- Dados brutos não foram alterados.
- Dados tratados foram criados em `dados/tratados/`.
- Nenhum dado final foi criado.
- Nenhum KPI final foi criado.
- Nenhum dashboard foi gerado.
- Nenhuma linha foi removida.
- Nenhuma imputação automática foi feita.

## 3. Fontes utilizadas

- Arquivos brutos lidos: `customers.csv`, `loads.csv`, `trips.csv`, `delivery_events.csv`, `routes.csv`, `fuel_purchases.csv`, `trucks.csv`.
- Relatórios de referência: `relatorios\01_relatorio_inspecao_dados.md`, `relatorios\02_plano_tratamento_dados.md`.
- Arquivos tratados gerados: `dados/tratados/customers_tratado.csv`, `dados/tratados/loads_tratado.csv`, `dados/tratados/trips_tratado.csv`, `dados/tratados/delivery_events_tratado.csv`, `dados/tratados/routes_tratado.csv`, `dados/tratados/fuel_purchases_tratado.csv`, `dados/tratados/trucks_tratado.csv`.

## 4. Escopo aplicado na Etapa 03

Tabelas tratadas no núcleo V1: `customers.csv`, `loads.csv`, `trips.csv`, `delivery_events.csv`, `routes.csv`, `fuel_purchases.csv`, `trucks.csv`.

Tabelas fora do escopo desta etapa:

| tabela fora do escopo | motivo |
| --- | --- |
| drivers.csv | contém dados pessoais/identificáveis e ficou fora do núcleo V1. |
| driver_monthly_metrics.csv | tabela agregada mensal por motorista; fase futura. |
| truck_utilization_metrics.csv | tabela agregada mensal por caminhão; fase futura. |
| maintenance_records.csv | manutenção ficou como escopo complementar. |
| safety_incidents.csv | incidentes envolvem risco operacional e baixa ocorrência. |
| trailers.csv | dimensão complementar de equipamento. |
| facilities.csv | dimensão complementar de instalações. |

## 5. Tratamentos aplicados por tabela

| arquivo bruto | arquivo tratado | linhas antes/depois | colunas antes/depois | colunas convertidas | colunas mascaradas | colunas removidas | observações |
| --- | --- | --- | --- | --- | --- | --- | --- |
| customers.csv | customers_tratado.csv | 200 / 200 | 8 / 8 | contract_start_date | customer_name | nenhuma | Linhas preservadas; granularidade não alterada; sem joins. |
| loads.csv | loads_tratado.csv | 85410 / 85410 | 12 / 12 | load_date | nenhuma | nenhuma | Linhas preservadas; granularidade não alterada; sem joins. |
| trips.csv | trips_tratado.csv | 85410 / 85410 | 12 / 12 | dispatch_date | nenhuma | nenhuma | Linhas preservadas; granularidade não alterada; sem joins. |
| delivery_events.csv | delivery_events_tratado.csv | 170820 / 170820 | 11 / 11 | scheduled_datetime, actual_datetime | nenhuma | nenhuma | Linhas preservadas; granularidade não alterada; sem joins. |
| routes.csv | routes_tratado.csv | 58 / 58 | 9 / 9 | nenhuma | nenhuma | nenhuma | Linhas preservadas; granularidade não alterada; sem joins. |
| fuel_purchases.csv | fuel_purchases_tratado.csv | 196442 / 196442 | 11 / 11 | purchase_date | fuel_card_number | nenhuma | Linhas preservadas; granularidade não alterada; sem joins. |
| trucks.csv | trucks_tratado.csv | 120 / 120 | 11 / 11 | acquisition_date | vin | nenhuma | Linhas preservadas; granularidade não alterada; sem joins. |

## 6. Conversão de datas

| tabela | coluna | valores válidos antes | valores convertidos | valores não convertidos | observação |
| --- | --- | --- | --- | --- | --- |
| customers.csv | contract_start_date | 200 | 200 | 0 | Conversão segura com errors='coerce'; fuso horário não foi alterado. |
| loads.csv | load_date | 85410 | 85410 | 0 | Conversão segura com errors='coerce'; fuso horário não foi alterado. |
| trips.csv | dispatch_date | 85410 | 85410 | 0 | Conversão segura com errors='coerce'; fuso horário não foi alterado. |
| delivery_events.csv | scheduled_datetime | 170820 | 170820 | 0 | Conversão segura com errors='coerce'; fuso horário não foi alterado. |
| delivery_events.csv | actual_datetime | 170820 | 170820 | 0 | Conversão segura com errors='coerce'; fuso horário não foi alterado. |
| fuel_purchases.csv | purchase_date | 196442 | 196442 | 0 | Conversão segura com errors='coerce'; fuso horário não foi alterado. |
| trucks.csv | acquisition_date | 120 | 120 | 0 | Conversão segura com errors='coerce'; fuso horário não foi alterado. |

## 7. Campos sensíveis e mascaramento

| tabela | coluna | tipo de risco | ação aplicada | justificativa |
| --- | --- | --- | --- | --- |
| customers.csv | customer_name | dado sensível/confidencial | mascaramento consistente de 107 valores distintos | preservar estrutura analítica sem expor valor original. |
| fuel_purchases.csv | fuel_card_number | dado sensível/confidencial | mascaramento consistente de 176645 valores distintos | preservar estrutura analítica sem expor valor original. |
| trucks.csv | vin | dado sensível/confidencial | mascaramento consistente de 120 valores distintos | preservar estrutura analítica sem expor valor original. |

## 8. Valores ausentes preservados

| tabela | coluna | nulos antes | nulos depois | tratamento aplicado | justificativa |
| --- | --- | --- | --- | --- | --- |
| trips.csv | driver_id | 1714 | 1714 | nulos preservados | não preencher, remover ou criar categoria sem validação humana. |
| trips.csv | truck_id | 1672 | 1672 | nulos preservados | não preencher, remover ou criar categoria sem validação humana. |
| trips.csv | trailer_id | 1680 | 1680 | nulos preservados | não preencher, remover ou criar categoria sem validação humana. |
| fuel_purchases.csv | driver_id | 3988 | 3988 | nulos preservados | não preencher, remover ou criar categoria sem validação humana. |
| fuel_purchases.csv | truck_id | 3880 | 3880 | nulos preservados | não preencher, remover ou criar categoria sem validação humana. |

## 9. Métricas e campos preservados

| tabela | campo | tipo | ação |
| --- | --- | --- | --- |
| customers.csv | annual_revenue_potential | financeiro preservado | valor preservado, sem agregação, arredondamento ou alteração de escala |
| loads.csv | accessorial_charges | financeiro preservado | valor preservado, sem agregação, arredondamento ou alteração de escala |
| loads.csv | fuel_surcharge | financeiro preservado | valor preservado, sem agregação, arredondamento ou alteração de escala |
| loads.csv | revenue | financeiro preservado | valor preservado, sem agregação, arredondamento ou alteração de escala |
| loads.csv | pieces | métrica operacional preservada | valor preservado, sem agregação, arredondamento ou alteração de escala |
| loads.csv | weight_lbs | métrica operacional preservada | valor preservado, sem agregação, arredondamento ou alteração de escala |
| trips.csv | actual_distance_miles | métrica operacional preservada | valor preservado, sem agregação, arredondamento ou alteração de escala |
| trips.csv | actual_duration_hours | métrica operacional preservada | valor preservado, sem agregação, arredondamento ou alteração de escala |
| trips.csv | average_mpg | métrica operacional preservada | valor preservado, sem agregação, arredondamento ou alteração de escala |
| trips.csv | fuel_gallons_used | métrica operacional preservada | valor preservado, sem agregação, arredondamento ou alteração de escala |
| trips.csv | idle_time_hours | métrica operacional preservada | valor preservado, sem agregação, arredondamento ou alteração de escala |
| delivery_events.csv | detention_minutes | métrica operacional preservada | valor preservado, sem agregação, arredondamento ou alteração de escala |
| routes.csv | base_rate_per_mile | financeiro preservado | valor preservado, sem agregação, arredondamento ou alteração de escala |
| routes.csv | base_rate_per_mile | taxa/preço unitário preservado | valor preservado, sem agregação, arredondamento ou alteração de escala |
| routes.csv | fuel_surcharge_rate | taxa/preço unitário preservado | valor preservado, sem agregação, arredondamento ou alteração de escala |
| routes.csv | typical_distance_miles | métrica operacional preservada | valor preservado, sem agregação, arredondamento ou alteração de escala |
| routes.csv | typical_transit_days | métrica operacional preservada | valor preservado, sem agregação, arredondamento ou alteração de escala |
| fuel_purchases.csv | price_per_gallon | financeiro preservado | valor preservado, sem agregação, arredondamento ou alteração de escala |
| fuel_purchases.csv | total_cost | financeiro preservado | valor preservado, sem agregação, arredondamento ou alteração de escala |
| fuel_purchases.csv | price_per_gallon | taxa/preço unitário preservado | valor preservado, sem agregação, arredondamento ou alteração de escala |
| fuel_purchases.csv | gallons | métrica operacional preservada | valor preservado, sem agregação, arredondamento ou alteração de escala |
| trucks.csv | acquisition_mileage | métrica operacional preservada | valor preservado, sem agregação, arredondamento ou alteração de escala |
| trucks.csv | tank_capacity_gallons | métrica operacional preservada | valor preservado, sem agregação, arredondamento ou alteração de escala |

## 10. Controle de qualidade pós-tratamento

| tabela | linhas bruto | linhas tratado | diferença de linhas | colunas bruto | colunas tratado | diferença de colunas | status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| customers.csv | 200 | 200 | 0 | 8 | 8 | 0 | OK - linhas preservadas |
| loads.csv | 85410 | 85410 | 0 | 12 | 12 | 0 | OK - linhas preservadas |
| trips.csv | 85410 | 85410 | 0 | 12 | 12 | 0 | OK - linhas preservadas |
| delivery_events.csv | 170820 | 170820 | 0 | 11 | 11 | 0 | OK - linhas preservadas |
| routes.csv | 58 | 58 | 0 | 9 | 9 | 0 | OK - linhas preservadas |
| fuel_purchases.csv | 196442 | 196442 | 0 | 11 | 11 | 0 | OK - linhas preservadas |
| trucks.csv | 120 | 120 | 0 | 11 | 11 | 0 | OK - linhas preservadas |

## 11. Pendências para a Etapa 04

- Validar se datas foram convertidas corretamente.
- Validar mascaramento.
- Validar nulos preservados.
- Validar escalas de taxas/percentuais.
- Validar relacionamentos.
- Validar se arquivos tratados estão prontos para geração de dados finais.

## 12. Decisão da Etapa 03

Status da Etapa 03:

* [ ] Aprovada
* [x] Aprovada com ressalvas
* [ ] Reprovada para avanço

Observações da validação humana:

* A Etapa 03 está aprovada como execução inicial de tratamento e padronização dos dados do núcleo V1.
* Os dados brutos foram preservados integralmente.
* Foram criados arquivos tratados em `dados/tratados/` para `customers`, `loads`, `trips`, `delivery_events`, `routes`, `fuel_purchases` e `trucks`.
* Nenhuma linha foi removida, nenhuma imputação automática foi aplicada e nenhuma alteração de granularidade foi realizada.
* Os campos sensíveis `customer_name`, `fuel_card_number` e `vin` foram mascarados de forma consistente.
* As datas previstas foram convertidas com sucesso, sem registros não convertidos.
* Os nulos operacionais foram preservados para validação posterior.
* As ressalvas para a próxima etapa envolvem validar tipos gravados nos arquivos tratados, consistência do mascaramento, formato das datas, relacionamentos entre tabelas tratadas, escala de taxas/percentuais e prontidão para geração de dados finais.
* A próxima etapa só deve gerar dados finais após validação dos arquivos tratados.


## 13. Confirmações finais

- Dados brutos preservados.
- Arquivos tratados criados.
- Dados finais não criados.
- KPIs finais não criados.
- Dashboard não criado.
