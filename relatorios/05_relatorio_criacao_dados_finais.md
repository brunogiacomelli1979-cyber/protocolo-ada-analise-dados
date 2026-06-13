# Relatório da Etapa 05 — Criação dos Dados Finais para Power BI

## 1. Objetivo da etapa

Esta etapa cria os arquivos finais para Power BI a partir dos dados tratados validados nas etapas anteriores do Protocolo ADA.

Python gera evidências. IA interpreta hipóteses. Humano valida decisões.

## 2. Confirmação de segurança

* dados brutos não foram alterados;
* dados tratados não foram alterados;
* dados finais foram criados em `dados/finais/`;
* nenhum dashboard foi criado;
* nenhum KPI final complexo foi criado;
* nenhuma imputação automática foi feita.

## 3. Fontes utilizadas

Arquivos tratados utilizados:
* `dados/tratados/customers_tratado.csv`
* `dados/tratados/routes_tratado.csv`
* `dados/tratados/trucks_tratado.csv`
* `dados/tratados/loads_tratado.csv`
* `dados/tratados/trips_tratado.csv`
* `dados/tratados/delivery_events_tratado.csv`
* `dados/tratados/fuel_purchases_tratado.csv`

Relatórios de referência:
* `relatorios/02_plano_tratamento_dados.md`
* `relatorios/03_relatorio_tratamento_padronizacao.md`
* `relatorios/04_relatorio_validacao_dados_tratados.md`
* `relatorios/04_1_checklist_decisao_etapa_05.md`

Checklist de decisão utilizado:

* `relatorios/04_1_checklist_decisao_etapa_05.md`

## 4. Arquivos finais criados

| arquivo final | origem | granularidade | linhas | colunas | status |
|---|---|---|---:|---:|---|
| `dim_clientes.csv` | customers_tratado.csv | uma linha por customer_id | 200 | 8 | OK |
| `dim_rotas.csv` | routes_tratado.csv | uma linha por route_id | 58 | 9 | OK |
| `dim_caminhoes.csv` | trucks_tratado.csv | uma linha por truck_id | 120 | 10 | OK |
| `fato_cargas.csv` | loads_tratado.csv | uma linha por load_id | 85410 | 12 | OK |
| `fato_viagens.csv` | trips_tratado.csv | uma linha por trip_id | 85410 | 12 | OK |
| `fato_eventos_entrega.csv` | delivery_events_tratado.csv | uma linha por event_id | 170820 | 11 | OK |
| `fato_abastecimentos.csv` | fuel_purchases_tratado.csv | uma linha por fuel_purchase_id | 196442 | 10 | OK |
| `dim_calendario.csv` | datas do núcleo final V1 | uma linha por data | 3630 | 9 | OK |

## 5. Estrutura das dimensões

### dim_clientes.csv

* origem: `customers_tratado.csv`;
* chave: `customer_id`;
* granularidade: uma linha por customer_id;
* colunas: `customer_id`, `customer_name`, `customer_type`, `primary_freight_type`, `account_status`, `contract_start_date`, `credit_terms_days`, `annual_revenue_potential`;
* campos sensíveis removidos ou mantidos mascarados: `customer_name` mantido mascarado.;
* observações: customer_name mantido mascarado.

### dim_rotas.csv

* origem: `routes_tratado.csv`;
* chave: `route_id`;
* granularidade: uma linha por route_id;
* colunas: `route_id`, `origin_city`, `origin_state`, `destination_city`, `destination_state`, `typical_distance_miles`, `base_rate_per_mile`, `fuel_surcharge_rate`, `typical_transit_days`;
* campos sensíveis removidos ou mantidos mascarados: nenhum campo sensível identificado para remoção na V1.;
* observações: Taxas preservadas na escala original.

### dim_caminhoes.csv

* origem: `trucks_tratado.csv`;
* chave: `truck_id`;
* granularidade: uma linha por truck_id;
* colunas: `truck_id`, `unit_number`, `make`, `model_year`, `acquisition_date`, `acquisition_mileage`, `fuel_type`, `tank_capacity_gallons`, `status`, `home_terminal`;
* campos sensíveis removidos ou mantidos mascarados: `vin` removido.;
* observações: vin removido dos dados finais.

## 6. Estrutura das tabelas fato

### fato_cargas.csv

* origem: `loads_tratado.csv`;
* chave: `load_id`;
* granularidade: uma linha por load_id;
* colunas: `load_id`, `customer_id`, `route_id`, `load_date`, `load_type`, `weight_lbs`, `pieces`, `revenue`, `fuel_surcharge`, `accessorial_charges`, `load_status`, `booking_type`;
* nulos preservados: sem nulos operacionais destacados.;
* campos que não devem ser somados diretamente: sem restrição específica além de validar regras de negócio para valores financeiros.;
* observações: sem observações adicionais.

### fato_viagens.csv

* origem: `trips_tratado.csv`;
* chave: `trip_id`;
* granularidade: uma linha por trip_id;
* colunas: `trip_id`, `load_id`, `driver_id`, `truck_id`, `trailer_id`, `dispatch_date`, `actual_distance_miles`, `actual_duration_hours`, `fuel_gallons_used`, `average_mpg`, `idle_time_hours`, `trip_status`;
* nulos preservados: `driver_id`: 1714; `truck_id`: 1672; `trailer_id`: 1680;
* campos que não devem ser somados diretamente: `average_mpg`.;
* observações: Nulos operacionais preservados; average_mpg não deve ser somado diretamente.

### fato_eventos_entrega.csv

* origem: `delivery_events_tratado.csv`;
* chave: `event_id`;
* granularidade: uma linha por event_id;
* colunas: `event_id`, `load_id`, `trip_id`, `event_type`, `facility_id`, `scheduled_datetime`, `actual_datetime`, `detention_minutes`, `on_time_flag`, `location_city`, `location_state`;
* nulos preservados: sem nulos operacionais destacados.;
* campos que não devem ser somados diretamente: não criar KPI de pontualidade diretamente nesta etapa.;
* observações: on_time_flag preservado; KPI de pontualidade não foi criado.

### fato_abastecimentos.csv

* origem: `fuel_purchases_tratado.csv`;
* chave: `fuel_purchase_id`;
* granularidade: uma linha por fuel_purchase_id;
* colunas: `fuel_purchase_id`, `trip_id`, `truck_id`, `driver_id`, `purchase_date`, `location_city`, `location_state`, `gallons`, `price_per_gallon`, `total_cost`;
* nulos preservados: `driver_id`: 3988; `truck_id`: 3880;
* campos que não devem ser somados diretamente: `price_per_gallon`.;
* observações: fuel_card_number removido; price_per_gallon não deve ser somado diretamente.

## 7. Dimensão calendário

* menor data usada: `2015-01-27`;
* maior data usada: `2025-01-03`;
* quantidade de datas criadas: 3630;
* campos criados: `data`, `ano`, `mes`, `nome_mes`, `trimestre`, `ano_mes`, `dia`, `dia_semana`, `nome_dia_semana`;
* observações: calendário criado sem feriados e sem calendário fiscal.

## 8. Campos sensíveis e decisões aplicadas

| campo | origem | decisão | ação aplicada | justificativa | status |
|---|---|---|---|---|---|
| `customer_name` | customers_tratado.csv | manter mascarado | mantido em dim_clientes.csv | Permite segmentação sem expor o nome original do cliente. | OK |
| `vin` | trucks_tratado.csv | remover dos dados finais | removido de dim_caminhoes.csv | Identificador operacional sem valor analítico público para a V1. | OK |
| `fuel_card_number` | fuel_purchases_tratado.csv | remover dos dados finais | removido de fato_abastecimentos.csv | Reduz risco de exposição e não agrega valor analítico público. | OK |

## 9. Nulos preservados

| tabela final | coluna | nulos preservados | percentual | justificativa |
|---|---|---:|---:|---|
| `fato_viagens.csv` | `driver_id` | 1714 | 2.01% | Nulo preservado; sem imputação automática e sem remoção de registros. |
| `fato_viagens.csv` | `truck_id` | 1672 | 1.96% | Nulo preservado; sem imputação automática e sem remoção de registros. |
| `fato_viagens.csv` | `trailer_id` | 1680 | 1.97% | Nulo preservado; sem imputação automática e sem remoção de registros. |
| `fato_abastecimentos.csv` | `driver_id` | 3988 | 2.03% | Nulo preservado; sem imputação automática e sem remoção de registros. |
| `fato_abastecimentos.csv` | `truck_id` | 3880 | 1.98% | Nulo preservado; sem imputação automática e sem remoção de registros. |

## 10. Relacionamentos esperados para Power BI

| tabela origem | coluna origem | tabela destino | coluna destino | tipo esperado | valores sem correspondência | status | observação |
|---|---|---|---|---|---:|---|---|
| `fato_cargas.csv` | `customer_id` | `dim_clientes.csv` | `customer_id` | muitos para um | 0 | OK | Sem nulos na coluna de relacionamento. |
| `fato_cargas.csv` | `route_id` | `dim_rotas.csv` | `route_id` | muitos para um | 0 | OK | Sem nulos na coluna de relacionamento. |
| `fato_viagens.csv` | `load_id` | `fato_cargas.csv` | `load_id` | 1:1 observado; validar no modelo | 0 | OK | Sem nulos na coluna de relacionamento. |
| `fato_viagens.csv` | `truck_id` | `dim_caminhoes.csv` | `truck_id` | muitos para um | 0 | OK | Nulos ignorados na correspondência e preservados no arquivo final. |
| `fato_eventos_entrega.csv` | `trip_id` | `fato_viagens.csv` | `trip_id` | muitos para um | 0 | OK | Sem nulos na coluna de relacionamento. |
| `fato_eventos_entrega.csv` | `load_id` | `fato_cargas.csv` | `load_id` | muitos para um | 0 | OK | Sem nulos na coluna de relacionamento. |
| `fato_abastecimentos.csv` | `trip_id` | `fato_viagens.csv` | `trip_id` | muitos para um | 0 | OK | Sem nulos na coluna de relacionamento. |
| `fato_abastecimentos.csv` | `truck_id` | `dim_caminhoes.csv` | `truck_id` | muitos para um | 0 | OK | Nulos ignorados na correspondência e preservados no arquivo final. |

## 11. Validações pós-criação

| arquivo | chave principal | duplicidades | linhas | colunas | status |
|---|---|---:|---:|---:|---|
| `dim_clientes.csv` | `customer_id` | 0 | 200 | 8 | OK |
| `dim_rotas.csv` | `route_id` | 0 | 58 | 9 | OK |
| `dim_caminhoes.csv` | `truck_id` | 0 | 120 | 10 | OK |
| `fato_cargas.csv` | `load_id` | 0 | 85410 | 12 | OK |
| `fato_viagens.csv` | `trip_id` | 0 | 85410 | 12 | OK |
| `fato_eventos_entrega.csv` | `event_id` | 0 | 170820 | 11 | OK |
| `fato_abastecimentos.csv` | `fuel_purchase_id` | 0 | 196442 | 10 | OK |
| `dim_calendario.csv` | `data` | 0 | 3630 | 9 | OK |

## 12. Pontos de atenção para Power BI

* não somar `average_mpg`;
* não somar `price_per_gallon`;
* não somar `base_rate_per_mile`;
* não somar `fuel_surcharge_rate`;
* formatar `fuel_surcharge_rate` como percentual no Power BI, se confirmado;
* formatar campos financeiros como moeda no Power BI;
* usar dimensão calendário para filtros temporais;
* revisar nulos preservados em relacionamentos.

## 13. Pendências para próxima etapa

* validação final dos dados finais;
* documentação dos KPIs;
* criação das medidas no Power BI;
* definição dos visuais;
* criação do dashboard.

## 14. Decisão da Etapa 05

Status da Etapa 05:

* [ ] Aprovada
* [x] Aprovada com ressalvas
* [ ] Reprovada para avanço

Observações da validação humana:

* A Etapa 05 está aprovada como criação inicial dos dados finais para Power BI.
* Os dados brutos e os dados tratados foram preservados.
* Os arquivos finais foram criados em `dados/finais/`, separados por granularidade em tabelas fato, dimensões e dimensão calendário.
* Foram criados os arquivos `dim_clientes.csv`, `dim_rotas.csv`, `dim_caminhoes.csv`, `fato_cargas.csv`, `fato_viagens.csv`, `fato_eventos_entrega.csv`, `fato_abastecimentos.csv` e `dim_calendario.csv`.
* Os campos sensíveis foram tratados conforme decisão de governança: `customer_name` foi mantido mascarado, `vin` foi removido e `fuel_card_number` foi removido.
* Nenhum dashboard foi criado e nenhum KPI final complexo foi calculado nesta etapa.
* As ressalvas para a próxima etapa envolvem a validação final dos dados finais, documentação dos KPIs, definição das medidas no Power BI, cuidado com nulos preservados e atenção para campos que não devem ser somados diretamente, como `average_mpg`, `price_per_gallon`, `base_rate_per_mile` e `fuel_surcharge_rate`.


## 15. Confirmações finais

* dados brutos preservados;
* dados tratados preservados;
* arquivos finais criados;
* dashboard não criado;
* KPIs finais complexos não criados.
