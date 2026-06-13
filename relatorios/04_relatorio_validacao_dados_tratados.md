# Relatório da Etapa 04 — Validação dos Dados Tratados

Gerado em: 2026-06-13 07:35:13

## 1. Objetivo da etapa

Esta etapa valida os dados tratados antes da criação dos dados finais para Power BI, sem aplicar novas transformações.

Python gera evidências. IA interpreta hipóteses. Humano valida decisões.

## 2. Confirmação de segurança

- Dados brutos não foram alterados.
- Dados tratados não foram alterados.
- Nenhum dado final foi criado.
- Nenhum KPI final foi criado.
- Nenhum dashboard foi gerado.
- Nenhuma transformação foi aplicada.

## 3. Fontes utilizadas

- Arquivos tratados lidos: `customers_tratado.csv`, `loads_tratado.csv`, `trips_tratado.csv`, `delivery_events_tratado.csv`, `routes_tratado.csv`, `fuel_purchases_tratado.csv`, `trucks_tratado.csv`.
- Relatórios de referência: `relatorios\01_relatorio_inspecao_dados.md`, `relatorios\02_plano_tratamento_dados.md`, `relatorios\03_relatorio_tratamento_padronizacao.md`.

## 4. Existência e leitura dos arquivos tratados

| arquivo esperado | encontrado | sucesso de leitura | linhas | colunas | erro | status | observação |
| --- | --- | --- | --- | --- | --- | --- | --- |
| dados\tratados\customers_tratado.csv | Sim | Sim | 200 | 8 |  | OK | Arquivo tratado lido com sucesso. |
| dados\tratados\loads_tratado.csv | Sim | Sim | 85410 | 12 |  | OK | Arquivo tratado lido com sucesso. |
| dados\tratados\trips_tratado.csv | Sim | Sim | 85410 | 12 |  | OK | Arquivo tratado lido com sucesso. |
| dados\tratados\delivery_events_tratado.csv | Sim | Sim | 170820 | 11 |  | OK | Arquivo tratado lido com sucesso. |
| dados\tratados\routes_tratado.csv | Sim | Sim | 58 | 9 |  | OK | Arquivo tratado lido com sucesso. |
| dados\tratados\fuel_purchases_tratado.csv | Sim | Sim | 196442 | 11 |  | OK | Arquivo tratado lido com sucesso. |
| dados\tratados\trucks_tratado.csv | Sim | Sim | 120 | 11 |  | OK | Arquivo tratado lido com sucesso. |

## 5. Preservação de linhas e colunas

| arquivo | linhas no bruto | linhas no tratado | diferença | status |
| --- | --- | --- | --- | --- |
| customers_tratado.csv | 200 | 200 | 0 | OK |
| loads_tratado.csv | 85410 | 85410 | 0 | OK |
| trips_tratado.csv | 85410 | 85410 | 0 | OK |
| delivery_events_tratado.csv | 170820 | 170820 | 0 | OK |
| routes_tratado.csv | 58 | 58 | 0 | OK |
| fuel_purchases_tratado.csv | 196442 | 196442 | 0 | OK |
| trucks_tratado.csv | 120 | 120 | 0 | OK |

| arquivo | colunas no bruto | colunas no tratado | diferença | colunas ausentes | colunas novas | status |
| --- | --- | --- | --- | --- | --- | --- |
| customers_tratado.csv | 8 | 8 | 0 | nenhuma | nenhuma | OK |
| loads_tratado.csv | 12 | 12 | 0 | nenhuma | nenhuma | OK |
| trips_tratado.csv | 12 | 12 | 0 | nenhuma | nenhuma | OK |
| delivery_events_tratado.csv | 11 | 11 | 0 | nenhuma | nenhuma | OK |
| routes_tratado.csv | 9 | 9 | 0 | nenhuma | nenhuma | OK |
| fuel_purchases_tratado.csv | 11 | 11 | 0 | nenhuma | nenhuma | OK |
| trucks_tratado.csv | 11 | 11 | 0 | nenhuma | nenhuma | OK |

## 6. Validação de mascaramento

| tabela | coluna | existe | padrão | distintos | nulos | status | observação |
| --- | --- | --- | --- | --- | --- | --- | --- |
| customers_tratado.csv | customer_name | Sim | ^Cliente_\d{3,}$ | 107 | 0 | OK | Máscara validada sem expor valores originais. |
| fuel_purchases_tratado.csv | fuel_card_number | Sim | ^CARTAO_MASCARADO_\d{3,}$ | 176645 | 0 | OK | Máscara validada sem expor valores originais. |
| trucks_tratado.csv | vin | Sim | ^VIN_MASCARADO_\d{3,}$ | 120 | 0 | OK | Máscara validada sem expor valores originais. |

## 7. Validação de datas

| tabela | coluna | nulos | menor data | maior data | valores inválidos aparentes | status |
| --- | --- | --- | --- | --- | --- | --- |
| customers_tratado.csv | contract_start_date | 0 | 2020-01-07 00:00:00 | 2022-01-01 00:00:00 | 0 | OK |
| loads_tratado.csv | load_date | 0 | 2022-01-01 00:00:00 | 2024-12-31 00:00:00 | 0 | OK |
| trips_tratado.csv | dispatch_date | 0 | 2022-01-01 00:00:00 | 2024-12-31 00:00:00 | 0 | OK |
| delivery_events_tratado.csv | scheduled_datetime | 0 | 2022-01-01 07:00:00 | 2025-01-02 19:21:42.629833 | 0 | OK |
| delivery_events_tratado.csv | actual_datetime | 0 | 2022-01-01 06:13:28.892373 | 2025-01-03 00:29:47.403350 | 0 | OK |
| fuel_purchases_tratado.csv | purchase_date | 0 | 2022-01-01 00:00:00 | 2025-01-02 23:00:00 | 0 | OK |
| trucks_tratado.csv | acquisition_date | 0 | 2015-01-27 00:00:00 | 2021-10-08 00:00:00 | 0 | OK |

## 8. Validação de nulos preservados

| tabela | coluna | nulos | percentual de nulos | status | interpretação pendente |
| --- | --- | --- | --- | --- | --- |
| trips_tratado.csv | driver_id | 1714 | 2.01% | Atenção | Nulos preservados; validar significado antes da Etapa 05. |
| trips_tratado.csv | truck_id | 1672 | 1.96% | Atenção | Nulos preservados; validar significado antes da Etapa 05. |
| trips_tratado.csv | trailer_id | 1680 | 1.97% | Atenção | Nulos preservados; validar significado antes da Etapa 05. |
| fuel_purchases_tratado.csv | driver_id | 3988 | 2.03% | Atenção | Nulos preservados; validar significado antes da Etapa 05. |
| fuel_purchases_tratado.csv | truck_id | 3880 | 1.98% | Atenção | Nulos preservados; validar significado antes da Etapa 05. |

## 9. Validação de tipos técnicos

Os tipos lidos pelo pandas são evidência técnica, não verdade definitiva de banco de dados.

| tabela | coluna | tipo técnico lido | papel esperado | status |
| --- | --- | --- | --- | --- |
| customers_tratado.csv | customer_id | str | ID como texto | OK |
| customers_tratado.csv | customer_name | str | evidência técnica | OK |
| customers_tratado.csv | customer_type | str | evidência técnica | OK |
| customers_tratado.csv | credit_terms_days | int64 | evidência técnica | OK |
| customers_tratado.csv | primary_freight_type | str | evidência técnica | OK |
| customers_tratado.csv | account_status | str | evidência técnica | OK |
| customers_tratado.csv | contract_start_date | str | data legível | OK |
| customers_tratado.csv | annual_revenue_potential | int64 | numérico financeiro | OK |
| loads_tratado.csv | load_id | str | ID como texto | OK |
| loads_tratado.csv | customer_id | str | ID como texto | OK |
| loads_tratado.csv | route_id | str | ID como texto | OK |
| loads_tratado.csv | load_date | str | data legível | OK |
| loads_tratado.csv | load_type | str | evidência técnica | OK |
| loads_tratado.csv | weight_lbs | int64 | métrica operacional numérica | OK |
| loads_tratado.csv | pieces | int64 | métrica operacional numérica | OK |
| loads_tratado.csv | revenue | float64 | numérico financeiro | OK |
| loads_tratado.csv | fuel_surcharge | float64 | numérico financeiro | OK |
| loads_tratado.csv | accessorial_charges | int64 | numérico financeiro | OK |
| loads_tratado.csv | load_status | str | evidência técnica | OK |
| loads_tratado.csv | booking_type | str | evidência técnica | OK |
| trips_tratado.csv | trip_id | str | ID como texto | OK |
| trips_tratado.csv | load_id | str | ID como texto | OK |
| trips_tratado.csv | driver_id | str | ID como texto | OK |
| trips_tratado.csv | truck_id | str | ID como texto | OK |
| trips_tratado.csv | trailer_id | str | ID como texto | OK |
| trips_tratado.csv | dispatch_date | str | data legível | OK |
| trips_tratado.csv | actual_distance_miles | int64 | métrica operacional numérica | OK |
| trips_tratado.csv | actual_duration_hours | float64 | métrica operacional numérica | OK |
| trips_tratado.csv | fuel_gallons_used | float64 | métrica operacional numérica | OK |
| trips_tratado.csv | average_mpg | float64 | métrica operacional numérica | OK |
| trips_tratado.csv | idle_time_hours | float64 | métrica operacional numérica | OK |
| trips_tratado.csv | trip_status | str | evidência técnica | OK |
| delivery_events_tratado.csv | event_id | str | ID como texto | OK |
| delivery_events_tratado.csv | load_id | str | ID como texto | OK |
| delivery_events_tratado.csv | trip_id | str | ID como texto | OK |
| delivery_events_tratado.csv | event_type | str | evidência técnica | OK |
| delivery_events_tratado.csv | facility_id | str | ID como texto | OK |
| delivery_events_tratado.csv | scheduled_datetime | str | data legível | OK |
| delivery_events_tratado.csv | actual_datetime | str | data legível | OK |
| delivery_events_tratado.csv | detention_minutes | int64 | métrica operacional numérica | OK |
| delivery_events_tratado.csv | on_time_flag | bool | booleano/flag | OK |
| delivery_events_tratado.csv | location_city | str | evidência técnica | OK |
| delivery_events_tratado.csv | location_state | str | evidência técnica | OK |
| routes_tratado.csv | route_id | str | ID como texto | OK |
| routes_tratado.csv | origin_city | str | evidência técnica | OK |
| routes_tratado.csv | origin_state | str | evidência técnica | OK |
| routes_tratado.csv | destination_city | str | evidência técnica | OK |
| routes_tratado.csv | destination_state | str | evidência técnica | OK |
| routes_tratado.csv | typical_distance_miles | int64 | métrica operacional numérica | OK |
| routes_tratado.csv | base_rate_per_mile | float64 | numérico financeiro | OK |
| routes_tratado.csv | fuel_surcharge_rate | float64 | evidência técnica | OK |
| routes_tratado.csv | typical_transit_days | int64 | métrica operacional numérica | OK |
| fuel_purchases_tratado.csv | fuel_purchase_id | str | ID como texto | OK |
| fuel_purchases_tratado.csv | trip_id | str | ID como texto | OK |
| fuel_purchases_tratado.csv | truck_id | str | ID como texto | OK |
| fuel_purchases_tratado.csv | driver_id | str | ID como texto | OK |
| fuel_purchases_tratado.csv | purchase_date | str | data legível | OK |
| fuel_purchases_tratado.csv | location_city | str | evidência técnica | OK |
| fuel_purchases_tratado.csv | location_state | str | evidência técnica | OK |
| fuel_purchases_tratado.csv | gallons | float64 | métrica operacional numérica | OK |
| fuel_purchases_tratado.csv | price_per_gallon | float64 | numérico financeiro | OK |
| fuel_purchases_tratado.csv | total_cost | float64 | numérico financeiro | OK |
| fuel_purchases_tratado.csv | fuel_card_number | str | evidência técnica | OK |
| trucks_tratado.csv | truck_id | str | ID como texto | OK |
| trucks_tratado.csv | unit_number | int64 | evidência técnica | OK |
| trucks_tratado.csv | make | str | evidência técnica | OK |
| trucks_tratado.csv | model_year | int64 | evidência técnica | OK |
| trucks_tratado.csv | vin | str | evidência técnica | OK |
| trucks_tratado.csv | acquisition_date | str | data legível | OK |
| trucks_tratado.csv | acquisition_mileage | int64 | métrica operacional numérica | OK |
| trucks_tratado.csv | fuel_type | str | evidência técnica | OK |
| trucks_tratado.csv | tank_capacity_gallons | int64 | métrica operacional numérica | OK |
| trucks_tratado.csv | status | str | evidência técnica | OK |
| trucks_tratado.csv | home_terminal | str | evidência técnica | OK |

## 10. Validação de relacionamentos candidatos

| tabela origem | coluna origem | tabela destino | coluna destino | valores na origem | sem correspondência | percentual sem correspondência | cardinalidade observada | status | observação |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| loads_tratado.csv | load_id | trips_tratado.csv | load_id | 85410 | 0 | 0.00% | 1:1 observado | OK | Validação por conjuntos de chaves; não define cardinalidade conceitual. |
| trips_tratado.csv | trip_id | delivery_events_tratado.csv | trip_id | 85410 | 0 | 0.00% | 1:N observado | OK | Validação por conjuntos de chaves; não define cardinalidade conceitual. |
| loads_tratado.csv | customer_id | customers_tratado.csv | customer_id | 200 | 0 | 0.00% | N:1 observado | OK | Validação por conjuntos de chaves; não define cardinalidade conceitual. |
| loads_tratado.csv | route_id | routes_tratado.csv | route_id | 58 | 0 | 0.00% | N:1 observado | OK | Validação por conjuntos de chaves; não define cardinalidade conceitual. |
| trips_tratado.csv | truck_id | trucks_tratado.csv | truck_id | 92 | 0 | 0.00% | N:1 observado | OK | Validação por conjuntos de chaves; não define cardinalidade conceitual. |
| fuel_purchases_tratado.csv | trip_id | trips_tratado.csv | trip_id | 76939 | 0 | 0.00% | N:1 observado | OK | Validação por conjuntos de chaves; não define cardinalidade conceitual. |
| fuel_purchases_tratado.csv | truck_id | trucks_tratado.csv | truck_id | 92 | 0 | 0.00% | N:1 observado | OK | Validação por conjuntos de chaves; não define cardinalidade conceitual. |

## 11. Validação de duplicidades

| tabela | chave | total de registros | valores únicos | duplicados | status |
| --- | --- | --- | --- | --- | --- |
| customers_tratado.csv | customer_id | 200 | 200 | 0 | OK |
| loads_tratado.csv | load_id | 85410 | 85410 | 0 | OK |
| trips_tratado.csv | trip_id | 85410 | 85410 | 0 | OK |
| delivery_events_tratado.csv | event_id | 170820 | 170820 | 0 | OK |
| routes_tratado.csv | route_id | 58 | 58 | 0 | OK |
| fuel_purchases_tratado.csv | fuel_purchase_id | 196442 | 196442 | 0 | OK |
| trucks_tratado.csv | truck_id | 120 | 120 | 0 | OK |

## 12. Validação de domínios categóricos

| tabela | coluna | valores distintos | principais valores | status |
| --- | --- | --- | --- | --- |
| customers_tratado.csv | customer_type | 3 | Contract, Spot, Dedicated | OK |
| customers_tratado.csv | account_status | 2 | Active, Inactive | OK |
| customers_tratado.csv | primary_freight_type | 6 | Automotive, Food/Beverage, Retail, Electronics, Consumer Goods | OK |
| loads_tratado.csv | load_type | 2 | Refrigerated, Dry Van | OK |
| loads_tratado.csv | load_status | 1 | Completed | OK |
| loads_tratado.csv | booking_type | 3 | Dedicated, Contract, Spot | OK |
| trips_tratado.csv | trip_status | 1 | Completed | OK |
| delivery_events_tratado.csv | event_type | 2 | Pickup, Delivery | OK |
| delivery_events_tratado.csv | location_state | 19 | TX, MO, PA, OR, WA | OK |
| routes_tratado.csv | origin_state | 17 | TX, MO, OH, IL, PA | OK |
| routes_tratado.csv | destination_state | 18 | CA, OR, WA, TX, CO | OK |
| trucks_tratado.csv | make | 6 | Peterbilt, Freightliner, Mack, Volvo, International | OK |
| trucks_tratado.csv | fuel_type | 1 | Diesel | OK |
| trucks_tratado.csv | status | 3 | Active, Maintenance, Inactive | OK |
| trucks_tratado.csv | home_terminal | 24 | Dallas, Portland, Kansas City, Seattle, Miami | OK |

## 13. Validação de métricas e outliers simples

| tabela | campo | mínimo | máximo | média | mediana | valores negativos | zeros | status | observação |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| customers_tratado.csv | annual_revenue_potential | 101641 | 4990599 | 2688236.745 | 2784584.5 | 0 | 0 | OK | Sem alerta simples de valores negativos. |
| loads_tratado.csv | weight_lbs | 10000 | 45000 | 27477.495304999415 | 27482.0 | 0 | 0 | OK | Sem alerta simples de valores negativos. |
| loads_tratado.csv | pieces | 1 | 28 | 14.47053038285915 | 14.0 | 0 | 0 | OK | Sem alerta simples de valores negativos. |
| loads_tratado.csv | revenue | 125.93 | 8125.22 | 3073.7126834094365 | 2827.9849999999997 | 0 | 0 | OK | Sem alerta simples de valores negativos. |
| loads_tratado.csv | fuel_surcharge | 13.8 | 891.82 | 350.97211860437886 | 314.64 | 0 | 0 | OK | Sem alerta simples de valores negativos. |
| loads_tratado.csv | accessorial_charges | 0 | 200 | 71.64383561643835 | 50.0 | 0 | 32186 | OK | Sem alerta simples de valores negativos. |
| trips_tratado.csv | actual_distance_miles | 90 | 3391 | 1430.2681301955274 | 1297.5 | 0 | 0 | OK | Sem alerta simples de valores negativos. |
| trips_tratado.csv | actual_duration_hours | 1.4 | 67.8 | 25.01467392576982 | 23.0 | 0 | 0 | OK | Sem alerta simples de valores negativos. |
| trips_tratado.csv | fuel_gallons_used | 12.0 | 611.9 | 221.82742184755884 | 204.5 | 0 | 0 | OK | Sem alerta simples de valores negativos. |
| trips_tratado.csv | average_mpg | 5.5 | 7.5 | 6.5014625922023175 | 6.5 | 0 | 0 | OK | Sem alerta simples de valores negativos. |
| trips_tratado.csv | idle_time_hours | 2.0 | 12.0 | 7.010783280646295 | 7.0 | 0 | 0 | OK | Sem alerta simples de valores negativos. |
| delivery_events_tratado.csv | detention_minutes | 0 | 239 | 91.53746048472075 | 88.0 | 0 | 22472 | OK | Sem alerta simples de valores negativos. |
| routes_tratado.csv | typical_distance_miles | 92 | 3141 | 1391.5 | 1271.0 | 0 | 0 | OK | Sem alerta simples de valores negativos. |
| routes_tratado.csv | typical_transit_days | 1 | 5 | 2.1206896551724137 | 2.0 | 0 | 0 | OK | Sem alerta simples de valores negativos. |
| routes_tratado.csv | base_rate_per_mile | 1.52 | 2.79 | 2.1967241379310343 | 2.23 | 0 | 0 | OK | Sem alerta simples de valores negativos. |
| routes_tratado.csv | fuel_surcharge_rate | 0.15 | 0.34 | 0.24879310344827588 | 0.245 | 0 | 0 | OK | Sem alerta simples de valores negativos. |
| fuel_purchases_tratado.csv | gallons | 50.0 | 200.0 | 124.81565958399935 | 124.7 | 0 | 0 | OK | Sem alerta simples de valores negativos. |
| fuel_purchases_tratado.csv | price_per_gallon | 3.15 | 5.0 | 3.898418138687246 | 3.856 | 0 | 0 | OK | Sem alerta simples de valores negativos. |
| fuel_purchases_tratado.csv | total_cost | 158.5 | 997.9 | 486.62196495657753 | 480.66 | 0 | 0 | OK | Sem alerta simples de valores negativos. |
| trucks_tratado.csv | acquisition_mileage | 227 | 49556 | 26058.216666666667 | 26060.5 | 0 | 0 | OK | Sem alerta simples de valores negativos. |
| trucks_tratado.csv | tank_capacity_gallons | 150 | 250 | 201.66666666666666 | 200.0 | 0 | 0 | OK | Sem alerta simples de valores negativos. |

## 14. Validação de percentuais, taxas e preços unitários

| tabela | campo | mínimo | máximo | média | mediana | valores acima de 1 | interpretação provável | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| routes_tratado.csv | fuel_surcharge_rate | 0.15 | 0.34 | 0.24879310344827588 | 0.245 | 0 | percentual/taxa; escala precisa de validação humana | OK |
| routes_tratado.csv | base_rate_per_mile | 1.52 | 2.79 | 2.1967241379310343 | 2.23 | 58 | taxa monetária por milha, não percentual | OK |
| fuel_purchases_tratado.csv | price_per_gallon | 3.15 | 5.0 | 3.898418138687246 | 3.856 | 196442 | preço por galão, não percentual | OK |

## 15. Matriz geral de status

| tema | status |
| --- | --- |
| arquivos encontrados | OK |
| leitura dos arquivos | OK |
| preservação de linhas | OK |
| preservação de colunas | OK |
| mascaramento | OK |
| datas | OK |
| nulos | Atenção |
| tipos técnicos | OK |
| relacionamentos | OK |
| duplicidades | OK |
| domínios categóricos | OK |
| métricas | OK |
| taxas/percentuais | OK |

## 16. Pendências para a Etapa 05

- Relacionamentos aceitos.
- Granularidade das tabelas finais.
- Quais fatos e dimensões serão criados.
- Tratamento de nulos.
- Uso ou não de registros sem correspondência.
- Regras de agregação.
- Escala de percentuais.
- Campos mascarados que seguem para dados finais.
- Criação de dimensão calendário.

## 17. Decisão da Etapa 04

<!-- INICIO_VALIDACAO_HUMANA -->
Status da Etapa 04:

* [ ] Aprovada
* [x] Aprovada com ressalvas
* [ ] Reprovada para avanço

Observações da validação humana:

* A Etapa 04 está aprovada como validação somente leitura dos dados tratados.
* Nenhum dado bruto ou tratado foi alterado.
* Nenhum dado final, KPI final ou dashboard foi criado.
* Os 7 arquivos tratados do núcleo V1 foram encontrados, lidos e validados com sucesso.
* As linhas e colunas foram preservadas em todos os arquivos tratados.
* O mascaramento de `customer_name`, `fuel_card_number` e `vin` foi validado sem exposição dos valores originais.
* As datas convertidas foram validadas como legíveis e coerentes.
* As chaves principais não apresentaram duplicidades.
* Os relacionamentos candidatos avaliados não apresentaram valores sem correspondência.
* A única ressalva relevante envolve os nulos preservados em campos operacionais, especialmente `driver_id`, `truck_id` e `trailer_id`, que devem ter regra definida antes da criação dos dados finais.
* A Etapa 05 pode avançar, desde que trate explicitamente as decisões sobre granularidade, fatos, dimensões, nulos, relacionamentos, percentuais/taxas, regras de agregação e criação da dimensão calendário.
<!-- FIM_VALIDACAO_HUMANA -->


## 18. Confirmações finais

- Dados brutos preservados.
- Dados tratados preservados.
- Dados finais não criados.
- KPIs finais não criados.
- Dashboard não criado.
