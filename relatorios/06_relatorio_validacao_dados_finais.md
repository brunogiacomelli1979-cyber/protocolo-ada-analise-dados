# Relatório da Etapa 06 — Validação Final dos Dados Finais

Gerado em: 2026-06-24 07:56:30

## 1. Objetivo da Etapa 06

Validar os arquivos finais já criados para uso no Power BI, sem alterar nenhum CSV e sem criar KPIs finais complexos.

Python gera evidências. IA interpreta hipóteses. Humano valida decisões.

## 2. Confirmação de segurança

* dados brutos não foram lidos nem alterados;
* dados tratados não foram lidos nem alterados;
* dados finais foram apenas lidos em `dados/finais/`;
* nenhum CSV final foi alterado;
* nenhum KPI final complexo foi criado;
* nenhum dashboard foi criado.

## 3. Arquivos finais validados

| arquivo | caminho | existe | leitura | linhas | colunas | erro | status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| dim_clientes.csv | dados/finais/dim_clientes.csv | Sim | OK | 200 | 8 |  | OK |
| dim_rotas.csv | dados/finais/dim_rotas.csv | Sim | OK | 58 | 9 |  | OK |
| dim_caminhoes.csv | dados/finais/dim_caminhoes.csv | Sim | OK | 120 | 10 |  | OK |
| fato_cargas.csv | dados/finais/fato_cargas.csv | Sim | OK | 85410 | 12 |  | OK |
| fato_viagens.csv | dados/finais/fato_viagens.csv | Sim | OK | 85410 | 12 |  | OK |
| fato_eventos_entrega.csv | dados/finais/fato_eventos_entrega.csv | Sim | OK | 170820 | 11 |  | OK |
| fato_abastecimentos.csv | dados/finais/fato_abastecimentos.csv | Sim | OK | 196442 | 10 |  | OK |
| dim_calendario.csv | dados/finais/dim_calendario.csv | Sim | OK | 3630 | 9 |  | OK |

## 4. Estrutura dos arquivos finais

| arquivo | linhas | colunas | nomes das colunas | status |
| --- | --- | --- | --- | --- |
| dim_clientes.csv | 200 | 8 | customer_id, customer_name, customer_type, primary_freight_type, account_status, contract_start_date, credit_terms_days, annual_revenue_potential | OK |
| dim_rotas.csv | 58 | 9 | route_id, origin_city, origin_state, destination_city, destination_state, typical_distance_miles, base_rate_per_mile, fuel_surcharge_rate, typical_transit_days | OK |
| dim_caminhoes.csv | 120 | 10 | truck_id, unit_number, make, model_year, acquisition_date, acquisition_mileage, fuel_type, tank_capacity_gallons, status, home_terminal | OK |
| fato_cargas.csv | 85410 | 12 | load_id, customer_id, route_id, load_date, load_type, weight_lbs, pieces, revenue, fuel_surcharge, accessorial_charges, load_status, booking_type | OK |
| fato_viagens.csv | 85410 | 12 | trip_id, load_id, driver_id, truck_id, trailer_id, dispatch_date, actual_distance_miles, actual_duration_hours, fuel_gallons_used, average_mpg, idle_time_hours, trip_status | OK |
| fato_eventos_entrega.csv | 170820 | 11 | event_id, load_id, trip_id, event_type, facility_id, scheduled_datetime, actual_datetime, detention_minutes, on_time_flag, location_city, location_state | OK |
| fato_abastecimentos.csv | 196442 | 10 | fuel_purchase_id, trip_id, truck_id, driver_id, purchase_date, location_city, location_state, gallons, price_per_gallon, total_cost | OK |
| dim_calendario.csv | 3630 | 9 | data, ano, mes, nome_mes, trimestre, ano_mes, dia, dia_semana, nome_dia_semana | OK |

## 5. Validação de chaves

### Chaves únicas nas dimensões

| escopo | arquivo | chave | linhas | nulos | duplicidades | valores únicos | status | observação |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| dimensão | dim_clientes.csv | customer_id | 200 | 0 | 0 | 200 | OK | Chave sem nulos e sem duplicidades. |
| dimensão | dim_rotas.csv | route_id | 58 | 0 | 0 | 58 | OK | Chave sem nulos e sem duplicidades. |
| dimensão | dim_caminhoes.csv | truck_id | 120 | 0 | 0 | 120 | OK | Chave sem nulos e sem duplicidades. |
| dimensão | dim_calendario.csv | data | 3630 | 0 | 0 | 3630 | OK | Chave sem nulos e sem duplicidades. |

### Duplicidades em chaves relevantes das tabelas fato

| escopo | arquivo | chave | linhas | nulos | duplicidades | valores únicos | status | observação |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| fato | fato_cargas.csv | load_id | 85410 | 0 | 0 | 85410 | OK | Chave sem nulos e sem duplicidades. |
| fato | fato_viagens.csv | trip_id | 85410 | 0 | 0 | 85410 | OK | Chave sem nulos e sem duplicidades. |
| fato | fato_eventos_entrega.csv | event_id | 170820 | 0 | 0 | 170820 | OK | Chave sem nulos e sem duplicidades. |
| fato | fato_abastecimentos.csv | fuel_purchase_id | 196442 | 0 | 0 | 196442 | OK | Chave sem nulos e sem duplicidades. |

## 6. Validação de relacionamentos

| origem | coluna origem | destino | coluna destino | valores origem | sem correspondência | nulos origem | status | observação |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| fato_cargas.csv | customer_id | dim_clientes.csv | customer_id | 200 | 0 | 0 | OK | Sem nulos na chave de origem. |
| fato_cargas.csv | route_id | dim_rotas.csv | route_id | 58 | 0 | 0 | OK | Sem nulos na chave de origem. |
| fato_viagens.csv | load_id | fato_cargas.csv | load_id | 85410 | 0 | 0 | OK | Sem nulos na chave de origem. |
| fato_viagens.csv | truck_id | dim_caminhoes.csv | truck_id | 92 | 0 | 1672 | OK | Nulos preservados foram ignorados na correspondência. |
| fato_eventos_entrega.csv | trip_id | fato_viagens.csv | trip_id | 85410 | 0 | 0 | OK | Sem nulos na chave de origem. |
| fato_abastecimentos.csv | trip_id | fato_viagens.csv | trip_id | 76939 | 0 | 0 | OK | Sem nulos na chave de origem. |
| fato_abastecimentos.csv | truck_id | dim_caminhoes.csv | truck_id | 92 | 0 | 3880 | OK | Nulos preservados foram ignorados na correspondência. |

## 7. Validação da dimensão calendário

### Estrutura e período

| checagem | resultado | status |
| --- | --- | --- |
| coluna de data | coluna data encontrada | OK |
| datas inválidas | 0 | OK |
| datas duplicadas | 0 | OK |
| período mínimo | 2015-01-27 | OK |
| período máximo | 2025-01-03 | OK |

### Compatibilidade com datas das tabelas fato

| arquivo | coluna | menor data | maior data | datas fora do calendário | datas inválidas | status |
| --- | --- | --- | --- | --- | --- | --- |
| fato_cargas.csv | load_date | 2022-01-01 | 2024-12-31 | 0 | 0 | OK |
| fato_viagens.csv | dispatch_date | 2022-01-01 | 2024-12-31 | 0 | 0 | OK |
| fato_eventos_entrega.csv | scheduled_datetime | 2022-01-01 | 2025-01-02 | 0 | 0 | OK |
| fato_eventos_entrega.csv | actual_datetime | 2022-01-01 | 2025-01-03 | 0 | 0 | OK |
| fato_abastecimentos.csv | purchase_date | 2022-01-01 | 2025-01-02 | 0 | 0 | OK |

## 8. Validação de campos sensíveis

| arquivo | campo | regra | resultado | status |
| --- | --- | --- | --- | --- |
| dim_caminhoes.csv | vin | não deve existir nos dados finais | Ausente | OK |
| fato_abastecimentos.csv | fuel_card_number | não deve existir nos dados finais | Ausente | OK |
| dim_clientes.csv | customer_name | se existir, deve estar mascarado | 0 valores fora do padrão Cliente_### | OK |

## 9. Nulos e pontos de atenção

Nulos operacionais foram preservados como evidência; esta etapa não aplica imputação, remoção de linhas ou correção automática.

| arquivo | coluna | linhas | nulos | percentual | status | observação |
| --- | --- | --- | --- | --- | --- | --- |
| fato_viagens.csv | driver_id | 85410 | 1714 | 2.01% | Atenção | Nulos preservados; validar interpretação no Power BI. |
| fato_viagens.csv | truck_id | 85410 | 1672 | 1.96% | Atenção | Nulos preservados; validar interpretação no Power BI. |
| fato_viagens.csv | trailer_id | 85410 | 1680 | 1.97% | Atenção | Nulos preservados; validar interpretação no Power BI. |
| fato_abastecimentos.csv | driver_id | 196442 | 3988 | 2.03% | Atenção | Nulos preservados; validar interpretação no Power BI. |
| fato_abastecimentos.csv | truck_id | 196442 | 3880 | 1.98% | Atenção | Nulos preservados; validar interpretação no Power BI. |
| fato_eventos_entrega.csv | actual_datetime | 170820 | 0 | 0.00% | OK | Sem nulos observados. |

## 10. Campos com risco de agregação indevida no Power BI

| arquivo | campo | existe | risco | status |
| --- | --- | --- | --- | --- |
| fato_viagens.csv | average_mpg | Sim | Media operacional; usar media ponderada ou regra validada, nunca soma simples. | Atenção |
| fato_abastecimentos.csv | price_per_gallon | Sim | Preco unitario; usar media ponderada por galoes ou regra validada. | Atenção |
| dim_rotas.csv | base_rate_per_mile | Sim | Taxa por milha; nao representa valor total da rota. | Atenção |
| dim_rotas.csv | fuel_surcharge_rate | Sim | Taxa/percentual; confirmar escala e formatacao no Power BI. | Atenção |

## 11. Matriz geral de status

| tema | status |
| --- | --- |
| existência e leitura dos arquivos finais | OK |
| estrutura dos arquivos finais | OK |
| chaves das dimensões | OK |
| duplicidades nas tabelas fato | OK |
| relacionamentos esperados | OK |
| dimensão calendário | OK |
| cobertura temporal das fatos | OK |
| campos sensíveis | OK |
| nulos operacionais preservados | Atenção |
| campos com risco de agregação indevida | Atenção |

## 12. Limitações da validação

* A validação é estrutural e relacional; não substitui validação de regras de negócio pelo usuário.
* A etapa não recalcula KPIs finais, métricas gerenciais ou medidas DAX.
* A etapa não avalia layout, performance ou interações do Power BI.
* A dimensão calendário foi validada por cobertura geral das datas disponíveis, sem calendário fiscal ou feriados.
* Nulos operacionais foram apenas registrados, não corrigidos.

## 13. Recomendação para avanço

Avançar para documentação de KPIs e modelagem no Power BI com ressalvas de atenção aos nulos operacionais e aos campos que não devem ser somados diretamente.

## 14. Decisão da Etapa 06

<!-- INICIO_VALIDACAO_HUMANA -->
Status da Etapa 06:

* [ ] Aprovada
* [x] Aprovada com ressalvas
* [ ] Reprovada para avanço

Observações da validação humana:

* A Etapa 06 está aprovada como validação final dos dados finais para Power BI.
* Foram validados 8 arquivos finais em `dados/finais/`, sem alteração de dados brutos, tratados ou finais.
* A validação confirmou existência, leitura, estrutura, chaves, duplicidades, relacionamentos esperados, dimensão calendário e tratamento de campos sensíveis.
* Não foram encontrados alertas críticos.
* Os alertas de atenção não impedem o avanço, mas devem ser considerados na modelagem do Power BI.
* Os nulos operacionais em `driver_id`, `truck_id` e `trailer_id` foram preservados e não devem ser imputados automaticamente.
* Os campos `average_mpg`, `price_per_gallon`, `base_rate_per_mile` e `fuel_surcharge_rate` exigem regra de agregação específica e não devem ser somados diretamente.
* A próxima etapa pode avançar para definição de perguntas analíticas, KPIs e regras de modelagem para Power BI.


Observações da validação humana:

* A preencher.
<!-- FIM_VALIDACAO_HUMANA -->

## 15. Confirmações finais

* Etapa 06 concluída como validação final dos dados finais;
* arquivos finais validados: 8 de 8;
* alertas OK: 45;
* alertas Atenção: 9;
* alertas Crítico: 0;
* nenhum dado bruto, tratado ou final foi alterado;
* nenhum dashboard foi criado;
* nenhum KPI final complexo foi criado.
