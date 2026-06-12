# Relatório da Etapa 01 — Inspeção Segura e Interpretação Inicial dos Dados Brutos

Gerado em: 2026-06-12 17:27:42

## 1. Objetivo da etapa

Esta etapa tem como objetivo compreender a estrutura técnica dos dados brutos, gerar evidências objetivas com Python, apoiar a interpretação com IA e preparar a base para validação humana antes do plano de tratamento.

Python gera evidências. IA interpreta hipóteses. Humano valida decisões.

## 2. Confirmação de segurança

- Dados brutos não foram alterados.
- Nenhuma transformação foi aplicada.
- Nenhum dado tratado foi criado.
- Nenhum KPI final foi criado.
- Nenhum dashboard foi gerado.
- As classificações são hipóteses iniciais.
- Nenhuma decisão de tratamento foi tomada.

## 3. Documentação da base

- Nome do arquivo: `DATABASE_SCHEMA.txt`
- Quantidade de linhas: 87
- Quantidade de caracteres: 2750
- Observação: este arquivo será usado apenas como apoio, não como fonte única de decisão.

## 4. Inventário dos arquivos brutos

| Arquivo | Linhas | Colunas | Registros únicos por possível chave | Papel provável na base | Evidências usadas | Nível de confiança | Observação inicial |
| --- | --- | --- | --- | --- | --- | --- | --- |
| customers.csv | 200 | 8 | 200 | possível dimensão de clientes | presença de data, chave identificadora provável, métricas numéricas, atributos categóricos | alto | Hipótese inicial; requer validação humana. |
| delivery_events.csv | 170820 | 11 | 170820 | possível tabela de eventos | muitas linhas, presença de data, presença de IDs externos, chave identificadora provável, métricas numéricas, atributos categóricos | alto | Hipótese inicial; requer validação humana. |
| driver_monthly_metrics.csv | 4464 | 9 | Não identificada | possível tabela agregada mensal por motorista | chave identificadora provável, métricas numéricas, métricas consolidadas ou derivadas, atributos categóricos | alto | Hipótese inicial; requer validação humana. |
| drivers.csv | 150 | 12 | 150 | possível dimensão de motoristas, com dados pessoais | presença de data, chave identificadora provável, métricas numéricas, atributos categóricos | alto | Hipótese inicial; requer validação humana. |
| facilities.csv | 50 | 9 | 50 | possível dimensão de instalações | chave identificadora provável, métricas numéricas, atributos categóricos | alto | Hipótese inicial; requer validação humana. |
| fuel_purchases.csv | 196442 | 11 | 196442 | possível tabela fato/transacional de abastecimentos | muitas linhas, presença de data, presença de IDs externos, chave identificadora provável, métricas numéricas, métricas consolidadas ou derivadas, atributos categóricos | alto | Hipótese inicial; requer validação humana. |
| loads.csv | 85410 | 12 | 85410 | possível tabela fato operacional | muitas linhas, presença de data, presença de IDs externos, chave identificadora provável, métricas numéricas, atributos categóricos | alto | Hipótese inicial; requer validação humana. |
| maintenance_records.csv | 2920 | 12 | 2920 | possível tabela fato/evento de manutenção | presença de data, presença de IDs externos, chave identificadora provável, métricas numéricas, métricas consolidadas ou derivadas, atributos categóricos | alto | Hipótese inicial; requer validação humana. |
| routes.csv | 58 | 9 | 58 | possível dimensão de rotas | chave identificadora provável, métricas numéricas, métricas consolidadas ou derivadas, atributos categóricos | alto | Hipótese inicial; requer validação humana. |
| safety_incidents.csv | 170 | 15 | 170 | possível tabela fato/evento de incidentes | presença de data, presença de IDs externos, chave identificadora provável, métricas numéricas, atributos categóricos | alto | Hipótese inicial; requer validação humana. |
| trailers.csv | 180 | 9 | 180 | possível dimensão de carretas/equipamentos | presença de data, chave identificadora provável, métricas numéricas, atributos categóricos | alto | Hipótese inicial; requer validação humana. |
| trips.csv | 85410 | 12 | 85410 | possível tabela fato operacional | muitas linhas, presença de data, presença de IDs externos, chave identificadora provável, métricas numéricas, métricas consolidadas ou derivadas, atributos categóricos | alto | Hipótese inicial; requer validação humana. |
| truck_utilization_metrics.csv | 3312 | 10 | Não identificada | possível tabela agregada mensal por caminhão | chave identificadora provável, métricas numéricas, métricas consolidadas ou derivadas, atributos categóricos | alto | Hipótese inicial; requer validação humana. |
| trucks.csv | 120 | 11 | 120 | possível dimensão de caminhões/frota | presença de data, chave identificadora provável, métricas numéricas, atributos categóricos | alto | Hipótese inicial; requer validação humana. |

## 5. Inspeção técnica por arquivo

### Arquivo: `customers.csv`

**Quantidade de linhas:** 200

**Quantidade de colunas:** 8

**Lista de colunas:**

- `customer_id`
- `customer_name`
- `customer_type`
- `credit_terms_days`
- `primary_freight_type`
- `account_status`
- `contract_start_date`
- `annual_revenue_potential`

**Tipos pandas:**

| Coluna | Tipo pandas |
| --- | --- |
| customer_id | str |
| customer_name | str |
| customer_type | str |
| credit_terms_days | int64 |
| primary_freight_type | str |
| account_status | str |
| contract_start_date | str |
| annual_revenue_potential | int64 |

**Valores nulos por coluna:**

| Coluna | Valores nulos | Percentual de nulos |
| --- | --- | --- |
| customer_id | 0 | 0.00% |
| customer_name | 0 | 0.00% |
| customer_type | 0 | 0.00% |
| credit_terms_days | 0 | 0.00% |
| primary_freight_type | 0 | 0.00% |
| account_status | 0 | 0.00% |
| contract_start_date | 0 | 0.00% |
| annual_revenue_potential | 0 | 0.00% |

**Quantidade de linhas duplicadas:** 0

**Possíveis IDs:** customer_id

**Possíveis datas:** contract_start_date

**Possíveis campos numéricos:** credit_terms_days, annual_revenue_potential

**Possíveis campos categóricos:** customer_type, primary_freight_type, account_status

**Possíveis booleanos:** nenhum identificado automaticamente

**Possíveis financeiros:** annual_revenue_potential

**Possíveis percentuais ou taxas:** nenhum identificado automaticamente

**Possíveis métricas de tempo/duração:** credit_terms_days

**Amostra controlada de até 3 linhas:**

| customer_id | customer_name | customer_type | credit_terms_days | primary_freight_type | account_status | contract_start_date | annual_revenue_potential |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CUST00001 | Metro Wholesale | Dedicated | 60 | General | Inactive | 2020-02-20 | 985117 |
| CUST00002 | National Retail | Contract | 30 | Retail | Active | 2021-06-02 | 4936566 |
| CUST00003 | XYZ Industries | Contract | 30 | Consumer Goods | Active | 2020-09-04 | 3102814 |

### Arquivo: `delivery_events.csv`

**Quantidade de linhas:** 170820

**Quantidade de colunas:** 11

**Lista de colunas:**

- `event_id`
- `load_id`
- `trip_id`
- `event_type`
- `facility_id`
- `scheduled_datetime`
- `actual_datetime`
- `detention_minutes`
- `on_time_flag`
- `location_city`
- `location_state`

**Tipos pandas:**

| Coluna | Tipo pandas |
| --- | --- |
| event_id | str |
| load_id | str |
| trip_id | str |
| event_type | str |
| facility_id | str |
| scheduled_datetime | str |
| actual_datetime | str |
| detention_minutes | int64 |
| on_time_flag | bool |
| location_city | str |
| location_state | str |

**Valores nulos por coluna:**

| Coluna | Valores nulos | Percentual de nulos |
| --- | --- | --- |
| event_id | 0 | 0.00% |
| load_id | 0 | 0.00% |
| trip_id | 0 | 0.00% |
| event_type | 0 | 0.00% |
| facility_id | 0 | 0.00% |
| scheduled_datetime | 0 | 0.00% |
| actual_datetime | 0 | 0.00% |
| detention_minutes | 0 | 0.00% |
| on_time_flag | 0 | 0.00% |
| location_city | 0 | 0.00% |
| location_state | 0 | 0.00% |

**Quantidade de linhas duplicadas:** 0

**Possíveis IDs:** event_id, load_id, trip_id, facility_id

**Possíveis datas:** scheduled_datetime, actual_datetime

**Possíveis campos numéricos:** detention_minutes

**Possíveis campos categóricos:** event_type, location_city, location_state

**Possíveis booleanos:** on_time_flag

**Possíveis financeiros:** nenhum identificado automaticamente

**Possíveis percentuais ou taxas:** nenhum identificado automaticamente

**Possíveis métricas de tempo/duração:** detention_minutes

**Amostra controlada de até 3 linhas:**

| event_id | load_id | trip_id | event_type | facility_id | scheduled_datetime | actual_datetime | detention_minutes | on_time_flag | location_city | location_state |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EVT00000001 | LOAD00000001 | TRIP00000001 | Pickup | FAC00034 | 2022-01-01 18:00:00.000000 | 2022-01-01 20:58:55.918185 | 0 | False | Houston | TX |
| EVT00000002 | LOAD00000001 | TRIP00000001 | Delivery | FAC00046 | 2022-01-02 23:10:55.918185 | 2022-01-02 21:30:22.142060 | 230 | True | Detroit | MI |
| EVT00000003 | LOAD00000002 | TRIP00000002 | Pickup | FAC00015 | 2022-01-01 18:00:00.000000 | 2022-01-01 17:37:26.608430 | 62 | True | Kansas City | MO |

### Arquivo: `driver_monthly_metrics.csv`

**Quantidade de linhas:** 4464

**Quantidade de colunas:** 9

**Lista de colunas:**

- `driver_id`
- `month`
- `trips_completed`
- `total_miles`
- `total_revenue`
- `average_mpg`
- `total_fuel_gallons`
- `on_time_delivery_rate`
- `average_idle_hours`

**Tipos pandas:**

| Coluna | Tipo pandas |
| --- | --- |
| driver_id | str |
| month | str |
| trips_completed | int64 |
| total_miles | int64 |
| total_revenue | float64 |
| average_mpg | float64 |
| total_fuel_gallons | float64 |
| on_time_delivery_rate | float64 |
| average_idle_hours | float64 |

**Valores nulos por coluna:**

| Coluna | Valores nulos | Percentual de nulos |
| --- | --- | --- |
| driver_id | 0 | 0.00% |
| month | 0 | 0.00% |
| trips_completed | 0 | 0.00% |
| total_miles | 0 | 0.00% |
| total_revenue | 0 | 0.00% |
| average_mpg | 0 | 0.00% |
| total_fuel_gallons | 0 | 0.00% |
| on_time_delivery_rate | 0 | 0.00% |
| average_idle_hours | 0 | 0.00% |

**Quantidade de linhas duplicadas:** 0

**Possíveis IDs:** driver_id

**Possíveis datas:** nenhuma identificada automaticamente

**Possíveis campos numéricos:** trips_completed, total_miles, total_revenue, average_mpg, total_fuel_gallons, on_time_delivery_rate, average_idle_hours

**Possíveis campos categóricos:** month

**Possíveis booleanos:** nenhum identificado automaticamente

**Possíveis financeiros:** total_revenue

**Possíveis percentuais ou taxas:** on_time_delivery_rate

**Possíveis métricas de tempo/duração:** average_idle_hours

**Amostra controlada de até 3 linhas:**

| driver_id | month | trips_completed | total_miles | total_revenue | average_mpg | total_fuel_gallons | on_time_delivery_rate | average_idle_hours |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DRV00001 | 2022-01-01 | 26 | 36620 | 79141.59 | 6.61 | 5574.7 | 0.385 | 8.2 |
| DRV00001 | 2022-02-01 | 9 | 13515 | 27133.87 | 6.69 | 2095.1 | 0.333 | 6.8 |
| DRV00001 | 2022-03-01 | 20 | 30361 | 62399.62 | 6.36 | 4792.2 | 0.55 | 7.5 |

### Arquivo: `drivers.csv`

**Quantidade de linhas:** 150

**Quantidade de colunas:** 12

**Lista de colunas:**

- `driver_id`
- `first_name`
- `last_name`
- `hire_date`
- `termination_date`
- `license_number`
- `license_state`
- `date_of_birth`
- `home_terminal`
- `employment_status`
- `cdl_class`
- `years_experience`

**Tipos pandas:**

| Coluna | Tipo pandas |
| --- | --- |
| driver_id | str |
| first_name | str |
| last_name | str |
| hire_date | str |
| termination_date | str |
| license_number | str |
| license_state | str |
| date_of_birth | str |
| home_terminal | str |
| employment_status | str |
| cdl_class | str |
| years_experience | int64 |

**Valores nulos por coluna:**

| Coluna | Valores nulos | Percentual de nulos |
| --- | --- | --- |
| driver_id | 0 | 0.00% |
| first_name | 0 | 0.00% |
| last_name | 0 | 0.00% |
| hire_date | 0 | 0.00% |
| termination_date | 124 | 82.67% |
| license_number | 0 | 0.00% |
| license_state | 0 | 0.00% |
| date_of_birth | 0 | 0.00% |
| home_terminal | 0 | 0.00% |
| employment_status | 0 | 0.00% |
| cdl_class | 0 | 0.00% |
| years_experience | 0 | 0.00% |

**Quantidade de linhas duplicadas:** 0

**Possíveis IDs:** driver_id

**Possíveis datas:** hire_date, termination_date, date_of_birth

**Possíveis campos numéricos:** years_experience

**Possíveis campos categóricos:** license_state, home_terminal, employment_status, cdl_class

**Possíveis booleanos:** nenhum identificado automaticamente

**Possíveis financeiros:** nenhum identificado automaticamente

**Possíveis percentuais ou taxas:** nenhum identificado automaticamente

**Possíveis métricas de tempo/duração:** years_experience

**Amostra controlada de até 3 linhas:**

| driver_id | first_name | last_name | hire_date | termination_date | license_number | license_state | date_of_birth | home_terminal | employment_status | cdl_class | years_experience |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DRV00001 | Jennifer | Hernandez | 2014-10-31 |  | DL673510887 | WA | 1973-11-07 | Denver | Active | A | 3 |
| DRV00002 | William | Martin | 2020-10-02 |  | DL128955006 | GA | 1976-11-03 | Columbus | Active | A | 20 |
| DRV00003 | Charles | Hernandez | 2021-09-21 |  | DL523076025 | NC | 1970-04-06 | Salt Lake City | Active | A | 19 |

### Arquivo: `facilities.csv`

**Quantidade de linhas:** 50

**Quantidade de colunas:** 9

**Lista de colunas:**

- `facility_id`
- `facility_name`
- `facility_type`
- `city`
- `state`
- `latitude`
- `longitude`
- `dock_doors`
- `operating_hours`

**Tipos pandas:**

| Coluna | Tipo pandas |
| --- | --- |
| facility_id | str |
| facility_name | str |
| facility_type | str |
| city | str |
| state | str |
| latitude | float64 |
| longitude | float64 |
| dock_doors | int64 |
| operating_hours | str |

**Valores nulos por coluna:**

| Coluna | Valores nulos | Percentual de nulos |
| --- | --- | --- |
| facility_id | 0 | 0.00% |
| facility_name | 0 | 0.00% |
| facility_type | 0 | 0.00% |
| city | 0 | 0.00% |
| state | 0 | 0.00% |
| latitude | 0 | 0.00% |
| longitude | 0 | 0.00% |
| dock_doors | 0 | 0.00% |
| operating_hours | 0 | 0.00% |

**Quantidade de linhas duplicadas:** 0

**Possíveis IDs:** facility_id

**Possíveis datas:** nenhuma identificada automaticamente

**Possíveis campos numéricos:** dock_doors

**Possíveis campos categóricos:** facility_type, city, state, operating_hours

**Possíveis booleanos:** nenhum identificado automaticamente

**Possíveis financeiros:** nenhum identificado automaticamente

**Possíveis percentuais ou taxas:** nenhum identificado automaticamente

**Possíveis métricas de tempo/duração:** nenhuma identificada automaticamente

**Amostra controlada de até 3 linhas:**

| facility_id | facility_name | facility_type | city | state | latitude | longitude | dock_doors | operating_hours |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FAC00001 | Houston Distribution Center | Cross-Dock | Houston | TX | 29.7604 | -95.3698 | 125 | 24/7 |
| FAC00002 | Kansas City Hub | Cross-Dock | Kansas City | MO | 39.0997 | -94.5786 | 33 | 7AM-7PM |
| FAC00003 | Charlotte Distribution Center | Distribution Center | Charlotte | NC | 35.2271 | -80.8431 | 138 | 24/7 |

### Arquivo: `fuel_purchases.csv`

**Quantidade de linhas:** 196442

**Quantidade de colunas:** 11

**Lista de colunas:**

- `fuel_purchase_id`
- `trip_id`
- `truck_id`
- `driver_id`
- `purchase_date`
- `location_city`
- `location_state`
- `gallons`
- `price_per_gallon`
- `total_cost`
- `fuel_card_number`

**Tipos pandas:**

| Coluna | Tipo pandas |
| --- | --- |
| fuel_purchase_id | str |
| trip_id | str |
| truck_id | str |
| driver_id | str |
| purchase_date | str |
| location_city | str |
| location_state | str |
| gallons | float64 |
| price_per_gallon | float64 |
| total_cost | float64 |
| fuel_card_number | str |

**Valores nulos por coluna:**

| Coluna | Valores nulos | Percentual de nulos |
| --- | --- | --- |
| fuel_purchase_id | 0 | 0.00% |
| trip_id | 0 | 0.00% |
| truck_id | 3880 | 1.98% |
| driver_id | 3988 | 2.03% |
| purchase_date | 0 | 0.00% |
| location_city | 0 | 0.00% |
| location_state | 0 | 0.00% |
| gallons | 0 | 0.00% |
| price_per_gallon | 0 | 0.00% |
| total_cost | 0 | 0.00% |
| fuel_card_number | 0 | 0.00% |

**Quantidade de linhas duplicadas:** 0

**Possíveis IDs:** fuel_purchase_id, trip_id, truck_id, driver_id

**Possíveis datas:** purchase_date

**Possíveis campos numéricos:** gallons, price_per_gallon, total_cost

**Possíveis campos categóricos:** location_city, location_state

**Possíveis booleanos:** nenhum identificado automaticamente

**Possíveis financeiros:** price_per_gallon, total_cost

**Possíveis percentuais ou taxas:** nenhum identificado automaticamente

**Possíveis métricas de tempo/duração:** nenhuma identificada automaticamente

**Amostra controlada de até 3 linhas:**

| fuel_purchase_id | trip_id | truck_id | driver_id | purchase_date | location_city | location_state | gallons | price_per_gallon | total_cost | fuel_card_number |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FUEL00000001 | TRIP00051284 | TRK00045 | DRV00102 | 2023-10-22 05:00:00 | Columbus | MN | 131.6 | 3.399 | 447.31 | FC567161 |
| FUEL00000002 | TRIP00073723 | TRK00013 |  | 2024-08-04 08:00:00 | New York | AZ | 139.9 | 3.18 | 444.88 | FC717910 |
| FUEL00000003 | TRIP00018286 | TRK00024 | DRV00142 | 2022-08-23 13:00:00 | Seattle | NE | 189.3 | 3.804 | 720.1 | FC912816 |

### Arquivo: `loads.csv`

**Quantidade de linhas:** 85410

**Quantidade de colunas:** 12

**Lista de colunas:**

- `load_id`
- `customer_id`
- `route_id`
- `load_date`
- `load_type`
- `weight_lbs`
- `pieces`
- `revenue`
- `fuel_surcharge`
- `accessorial_charges`
- `load_status`
- `booking_type`

**Tipos pandas:**

| Coluna | Tipo pandas |
| --- | --- |
| load_id | str |
| customer_id | str |
| route_id | str |
| load_date | str |
| load_type | str |
| weight_lbs | int64 |
| pieces | int64 |
| revenue | float64 |
| fuel_surcharge | float64 |
| accessorial_charges | int64 |
| load_status | str |
| booking_type | str |

**Valores nulos por coluna:**

| Coluna | Valores nulos | Percentual de nulos |
| --- | --- | --- |
| load_id | 0 | 0.00% |
| customer_id | 0 | 0.00% |
| route_id | 0 | 0.00% |
| load_date | 0 | 0.00% |
| load_type | 0 | 0.00% |
| weight_lbs | 0 | 0.00% |
| pieces | 0 | 0.00% |
| revenue | 0 | 0.00% |
| fuel_surcharge | 0 | 0.00% |
| accessorial_charges | 0 | 0.00% |
| load_status | 0 | 0.00% |
| booking_type | 0 | 0.00% |

**Quantidade de linhas duplicadas:** 0

**Possíveis IDs:** load_id, customer_id, route_id

**Possíveis datas:** load_date

**Possíveis campos numéricos:** weight_lbs, pieces, revenue, fuel_surcharge, accessorial_charges

**Possíveis campos categóricos:** load_date, load_type, load_status, booking_type

**Possíveis booleanos:** nenhum identificado automaticamente

**Possíveis financeiros:** revenue, fuel_surcharge, accessorial_charges

**Possíveis percentuais ou taxas:** nenhum identificado automaticamente

**Possíveis métricas de tempo/duração:** nenhuma identificada automaticamente

**Amostra controlada de até 3 linhas:**

| load_id | customer_id | route_id | load_date | load_type | weight_lbs | pieces | revenue | fuel_surcharge | accessorial_charges | load_status | booking_type |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LOAD00000001 | CUST00183 | RTE00019 | 2022-01-01 | Dry Van | 19178 | 13 | 3045.23 | 406.72 | 100 | Completed | Spot |
| LOAD00000002 | CUST00076 | RTE00058 | 2022-01-01 | Dry Van | 27761 | 22 | 1224.48 | 98.61 | 0 | Completed | Dedicated |
| LOAD00000003 | CUST00027 | RTE00048 | 2022-01-01 | Refrigerated | 35594 | 16 | 7171.12 | 792.88 | 0 | Completed | Spot |

### Arquivo: `maintenance_records.csv`

**Quantidade de linhas:** 2920

**Quantidade de colunas:** 12

**Lista de colunas:**

- `maintenance_id`
- `truck_id`
- `maintenance_date`
- `maintenance_type`
- `odometer_reading`
- `labor_hours`
- `labor_cost`
- `parts_cost`
- `total_cost`
- `facility_location`
- `downtime_hours`
- `service_description`

**Tipos pandas:**

| Coluna | Tipo pandas |
| --- | --- |
| maintenance_id | str |
| truck_id | str |
| maintenance_date | str |
| maintenance_type | str |
| odometer_reading | int64 |
| labor_hours | float64 |
| labor_cost | float64 |
| parts_cost | float64 |
| total_cost | float64 |
| facility_location | str |
| downtime_hours | float64 |
| service_description | str |

**Valores nulos por coluna:**

| Coluna | Valores nulos | Percentual de nulos |
| --- | --- | --- |
| maintenance_id | 0 | 0.00% |
| truck_id | 0 | 0.00% |
| maintenance_date | 0 | 0.00% |
| maintenance_type | 0 | 0.00% |
| odometer_reading | 0 | 0.00% |
| labor_hours | 0 | 0.00% |
| labor_cost | 0 | 0.00% |
| parts_cost | 0 | 0.00% |
| total_cost | 0 | 0.00% |
| facility_location | 0 | 0.00% |
| downtime_hours | 0 | 0.00% |
| service_description | 0 | 0.00% |

**Quantidade de linhas duplicadas:** 0

**Possíveis IDs:** maintenance_id, truck_id

**Possíveis datas:** maintenance_date

**Possíveis campos numéricos:** odometer_reading, labor_hours, labor_cost, parts_cost, total_cost, downtime_hours

**Possíveis campos categóricos:** maintenance_type, facility_location

**Possíveis booleanos:** nenhum identificado automaticamente

**Possíveis financeiros:** labor_cost, parts_cost, total_cost

**Possíveis percentuais ou taxas:** nenhum identificado automaticamente

**Possíveis métricas de tempo/duração:** labor_hours, downtime_hours

**Amostra controlada de até 3 linhas:**

| maintenance_id | truck_id | maintenance_date | maintenance_type | odometer_reading | labor_hours | labor_cost | parts_cost | total_cost | facility_location | downtime_hours | service_description |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MAINT00000001 | TRK00085 | 2022-01-01 | Inspection | 400255 | 7.8 | 781.42 | 10.41 | 791.83 | Kansas City | 22.2 | Emergency Inspection |
| MAINT00000002 | TRK00041 | 2022-01-01 | Tire | 268041 | 0.9 | 80.91 | 3207.16 | 3288.07 | Seattle | 8.0 | Scheduled Tire |
| MAINT00000003 | TRK00090 | 2022-01-01 | Preventive | 698915 | 7.2 | 733.18 | 1570.57 | 2303.75 | Miami | 16.5 | Routine Preventive |

### Arquivo: `routes.csv`

**Quantidade de linhas:** 58

**Quantidade de colunas:** 9

**Lista de colunas:**

- `route_id`
- `origin_city`
- `origin_state`
- `destination_city`
- `destination_state`
- `typical_distance_miles`
- `base_rate_per_mile`
- `fuel_surcharge_rate`
- `typical_transit_days`

**Tipos pandas:**

| Coluna | Tipo pandas |
| --- | --- |
| route_id | str |
| origin_city | str |
| origin_state | str |
| destination_city | str |
| destination_state | str |
| typical_distance_miles | int64 |
| base_rate_per_mile | float64 |
| fuel_surcharge_rate | float64 |
| typical_transit_days | int64 |

**Valores nulos por coluna:**

| Coluna | Valores nulos | Percentual de nulos |
| --- | --- | --- |
| route_id | 0 | 0.00% |
| origin_city | 0 | 0.00% |
| origin_state | 0 | 0.00% |
| destination_city | 0 | 0.00% |
| destination_state | 0 | 0.00% |
| typical_distance_miles | 0 | 0.00% |
| base_rate_per_mile | 0 | 0.00% |
| fuel_surcharge_rate | 0 | 0.00% |
| typical_transit_days | 0 | 0.00% |

**Quantidade de linhas duplicadas:** 0

**Possíveis IDs:** route_id

**Possíveis datas:** nenhuma identificada automaticamente

**Possíveis campos numéricos:** typical_distance_miles, base_rate_per_mile, fuel_surcharge_rate, typical_transit_days

**Possíveis campos categóricos:** origin_city, origin_state, destination_city, destination_state

**Possíveis booleanos:** nenhum identificado automaticamente

**Possíveis financeiros:** base_rate_per_mile, fuel_surcharge_rate

**Possíveis percentuais ou taxas:** base_rate_per_mile, fuel_surcharge_rate

**Possíveis métricas de tempo/duração:** typical_transit_days

**Amostra controlada de até 3 linhas:**

| route_id | origin_city | origin_state | destination_city | destination_state | typical_distance_miles | base_rate_per_mile | fuel_surcharge_rate | typical_transit_days |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RTE00001 | Atlanta | GA | Chicago | IL | 677 | 1.7 | 0.19 | 1 |
| RTE00002 | Atlanta | GA | Miami | FL | 697 | 2.08 | 0.22 | 1 |
| RTE00003 | Chicago | IL | Los Angeles | CA | 2003 | 2.55 | 0.29 | 3 |

### Arquivo: `safety_incidents.csv`

**Quantidade de linhas:** 170

**Quantidade de colunas:** 15

**Lista de colunas:**

- `incident_id`
- `trip_id`
- `truck_id`
- `driver_id`
- `incident_date`
- `incident_type`
- `location_city`
- `location_state`
- `at_fault_flag`
- `injury_flag`
- `vehicle_damage_cost`
- `cargo_damage_cost`
- `claim_amount`
- `preventable_flag`
- `description`

**Tipos pandas:**

| Coluna | Tipo pandas |
| --- | --- |
| incident_id | str |
| trip_id | str |
| truck_id | str |
| driver_id | str |
| incident_date | str |
| incident_type | str |
| location_city | str |
| location_state | str |
| at_fault_flag | bool |
| injury_flag | bool |
| vehicle_damage_cost | float64 |
| cargo_damage_cost | float64 |
| claim_amount | float64 |
| preventable_flag | bool |
| description | str |

**Valores nulos por coluna:**

| Coluna | Valores nulos | Percentual de nulos |
| --- | --- | --- |
| incident_id | 0 | 0.00% |
| trip_id | 0 | 0.00% |
| truck_id | 1 | 0.59% |
| driver_id | 1 | 0.59% |
| incident_date | 0 | 0.00% |
| incident_type | 0 | 0.00% |
| location_city | 0 | 0.00% |
| location_state | 0 | 0.00% |
| at_fault_flag | 0 | 0.00% |
| injury_flag | 0 | 0.00% |
| vehicle_damage_cost | 0 | 0.00% |
| cargo_damage_cost | 0 | 0.00% |
| claim_amount | 0 | 0.00% |
| preventable_flag | 0 | 0.00% |
| description | 0 | 0.00% |

**Quantidade de linhas duplicadas:** 0

**Possíveis IDs:** incident_id, trip_id, truck_id, driver_id

**Possíveis datas:** incident_date

**Possíveis campos numéricos:** vehicle_damage_cost, cargo_damage_cost, claim_amount

**Possíveis campos categóricos:** incident_type, location_city, location_state

**Possíveis booleanos:** at_fault_flag, injury_flag, preventable_flag

**Possíveis financeiros:** vehicle_damage_cost, cargo_damage_cost, claim_amount

**Possíveis percentuais ou taxas:** nenhum identificado automaticamente

**Possíveis métricas de tempo/duração:** nenhuma identificada automaticamente

**Amostra controlada de até 3 linhas:**

| incident_id | trip_id | truck_id | driver_id | incident_date | incident_type | location_city | location_state | at_fault_flag | injury_flag | vehicle_damage_cost | cargo_damage_cost | claim_amount | preventable_flag | description |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| INC00000001 | TRIP00036079 | TRK00006 | DRV00006 | 2023-04-09 14:00:00 | Moving Violation | Columbus | PA | True | False | 12629.26 | 0.0 | 12629.26 | True | Severe incident involving equipment |
| INC00000002 | TRIP00032462 | TRK00084 | DRV00006 | 2023-02-19 11:00:00 | Moving Violation | Columbus | NC | False | False | 2700.7 | 14284.24 | 16984.94 | False | Severe incident involving weather |
| INC00000003 | TRIP00067583 | TRK00106 | DRV00119 | 2024-05-20 01:00:00 | Customer Complaint | Seattle | OK | True | False | 24302.32 | 0.0 | 24302.32 | True | Minor incident involving traffic |

### Arquivo: `trailers.csv`

**Quantidade de linhas:** 180

**Quantidade de colunas:** 9

**Lista de colunas:**

- `trailer_id`
- `trailer_number`
- `trailer_type`
- `length_feet`
- `model_year`
- `vin`
- `acquisition_date`
- `status`
- `current_location`

**Tipos pandas:**

| Coluna | Tipo pandas |
| --- | --- |
| trailer_id | str |
| trailer_number | int64 |
| trailer_type | str |
| length_feet | int64 |
| model_year | int64 |
| vin | str |
| acquisition_date | str |
| status | str |
| current_location | str |

**Valores nulos por coluna:**

| Coluna | Valores nulos | Percentual de nulos |
| --- | --- | --- |
| trailer_id | 0 | 0.00% |
| trailer_number | 0 | 0.00% |
| trailer_type | 0 | 0.00% |
| length_feet | 0 | 0.00% |
| model_year | 0 | 0.00% |
| vin | 0 | 0.00% |
| acquisition_date | 0 | 0.00% |
| status | 0 | 0.00% |
| current_location | 0 | 0.00% |

**Quantidade de linhas duplicadas:** 0

**Possíveis IDs:** trailer_id

**Possíveis datas:** acquisition_date

**Possíveis campos numéricos:** length_feet

**Possíveis campos categóricos:** trailer_type, status, current_location

**Possíveis booleanos:** nenhum identificado automaticamente

**Possíveis financeiros:** nenhum identificado automaticamente

**Possíveis percentuais ou taxas:** nenhum identificado automaticamente

**Possíveis métricas de tempo/duração:** nenhuma identificada automaticamente

**Amostra controlada de até 3 linhas:**

| trailer_id | trailer_number | trailer_type | length_feet | model_year | vin | acquisition_date | status | current_location |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TRL00001 | 4290 | Refrigerated | 53 | 2016 | 1AV889081755621178 | 2018-05-11 | Active | Kansas City |
| TRL00002 | 8848 | Dry Van | 53 | 2018 | 1BU942062588832828 | 2018-11-24 | Active | Kansas City |
| TRL00003 | 6147 | Dry Van | 53 | 2022 | 1AV669057807416326 | 2019-01-28 | Active | Milwaukee |

### Arquivo: `trips.csv`

**Quantidade de linhas:** 85410

**Quantidade de colunas:** 12

**Lista de colunas:**

- `trip_id`
- `load_id`
- `driver_id`
- `truck_id`
- `trailer_id`
- `dispatch_date`
- `actual_distance_miles`
- `actual_duration_hours`
- `fuel_gallons_used`
- `average_mpg`
- `idle_time_hours`
- `trip_status`

**Tipos pandas:**

| Coluna | Tipo pandas |
| --- | --- |
| trip_id | str |
| load_id | str |
| driver_id | str |
| truck_id | str |
| trailer_id | str |
| dispatch_date | str |
| actual_distance_miles | int64 |
| actual_duration_hours | float64 |
| fuel_gallons_used | float64 |
| average_mpg | float64 |
| idle_time_hours | float64 |
| trip_status | str |

**Valores nulos por coluna:**

| Coluna | Valores nulos | Percentual de nulos |
| --- | --- | --- |
| trip_id | 0 | 0.00% |
| load_id | 0 | 0.00% |
| driver_id | 1714 | 2.01% |
| truck_id | 1672 | 1.96% |
| trailer_id | 1680 | 1.97% |
| dispatch_date | 0 | 0.00% |
| actual_distance_miles | 0 | 0.00% |
| actual_duration_hours | 0 | 0.00% |
| fuel_gallons_used | 0 | 0.00% |
| average_mpg | 0 | 0.00% |
| idle_time_hours | 0 | 0.00% |
| trip_status | 0 | 0.00% |

**Quantidade de linhas duplicadas:** 0

**Possíveis IDs:** trip_id, load_id, driver_id, truck_id, trailer_id

**Possíveis datas:** dispatch_date

**Possíveis campos numéricos:** actual_distance_miles, actual_duration_hours, fuel_gallons_used, average_mpg, idle_time_hours

**Possíveis campos categóricos:** dispatch_date, trip_status

**Possíveis booleanos:** nenhum identificado automaticamente

**Possíveis financeiros:** nenhum identificado automaticamente

**Possíveis percentuais ou taxas:** nenhum identificado automaticamente

**Possíveis métricas de tempo/duração:** actual_duration_hours, idle_time_hours

**Amostra controlada de até 3 linhas:**

| trip_id | load_id | driver_id | truck_id | trailer_id | dispatch_date | actual_distance_miles | actual_duration_hours | fuel_gallons_used | average_mpg | idle_time_hours | trip_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TRIP00000001 | LOAD00000001 | DRV00117 | TRK00035 | TRL00167 | 2022-01-01 | 1314 | 26.2 | 183.8 | 7.15 | 3.5 | Completed |
| TRIP00000002 | LOAD00000002 | DRV00141 | TRK00108 | TRL00082 | 2022-01-01 | 515 | 8.6 | 93.6 | 5.5 | 8.3 | Completed |
| TRIP00000003 | LOAD00000003 | DRV00032 | TRK00031 | TRL00138 | 2022-01-01 | 2509 | 45.0 | 339.1 | 7.4 | 12.0 | Completed |

### Arquivo: `truck_utilization_metrics.csv`

**Quantidade de linhas:** 3312

**Quantidade de colunas:** 10

**Lista de colunas:**

- `truck_id`
- `month`
- `trips_completed`
- `total_miles`
- `total_revenue`
- `average_mpg`
- `maintenance_events`
- `maintenance_cost`
- `downtime_hours`
- `utilization_rate`

**Tipos pandas:**

| Coluna | Tipo pandas |
| --- | --- |
| truck_id | str |
| month | str |
| trips_completed | int64 |
| total_miles | int64 |
| total_revenue | float64 |
| average_mpg | float64 |
| maintenance_events | int64 |
| maintenance_cost | float64 |
| downtime_hours | float64 |
| utilization_rate | float64 |

**Valores nulos por coluna:**

| Coluna | Valores nulos | Percentual de nulos |
| --- | --- | --- |
| truck_id | 0 | 0.00% |
| month | 0 | 0.00% |
| trips_completed | 0 | 0.00% |
| total_miles | 0 | 0.00% |
| total_revenue | 0 | 0.00% |
| average_mpg | 0 | 0.00% |
| maintenance_events | 0 | 0.00% |
| maintenance_cost | 0 | 0.00% |
| downtime_hours | 0 | 0.00% |
| utilization_rate | 0 | 0.00% |

**Quantidade de linhas duplicadas:** 0

**Possíveis IDs:** truck_id

**Possíveis datas:** nenhuma identificada automaticamente

**Possíveis campos numéricos:** trips_completed, total_miles, total_revenue, average_mpg, maintenance_events, maintenance_cost, downtime_hours, utilization_rate

**Possíveis campos categóricos:** month

**Possíveis booleanos:** nenhum identificado automaticamente

**Possíveis financeiros:** total_revenue, maintenance_cost

**Possíveis percentuais ou taxas:** utilization_rate

**Possíveis métricas de tempo/duração:** downtime_hours

**Amostra controlada de até 3 linhas:**

| truck_id | month | trips_completed | total_miles | total_revenue | average_mpg | maintenance_events | maintenance_cost | downtime_hours | utilization_rate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TRK00001 | 2022-01-01 | 22 | 39269 | 84792.02 | 6.78 | 2 | 4380.98 | 63.1 | 0.71 |
| TRK00001 | 2022-02-01 | 27 | 40787 | 88809.05 | 6.23 | 0 | 0.0 | 0.0 | 0.964 |
| TRK00001 | 2022-03-01 | 34 | 57422 | 120453.71 | 6.49 | 0 | 0.0 | 0.0 | 1.097 |

### Arquivo: `trucks.csv`

**Quantidade de linhas:** 120

**Quantidade de colunas:** 11

**Lista de colunas:**

- `truck_id`
- `unit_number`
- `make`
- `model_year`
- `vin`
- `acquisition_date`
- `acquisition_mileage`
- `fuel_type`
- `tank_capacity_gallons`
- `status`
- `home_terminal`

**Tipos pandas:**

| Coluna | Tipo pandas |
| --- | --- |
| truck_id | str |
| unit_number | int64 |
| make | str |
| model_year | int64 |
| vin | str |
| acquisition_date | str |
| acquisition_mileage | int64 |
| fuel_type | str |
| tank_capacity_gallons | int64 |
| status | str |
| home_terminal | str |

**Valores nulos por coluna:**

| Coluna | Valores nulos | Percentual de nulos |
| --- | --- | --- |
| truck_id | 0 | 0.00% |
| unit_number | 0 | 0.00% |
| make | 0 | 0.00% |
| model_year | 0 | 0.00% |
| vin | 0 | 0.00% |
| acquisition_date | 0 | 0.00% |
| acquisition_mileage | 0 | 0.00% |
| fuel_type | 0 | 0.00% |
| tank_capacity_gallons | 0 | 0.00% |
| status | 0 | 0.00% |
| home_terminal | 0 | 0.00% |

**Quantidade de linhas duplicadas:** 0

**Possíveis IDs:** truck_id

**Possíveis datas:** acquisition_date

**Possíveis campos numéricos:** acquisition_mileage, tank_capacity_gallons

**Possíveis campos categóricos:** make, fuel_type, status, home_terminal

**Possíveis booleanos:** nenhum identificado automaticamente

**Possíveis financeiros:** nenhum identificado automaticamente

**Possíveis percentuais ou taxas:** nenhum identificado automaticamente

**Possíveis métricas de tempo/duração:** nenhuma identificada automaticamente

**Amostra controlada de até 3 linhas:**

| truck_id | unit_number | make | model_year | vin | acquisition_date | acquisition_mileage | fuel_type | tank_capacity_gallons | status | home_terminal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TRK00001 | 3463 | Peterbilt | 2016 | 1VV205190335317039 | 2017-04-27 | 18814 | Diesel | 200 | Active | Omaha |
| TRK00002 | 6461 | Kenworth | 2015 | 1NV753749606229960 | 2018-10-04 | 26795 | Diesel | 150 | Active | Seattle |
| TRK00003 | 2335 | Peterbilt | 2018 | 1NT803101860493229 | 2020-09-17 | 11795 | Diesel | 150 | Maintenance | Atlanta |

## Erros de leitura

Nenhum erro de leitura foi registrado.

## 6. Perfil técnico das colunas

### `customers.csv`

| coluna | tipo_pandas | nulos | percentual_nulos | unicos | percentual_unicos | exemplos | minimo | maximo | media | mediana | zeros | percentual_zeros | padrao | hipotese | confianca | validacao |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| customer_id | str | 0 | 0.00% | 200 | 100.00% | CUST00001, CUST00002, CUST00003 |  |  |  |  |  |  | Texto curto ou código descritivo. | possível identificador | alto | Validar se é chave primária |
| customer_name | str | 0 | 0.00% | 107 | 53.50% | Metro Wholesale, National Retail, XYZ Industries |  |  |  |  |  |  | Texto curto ou código descritivo. | possível dado comercial confidencial | médio | Sim |
| customer_type | str | 0 | 0.00% | 3 | 1.50% | Dedicated, Contract, Spot |  |  |  |  |  |  | Texto curto ou código descritivo. | possível categoria/status/código | médio | Validar domínio de valores |
| credit_terms_days | int64 | 0 | 0.00% | 4 | 2.00% | 60, 30, 15 | 15.0 | 60.0 | 37.65 | 30.0 | 0 | 0.00% | Numérico | possível métrica de duração | alto | Validar unidade |
| primary_freight_type | str | 0 | 0.00% | 6 | 3.00% | General, Retail, Consumer Goods |  |  |  |  |  |  | Texto curto ou código descritivo. | possível categoria/status/código | médio | Validar domínio de valores |
| account_status | str | 0 | 0.00% | 2 | 1.00% | Inactive, Active |  |  |  |  |  |  | Texto curto ou código descritivo. | possível categoria/status/código | médio | Validar domínio de valores |
| contract_start_date | str | 0 | 0.00% | 173 | 86.50% | 2020-02-20, 2021-06-02, 2020-09-04 |  |  |  |  |  |  | Texto com padrão provável de data. | possível data | médio | Validar formato antes de converter |
| annual_revenue_potential | int64 | 0 | 0.00% | 200 | 100.00% | 985117, 4936566, 3102814 | 101641.0 | 4990599.0 | 2688236.745 | 2784584.5 | 0 | 0.00% | Numérico | possível valor financeiro | alto | Validar moeda e regra |

### `delivery_events.csv`

| coluna | tipo_pandas | nulos | percentual_nulos | unicos | percentual_unicos | exemplos | minimo | maximo | media | mediana | zeros | percentual_zeros | padrao | hipotese | confianca | validacao |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| event_id | str | 0 | 0.00% | 170820 | 100.00% | EVT00000001, EVT00000002, EVT00000003 |  |  |  |  |  |  | Texto curto ou código descritivo. | possível identificador | alto | Validar se é chave primária |
| load_id | str | 0 | 0.00% | 85410 | 50.00% | LOAD00000001, LOAD00000002, LOAD00000003 |  |  |  |  |  |  | Texto curto ou código descritivo. | possível chave estrangeira | médio | Validar relacionamento |
| trip_id | str | 0 | 0.00% | 85410 | 50.00% | TRIP00000001, TRIP00000002, TRIP00000003 |  |  |  |  |  |  | Texto curto ou código descritivo. | possível chave estrangeira | médio | Validar relacionamento |
| event_type | str | 0 | 0.00% | 2 | 0.00% | Pickup, Delivery |  |  |  |  |  |  | Texto curto ou código descritivo. | possível categoria/status/código | médio | Validar domínio de valores |
| facility_id | str | 0 | 0.00% | 50 | 0.03% | FAC00034, FAC00046, FAC00015 |  |  |  |  |  |  | Texto curto ou código descritivo. | possível chave estrangeira | médio | Validar relacionamento |
| scheduled_datetime | str | 0 | 0.00% | 99624 | 58.32% | 2022-01-01 18:00:00.000000, 2022-01-02 23:10:55.918185, 2022-01-02 02:13:26.608430 |  |  |  |  |  |  | Texto com padrão provável de data. | possível data/hora | alto | Validar formato e fuso |
| actual_datetime | str | 0 | 0.00% | 170820 | 100.00% | 2022-01-01 20:58:55.918185, 2022-01-02 21:30:22.142060, 2022-01-01 17:37:26.608430 |  |  |  |  |  |  | Texto com padrão provável de data. | possível data/hora | alto | Validar formato e fuso |
| detention_minutes | int64 | 0 | 0.00% | 240 | 0.14% | 0, 230, 62 | 0.0 | 239.0 | 91.5375 | 88.0 | 22472 | 13.16% | Numérico | possível métrica de duração | alto | Validar unidade |
| on_time_flag | bool | 0 | 0.00% | 2 | 0.00% | False, True | 0.0 | 1.0 | 0.5567 | 1.0 | 75725 | 44.33% | Numérico | possível booleano | alto | Validar regra de negócio |
| location_city | str | 0 | 0.00% | 20 | 0.01% | Houston, Detroit, Kansas City |  |  |  |  |  |  | Texto curto ou código descritivo. | possível categoria/status/código | médio | Validar domínio de valores |
| location_state | str | 0 | 0.00% | 19 | 0.01% | TX, MI, MO |  |  |  |  |  |  | Texto curto ou código descritivo. | possível categoria/status/código | médio | Validar domínio de valores |

### `driver_monthly_metrics.csv`

| coluna | tipo_pandas | nulos | percentual_nulos | unicos | percentual_unicos | exemplos | minimo | maximo | media | mediana | zeros | percentual_zeros | padrao | hipotese | confianca | validacao |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| driver_id | str | 0 | 0.00% | 124 | 2.78% | DRV00001, DRV00002, DRV00003 |  |  |  |  |  |  | Texto curto ou código descritivo. | possível chave estrangeira | médio | Validar relacionamento |
| month | str | 0 | 0.00% | 36 | 0.81% | 2022-01-01, 2022-02-01, 2022-03-01 |  |  |  |  |  |  | Texto com padrão provável de data. | possível data | médio | Validar formato antes de converter |
| trips_completed | int64 | 0 | 0.00% | 32 | 0.72% | 26, 9, 20 | 5.0 | 37.0 | 18.7491 | 19.0 | 0 | 0.00% | Numérico | possível contagem | alto | Validar unidade |
| total_miles | int64 | 0 | 0.00% | 4100 | 91.85% | 36620, 13515, 30361 | 3310.0 | 57954.0 | 26812.7923 | 26409.5 | 0 | 0.00% | Numérico | possível quantidade ou métrica contínua | médio | Validar unidade e agregação |
| total_revenue | float64 | 0 | 0.00% | 4463 | 99.98% | 79141.59, 27133.87, 62399.62 | 7096.56 | 124579.53 | 57630.9477 | 56652.715 | 0 | 0.00% | Numérico | possível valor financeiro | alto | Validar moeda e regra |
| average_mpg | float64 | 0 | 0.00% | 97 | 2.17% | 6.61, 6.69, 6.36 | 6.01 | 7.07 | 6.5019 | 6.5 | 0 | 0.00% | Numérico | possível média | alto | Não somar diretamente |
| total_fuel_gallons | float64 | 0 | 0.00% | 4201 | 94.11% | 5574.7, 2095.1, 4792.2 | 521.9 | 9007.5 | 4158.6317 | 4083.95 | 0 | 0.00% | Numérico | possível quantidade ou métrica contínua | médio | Validar unidade e agregação |
| on_time_delivery_rate | float64 | 0 | 0.00% | 187 | 4.19% | 0.385, 0.333, 0.55 | 0.0 | 0.833 | 0.446 | 0.444 | 1 | 0.02% | Numérico | possível percentual em escala decimal | médio | Validar escala |
| average_idle_hours | float64 | 0 | 0.00% | 51 | 1.14% | 8.2, 6.8, 7.5 | 4.4 | 9.7 | 7.0117 | 7.0 | 0 | 0.00% | Numérico | possível média | alto | Não somar diretamente |

### `drivers.csv`

| coluna | tipo_pandas | nulos | percentual_nulos | unicos | percentual_unicos | exemplos | minimo | maximo | media | mediana | zeros | percentual_zeros | padrao | hipotese | confianca | validacao |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| driver_id | str | 0 | 0.00% | 150 | 100.00% | DRV00001, DRV00002, DRV00003 |  |  |  |  |  |  | Texto curto ou código descritivo. | possível identificador | alto | Validar se é chave primária |
| first_name | str | 0 | 0.00% | 20 | 13.33% | Jennifer, William, Charles |  |  |  |  |  |  | Texto curto ou código descritivo. | possível dado pessoal | alto | Sim |
| last_name | str | 0 | 0.00% | 20 | 13.33% | Hernandez, Martin, Brown |  |  |  |  |  |  | Texto curto ou código descritivo. | possível dado pessoal | alto | Sim |
| hire_date | str | 0 | 0.00% | 147 | 98.00% | 2014-10-31, 2020-10-02, 2021-09-21 |  |  |  |  |  |  | Texto com padrão provável de data. | possível data | médio | Validar formato antes de converter |
| termination_date | str | 124 | 82.67% | 26 | 17.33% | 2021-05-17, 2021-01-23, 2021-05-23 |  |  |  |  |  |  | Texto com padrão provável de data. | possível data | médio | Validar formato antes de converter |
| license_number | str | 0 | 0.00% | 150 | 100.00% | DL673510887, DL128955006, DL523076025 |  |  |  |  |  |  | Texto curto ou código descritivo. | possível dado pessoal/identificável | alto | Sim |
| license_state | str | 0 | 0.00% | 23 | 15.33% | WA, GA, NC |  |  |  |  |  |  | Texto curto ou código descritivo. | possível categoria/status/código | médio | Validar domínio de valores |
| date_of_birth | str | 0 | 0.00% | 148 | 98.67% | 1973-11-07, 1976-11-03, 1970-04-06 |  |  |  |  |  |  | Texto com padrão provável de data. | possível dado pessoal | alto | Sim |
| home_terminal | str | 0 | 0.00% | 25 | 16.67% | Denver, Columbus, Salt Lake City |  |  |  |  |  |  | Texto curto ou código descritivo. | possível categoria/status/código | médio | Validar domínio de valores |
| employment_status | str | 0 | 0.00% | 2 | 1.33% | Active, Terminated |  |  |  |  |  |  | Texto curto ou código descritivo. | possível categoria/status/código | médio | Validar domínio de valores |
| cdl_class | str | 0 | 0.00% | 1 | 0.67% | A |  |  |  |  |  |  | Texto curto ou código descritivo. | possível categoria/status/código | médio | Validar domínio de valores |
| years_experience | int64 | 0 | 0.00% | 24 | 16.00% | 3, 20, 19 | 2.0 | 25.0 | 13.4933 | 13.5 | 0 | 0.00% | Numérico | possível métrica de duração/experiência em anos | alto | Validar unidade |

### `facilities.csv`

| coluna | tipo_pandas | nulos | percentual_nulos | unicos | percentual_unicos | exemplos | minimo | maximo | media | mediana | zeros | percentual_zeros | padrao | hipotese | confianca | validacao |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| facility_id | str | 0 | 0.00% | 50 | 100.00% | FAC00001, FAC00002, FAC00003 |  |  |  |  |  |  | Texto curto ou código descritivo. | possível identificador | alto | Validar se é chave primária |
| facility_name | str | 0 | 0.00% | 35 | 70.00% | Houston Distribution Center, Kansas City Hub, Charlotte Distribution Center |  |  |  |  |  |  | Texto curto ou código descritivo. | ambíguo / exige validação | baixo | Validação humana necessária |
| facility_type | str | 0 | 0.00% | 4 | 8.00% | Cross-Dock, Distribution Center, Terminal |  |  |  |  |  |  | Texto curto ou código descritivo. | possível categoria/status/código | médio | Validar domínio de valores |
| city | str | 0 | 0.00% | 21 | 42.00% | Houston, Kansas City, Charlotte |  |  |  |  |  |  | Texto curto ou código descritivo. | possível categoria/status/código | médio | Validar domínio de valores |
| state | str | 0 | 0.00% | 20 | 40.00% | TX, MO, NC |  |  |  |  |  |  | Texto curto ou código descritivo. | possível categoria/status/código | médio | Validar domínio de valores |
| latitude | float64 | 0 | 0.00% | 21 | 42.00% | 29.7604, 39.0997, 35.2271 | 25.7617 | 45.5152 | 36.8693 | 36.1663 | 0 | 0.00% | Numérico | possível coordenada geográfica | alto | Validar uso geográfico |
| longitude | float64 | 0 | 0.00% | 21 | 42.00% | -95.3698, -94.5786, -80.8431 | -122.6784 | -74.006 | -93.2602 | -86.7816 | 0 | 0.00% | Numérico | possível coordenada geográfica | alto | Validar uso geográfico |
| dock_doors | int64 | 0 | 0.00% | 40 | 80.00% | 125, 33, 138 | 16.0 | 150.0 | 78.58 | 67.5 | 0 | 0.00% | Numérico | possível quantidade ou métrica contínua | médio | Validar unidade e agregação |
| operating_hours | str | 0 | 0.00% | 4 | 8.00% | 24/7, 7AM-7PM, 8AM-5PM |  |  |  |  |  |  | Texto curto ou código descritivo. | possível categoria/status/código | médio | Validar domínio de valores |

### `fuel_purchases.csv`

| coluna | tipo_pandas | nulos | percentual_nulos | unicos | percentual_unicos | exemplos | minimo | maximo | media | mediana | zeros | percentual_zeros | padrao | hipotese | confianca | validacao |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| fuel_purchase_id | str | 0 | 0.00% | 196442 | 100.00% | FUEL00000001, FUEL00000002, FUEL00000003 |  |  |  |  |  |  | Texto curto ou código descritivo. | possível identificador | alto | Validar se é chave primária |
| trip_id | str | 0 | 0.00% | 76939 | 39.17% | TRIP00051284, TRIP00073723, TRIP00018286 |  |  |  |  |  |  | Texto curto ou código descritivo. | possível chave estrangeira | médio | Validar relacionamento |
| truck_id | str | 3880 | 1.98% | 92 | 0.05% | TRK00045, TRK00013, TRK00024 |  |  |  |  |  |  | Texto curto ou código descritivo. | possível chave estrangeira | médio | Validar relacionamento |
| driver_id | str | 3988 | 2.03% | 124 | 0.06% | DRV00102, DRV00142, DRV00047 |  |  |  |  |  |  | Texto curto ou código descritivo. | possível chave estrangeira | médio | Validar relacionamento |
| purchase_date | str | 0 | 0.00% | 26331 | 13.40% | 2023-10-22 05:00:00, 2024-08-04 08:00:00, 2022-08-23 13:00:00 |  |  |  |  |  |  | Texto com padrão provável de data. | possível data | médio | Validar formato antes de converter |
| location_city | str | 0 | 0.00% | 25 | 0.01% | Columbus, New York, Seattle |  |  |  |  |  |  | Texto curto ou código descritivo. | possível categoria/status/código | médio | Validar domínio de valores |
| location_state | str | 0 | 0.00% | 23 | 0.01% | MN, AZ, NE |  |  |  |  |  |  | Texto curto ou código descritivo. | possível categoria/status/código | médio | Validar domínio de valores |
| gallons | float64 | 0 | 0.00% | 1501 | 0.76% | 131.6, 139.9, 189.3 | 50.0 | 200.0 | 124.8157 | 124.7 | 0 | 0.00% | Numérico | possível quantidade ou métrica contínua | médio | Validar unidade e agregação |
| price_per_gallon | float64 | 0 | 0.00% | 1851 | 0.94% | 3.399, 3.18, 3.804 | 3.15 | 5.0 | 3.8984 | 3.856 | 0 | 0.00% | Numérico | possível taxa monetária por unidade | alto | Não somar diretamente |
| total_cost | float64 | 0 | 0.00% | 64113 | 32.64% | 447.31, 444.88, 720.1 | 158.5 | 997.9 | 486.622 | 480.66 | 0 | 0.00% | Numérico | possível valor financeiro | alto | Validar moeda e regra |
| fuel_card_number | str | 0 | 0.00% | 176645 | 89.92% | FC567161, FC717910, FC912816 |  |  |  |  |  |  | Texto curto ou código descritivo. | possível identificador operacional confidencial | alto | Sim |

### `loads.csv`

| coluna | tipo_pandas | nulos | percentual_nulos | unicos | percentual_unicos | exemplos | minimo | maximo | media | mediana | zeros | percentual_zeros | padrao | hipotese | confianca | validacao |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| load_id | str | 0 | 0.00% | 85410 | 100.00% | LOAD00000001, LOAD00000002, LOAD00000003 |  |  |  |  |  |  | Texto curto ou código descritivo. | possível identificador | alto | Validar se é chave primária |
| customer_id | str | 0 | 0.00% | 200 | 0.23% | CUST00183, CUST00076, CUST00027 |  |  |  |  |  |  | Texto curto ou código descritivo. | possível chave estrangeira | médio | Validar relacionamento |
| route_id | str | 0 | 0.00% | 58 | 0.07% | RTE00019, RTE00058, RTE00048 |  |  |  |  |  |  | Texto curto ou código descritivo. | possível chave estrangeira | médio | Validar relacionamento |
| load_date | str | 0 | 0.00% | 1096 | 1.28% | 2022-01-01, 2022-01-02, 2022-01-03 |  |  |  |  |  |  | Texto com padrão provável de data. | possível data | médio | Validar formato antes de converter |
| load_type | str | 0 | 0.00% | 2 | 0.00% | Dry Van, Refrigerated |  |  |  |  |  |  | Texto curto ou código descritivo. | possível categoria/status/código | médio | Validar domínio de valores |
| weight_lbs | int64 | 0 | 0.00% | 31927 | 37.38% | 19178, 27761, 35594 | 10000.0 | 45000.0 | 27477.4953 | 27482.0 | 0 | 0.00% | Numérico | possível quantidade ou métrica contínua | médio | Validar unidade e agregação |
| pieces | int64 | 0 | 0.00% | 28 | 0.03% | 13, 22, 16 | 1.0 | 28.0 | 14.4705 | 14.0 | 0 | 0.00% | Numérico | ambíguo / exige validação humana | baixo | Validação humana obrigatória |
| revenue | float64 | 0 | 0.00% | 79130 | 92.65% | 3045.23, 1224.48, 7171.12 | 125.93 | 8125.22 | 3073.7127 | 2827.985 | 0 | 0.00% | Numérico | possível valor financeiro | alto | Validar moeda e regra |
| fuel_surcharge | float64 | 0 | 0.00% | 57 | 0.07% | 406.72, 98.61, 792.88 | 13.8 | 891.82 | 350.9721 | 314.64 | 0 | 0.00% | Numérico | possível valor financeiro | alto | Validar moeda e regra |
| accessorial_charges | int64 | 0 | 0.00% | 6 | 0.01% | 100, 0, 50 | 0.0 | 200.0 | 71.6438 | 50.0 | 32186 | 37.68% | Numérico | possível valor financeiro | alto | Validar moeda e regra |
| load_status | str | 0 | 0.00% | 1 | 0.00% | Completed |  |  |  |  |  |  | Texto curto ou código descritivo. | possível categoria/status/código | médio | Validar domínio de valores |
| booking_type | str | 0 | 0.00% | 3 | 0.00% | Spot, Dedicated, Contract |  |  |  |  |  |  | Texto curto ou código descritivo. | possível categoria/status/código | médio | Validar domínio de valores |

### `maintenance_records.csv`

| coluna | tipo_pandas | nulos | percentual_nulos | unicos | percentual_unicos | exemplos | minimo | maximo | media | mediana | zeros | percentual_zeros | padrao | hipotese | confianca | validacao |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| maintenance_id | str | 0 | 0.00% | 2920 | 100.00% | MAINT00000001, MAINT00000002, MAINT00000003 |  |  |  |  |  |  | Texto curto ou código descritivo. | possível identificador | alto | Validar se é chave primária |
| truck_id | str | 0 | 0.00% | 120 | 4.11% | TRK00085, TRK00041, TRK00090 |  |  |  |  |  |  | Texto curto ou código descritivo. | possível chave estrangeira | médio | Validar relacionamento |
| maintenance_date | str | 0 | 0.00% | 1020 | 34.93% | 2022-01-01, 2022-01-02, 2022-01-03 |  |  |  |  |  |  | Texto com padrão provável de data. | possível data | médio | Validar formato antes de converter |
| maintenance_type | str | 0 | 0.00% | 7 | 0.24% | Inspection, Tire, Preventive |  |  |  |  |  |  | Texto curto ou código descritivo. | possível categoria/status/código | médio | Validar domínio de valores |
| odometer_reading | int64 | 0 | 0.00% | 2912 | 99.73% | 400255, 268041, 698915 | 50156.0 | 749875.0 | 401534.7877 | 407955.0 | 0 | 0.00% | Numérico | possível identificador operacional confidencial | baixo | Validar significado |
| labor_hours | float64 | 0 | 0.00% | 76 | 2.60% | 7.8, 0.9, 7.2 | 0.5 | 8.0 | 4.1785 | 4.2 | 0 | 0.00% | Numérico | possível métrica de duração | alto | Validar unidade |
| labor_cost | float64 | 0 | 0.00% | 2851 | 97.64% | 781.42, 80.91, 733.18 | 43.28 | 976.87 | 438.5298 | 435.2 | 0 | 0.00% | Numérico | possível valor financeiro | alto | Validar moeda e regra |
| parts_cost | float64 | 0 | 0.00% | 2903 | 99.42% | 10.41, 3207.16, 1570.57 | 0.14 | 3498.61 | 1523.9953 | 1465.415 | 0 | 0.00% | Numérico | possível valor financeiro | alto | Validar moeda e regra |
| total_cost | float64 | 0 | 0.00% | 2914 | 99.79% | 791.83, 3288.07, 2303.75 | 60.82 | 4426.57 | 1962.5251 | 1896.045 | 0 | 0.00% | Numérico | possível valor financeiro | alto | Validar moeda e regra |
| facility_location | str | 0 | 0.00% | 25 | 0.86% | Kansas City, Seattle, Miami |  |  |  |  |  |  | Texto curto ou código descritivo. | possível categoria/status/código | médio | Validar domínio de valores |
| downtime_hours | float64 | 0 | 0.00% | 460 | 15.75% | 22.2, 8.0, 16.5 | 2.0 | 48.0 | 24.7365 | 24.75 | 0 | 0.00% | Numérico | possível métrica de duração | alto | Validar unidade |
| service_description | str | 0 | 0.00% | 21 | 0.72% | Emergency Inspection, Scheduled Tire, Routine Preventive |  |  |  |  |  |  | Texto curto ou código descritivo. | possível texto livre com possível risco | médio | Sim |

### `routes.csv`

| coluna | tipo_pandas | nulos | percentual_nulos | unicos | percentual_unicos | exemplos | minimo | maximo | media | mediana | zeros | percentual_zeros | padrao | hipotese | confianca | validacao |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| route_id | str | 0 | 0.00% | 58 | 100.00% | RTE00001, RTE00002, RTE00003 |  |  |  |  |  |  | Texto curto ou código descritivo. | possível identificador | alto | Validar se é chave primária |
| origin_city | str | 0 | 0.00% | 18 | 31.03% | Atlanta, Chicago, Dallas |  |  |  |  |  |  | Texto curto ou código descritivo. | possível categoria/status/código | médio | Validar domínio de valores |
| origin_state | str | 0 | 0.00% | 17 | 29.31% | GA, IL, TX |  |  |  |  |  |  | Texto curto ou código descritivo. | possível categoria/status/código | médio | Validar domínio de valores |
| destination_city | str | 0 | 0.00% | 19 | 32.76% | Chicago, Miami, Los Angeles |  |  |  |  |  |  | Texto curto ou código descritivo. | possível categoria/status/código | médio | Validar domínio de valores |
| destination_state | str | 0 | 0.00% | 18 | 31.03% | IL, FL, CA |  |  |  |  |  |  | Texto curto ou código descritivo. | possível categoria/status/código | médio | Validar domínio de valores |
| typical_distance_miles | int64 | 0 | 0.00% | 52 | 89.66% | 677, 697, 2003 | 92.0 | 3141.0 | 1391.5 | 1271.0 | 0 | 0.00% | Numérico | possível quantidade ou métrica contínua | médio | Validar unidade e agregação |
| base_rate_per_mile | float64 | 0 | 0.00% | 46 | 79.31% | 1.7, 2.08, 2.55 | 1.52 | 2.79 | 2.1967 | 2.23 | 0 | 0.00% | Numérico | possível taxa monetária por unidade | alto | Não somar diretamente |
| fuel_surcharge_rate | float64 | 0 | 0.00% | 20 | 34.48% | 0.19, 0.22, 0.29 | 0.15 | 0.34 | 0.2488 | 0.245 | 0 | 0.00% | Numérico | possível percentual em escala decimal | médio | Validar escala |
| typical_transit_days | int64 | 0 | 0.00% | 5 | 8.62% | 1, 3, 2 | 1.0 | 5.0 | 2.1207 | 2.0 | 0 | 0.00% | Numérico | possível métrica de duração | alto | Validar unidade |

### `safety_incidents.csv`

| coluna | tipo_pandas | nulos | percentual_nulos | unicos | percentual_unicos | exemplos | minimo | maximo | media | mediana | zeros | percentual_zeros | padrao | hipotese | confianca | validacao |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| incident_id | str | 0 | 0.00% | 170 | 100.00% | INC00000001, INC00000002, INC00000003 |  |  |  |  |  |  | Texto curto ou código descritivo. | possível identificador | alto | Validar se é chave primária |
| trip_id | str | 0 | 0.00% | 170 | 100.00% | TRIP00036079, TRIP00032462, TRIP00067583 |  |  |  |  |  |  | Texto curto ou código descritivo. | possível identificador | alto | Validar se é chave primária |
| truck_id | str | 1 | 0.59% | 80 | 47.06% | TRK00006, TRK00084, TRK00106 |  |  |  |  |  |  | Texto curto ou código descritivo. | possível chave estrangeira | médio | Validar relacionamento |
| driver_id | str | 1 | 0.59% | 92 | 54.12% | DRV00006, DRV00119, DRV00134 |  |  |  |  |  |  | Texto curto ou código descritivo. | possível chave estrangeira | médio | Validar relacionamento |
| incident_date | str | 0 | 0.00% | 169 | 99.41% | 2023-04-09 14:00:00, 2023-02-19 11:00:00, 2024-05-20 01:00:00 |  |  |  |  |  |  | Texto com padrão provável de data. | possível data | médio | Validar formato antes de converter |
| incident_type | str | 0 | 0.00% | 5 | 2.94% | Moving Violation, Customer Complaint, Equipment Damage |  |  |  |  |  |  | Texto curto ou código descritivo. | possível categoria/status/código | médio | Validar domínio de valores |
| location_city | str | 0 | 0.00% | 25 | 14.71% | Columbus, Seattle, Kansas City |  |  |  |  |  |  | Texto curto ou código descritivo. | possível categoria/status/código | médio | Validar domínio de valores |
| location_state | str | 0 | 0.00% | 23 | 13.53% | PA, NC, OK |  |  |  |  |  |  | Texto curto ou código descritivo. | possível categoria/status/código | médio | Validar domínio de valores |
| at_fault_flag | bool | 0 | 0.00% | 2 | 1.18% | True, False | 0.0 | 1.0 | 0.3176 | 0.0 | 116 | 68.24% | Numérico | possível booleano | alto | Validar regra de negócio |
| injury_flag | bool | 0 | 0.00% | 2 | 1.18% | False, True | 0.0 | 1.0 | 0.1941 | 0.0 | 137 | 80.59% | Numérico | possível booleano | alto | Validar regra de negócio |
| vehicle_damage_cost | float64 | 0 | 0.00% | 119 | 70.00% | 12629.26, 2700.7, 24302.32 | 0.0 | 24614.16 | 9432.7124 | 8035.265 | 52 | 30.59% | Numérico | possível valor financeiro | alto | Validar moeda e regra |
| cargo_damage_cost | float64 | 0 | 0.00% | 49 | 28.82% | 0.0, 14284.24, 28315.16 | 0.0 | 49744.07 | 6174.1806 | 0.0 | 122 | 71.76% | Numérico | possível valor financeiro | alto | Validar moeda e regra |
| claim_amount | float64 | 0 | 0.00% | 132 | 77.65% | 12629.26, 16984.94, 24302.32 | 0.0 | 64245.72 | 15606.8931 | 13627.185 | 39 | 22.94% | Numérico | possível valor financeiro | alto | Validar moeda e regra |
| preventable_flag | bool | 0 | 0.00% | 2 | 1.18% | True, False | 0.0 | 1.0 | 0.3765 | 0.0 | 106 | 62.35% | Numérico | possível booleano | alto | Validar regra de negócio |
| description | str | 0 | 0.00% | 12 | 7.06% | Severe incident involving equipment, Severe incident involving weather, Minor incident involving traffic |  |  |  |  |  |  | Texto curto ou código descritivo. | possível texto livre com possível risco | médio | Sim |

### `trailers.csv`

| coluna | tipo_pandas | nulos | percentual_nulos | unicos | percentual_unicos | exemplos | minimo | maximo | media | mediana | zeros | percentual_zeros | padrao | hipotese | confianca | validacao |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| trailer_id | str | 0 | 0.00% | 180 | 100.00% | TRL00001, TRL00002, TRL00003 |  |  |  |  |  |  | Texto curto ou código descritivo. | possível identificador | alto | Validar se é chave primária |
| trailer_number | int64 | 0 | 0.00% | 176 | 97.78% | 4290, 8848, 6147 | 1072.0 | 9939.0 | 5881.6778 | 6150.5 | 0 | 0.00% | Numérico | possível código operacional ou número de unidade | alto | Não tratar como métrica |
| trailer_type | str | 0 | 0.00% | 2 | 1.11% | Refrigerated, Dry Van |  |  |  |  |  |  | Texto curto ou código descritivo. | possível categoria/status/código | médio | Validar domínio de valores |
| length_feet | int64 | 0 | 0.00% | 1 | 0.56% | 53 | 53.0 | 53.0 | 53.0 | 53.0 | 0 | 0.00% | Numérico | ambíguo / exige validação humana | baixo | Validação humana obrigatória |
| model_year | int64 | 0 | 0.00% | 10 | 5.56% | 2016, 2018, 2022 | 2015.0 | 2024.0 | 2019.1444 | 2019.0 | 0 | 0.00% | Numérico | possível ano/atributo temporal | alto | Validar significado |
| vin | str | 0 | 0.00% | 180 | 100.00% | 1AV889081755621178, 1BU942062588832828, 1AV669057807416326 |  |  |  |  |  |  | Texto curto ou código descritivo. | possível identificador operacional confidencial | alto | Sim |
| acquisition_date | str | 0 | 0.00% | 173 | 96.11% | 2018-05-11, 2018-11-24, 2019-01-28 |  |  |  |  |  |  | Texto com padrão provável de data. | possível data | médio | Validar formato antes de converter |
| status | str | 0 | 0.00% | 1 | 0.56% | Active |  |  |  |  |  |  | Texto curto ou código descritivo. | possível categoria/status/código | médio | Validar domínio de valores |
| current_location | str | 0 | 0.00% | 25 | 13.89% | Kansas City, Milwaukee, New York |  |  |  |  |  |  | Texto curto ou código descritivo. | possível categoria/status/código | médio | Validar domínio de valores |

### `trips.csv`

| coluna | tipo_pandas | nulos | percentual_nulos | unicos | percentual_unicos | exemplos | minimo | maximo | media | mediana | zeros | percentual_zeros | padrao | hipotese | confianca | validacao |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| trip_id | str | 0 | 0.00% | 85410 | 100.00% | TRIP00000001, TRIP00000002, TRIP00000003 |  |  |  |  |  |  | Texto curto ou código descritivo. | possível identificador | alto | Validar se é chave primária |
| load_id | str | 0 | 0.00% | 85410 | 100.00% | LOAD00000001, LOAD00000002, LOAD00000003 |  |  |  |  |  |  | Texto curto ou código descritivo. | possível identificador | alto | Validar se é chave primária |
| driver_id | str | 1714 | 2.01% | 124 | 0.15% | DRV00117, DRV00141, DRV00032 |  |  |  |  |  |  | Texto curto ou código descritivo. | possível chave estrangeira | médio | Validar relacionamento |
| truck_id | str | 1672 | 1.96% | 92 | 0.11% | TRK00035, TRK00108, TRK00031 |  |  |  |  |  |  | Texto curto ou código descritivo. | possível chave estrangeira | médio | Validar relacionamento |
| trailer_id | str | 1680 | 1.97% | 180 | 0.21% | TRL00167, TRL00082, TRL00138 |  |  |  |  |  |  | Texto curto ou código descritivo. | possível chave estrangeira | médio | Validar relacionamento |
| dispatch_date | str | 0 | 0.00% | 1096 | 1.28% | 2022-01-01, 2022-01-02, 2022-01-03 |  |  |  |  |  |  | Texto com padrão provável de data. | possível data | médio | Validar formato antes de converter |
| actual_distance_miles | int64 | 0 | 0.00% | 2818 | 3.30% | 1314, 515, 2509 | 90.0 | 3391.0 | 1430.2681 | 1297.5 | 0 | 0.00% | Numérico | possível quantidade ou métrica contínua | médio | Validar unidade e agregação |
| actual_duration_hours | float64 | 0 | 0.00% | 632 | 0.74% | 26.2, 8.6, 45.0 | 1.4 | 67.8 | 25.0147 | 23.0 | 0 | 0.00% | Numérico | possível métrica de duração | alto | Validar unidade |
| fuel_gallons_used | float64 | 0 | 0.00% | 5247 | 6.14% | 183.8, 93.6, 339.1 | 12.0 | 611.9 | 221.8274 | 204.5 | 0 | 0.00% | Numérico | possível quantidade ou métrica contínua | médio | Validar unidade e agregação |
| average_mpg | float64 | 0 | 0.00% | 201 | 0.24% | 7.15, 5.5, 7.4 | 5.5 | 7.5 | 6.5015 | 6.5 | 0 | 0.00% | Numérico | possível média | alto | Não somar diretamente |
| idle_time_hours | float64 | 0 | 0.00% | 101 | 0.12% | 3.5, 8.3, 12.0 | 2.0 | 12.0 | 7.0108 | 7.0 | 0 | 0.00% | Numérico | possível métrica de duração | alto | Validar unidade |
| trip_status | str | 0 | 0.00% | 1 | 0.00% | Completed |  |  |  |  |  |  | Texto curto ou código descritivo. | possível categoria/status/código | médio | Validar domínio de valores |

### `truck_utilization_metrics.csv`

| coluna | tipo_pandas | nulos | percentual_nulos | unicos | percentual_unicos | exemplos | minimo | maximo | media | mediana | zeros | percentual_zeros | padrao | hipotese | confianca | validacao |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| truck_id | str | 0 | 0.00% | 92 | 2.78% | TRK00001, TRK00002, TRK00004 |  |  |  |  |  |  | Texto curto ou código descritivo. | possível chave estrangeira | médio | Validar relacionamento |
| month | str | 0 | 0.00% | 36 | 1.09% | 2022-01-01, 2022-02-01, 2022-03-01 |  |  |  |  |  |  | Texto com padrão provável de data. | possível data | médio | Validar formato antes de converter |
| trips_completed | int64 | 0 | 0.00% | 35 | 1.06% | 22, 27, 34 | 11.0 | 46.0 | 25.2832 | 25.0 | 0 | 0.00% | Numérico | possível contagem | alto | Validar unidade |
| total_miles | int64 | 0 | 0.00% | 3134 | 94.63% | 39269, 40787, 57422 | 12680.0 | 71177.0 | 36152.2301 | 35758.0 | 0 | 0.00% | Numérico | possível quantidade ou métrica contínua | médio | Validar unidade e agregação |
| total_revenue | float64 | 0 | 0.00% | 3310 | 99.94% | 84792.02, 88809.05, 120453.71 | 27876.18 | 144891.1 | 77700.5616 | 76607.69 | 0 | 0.00% | Numérico | possível valor financeiro | alto | Validar moeda e regra |
| average_mpg | float64 | 0 | 0.00% | 76 | 2.29% | 6.78, 6.23, 6.49 | 6.01 | 6.86 | 6.501 | 6.5 | 0 | 0.00% | Numérico | possível média | alto | Não somar diretamente |
| maintenance_events | int64 | 0 | 0.00% | 5 | 0.15% | 2, 0, 1 | 0.0 | 4.0 | 0.6733 | 0.0 | 1684 | 50.85% | Numérico | possível contagem | alto | Validar unidade |
| maintenance_cost | float64 | 0 | 0.00% | 1627 | 49.12% | 4380.98, 0.0, 3548.15 | 0.0 | 10414.66 | 1307.1876 | 0.0 | 1684 | 50.85% | Numérico | possível valor financeiro | alto | Validar moeda e regra |
| downtime_hours | float64 | 0 | 0.00% | 655 | 19.78% | 63.1, 0.0, 71.8 | 0.0 | 152.2 | 16.5496 | 0.0 | 1684 | 50.85% | Numérico | possível métrica de duração | alto | Validar unidade |
| utilization_rate | float64 | 0 | 0.00% | 103 | 3.11% | 0.71, 0.964, 1.097 | 0.387 | 1.484 | 0.8304 | 0.833 | 0 | 0.00% | Numérico | possível percentual em escala 0 a 100 | médio | Validar escala |

### `trucks.csv`

| coluna | tipo_pandas | nulos | percentual_nulos | unicos | percentual_unicos | exemplos | minimo | maximo | media | mediana | zeros | percentual_zeros | padrao | hipotese | confianca | validacao |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| truck_id | str | 0 | 0.00% | 120 | 100.00% | TRK00001, TRK00002, TRK00003 |  |  |  |  |  |  | Texto curto ou código descritivo. | possível identificador | alto | Validar se é chave primária |
| unit_number | int64 | 0 | 0.00% | 120 | 100.00% | 3463, 6461, 2335 | 1086.0 | 9991.0 | 5568.6417 | 5669.0 | 0 | 0.00% | Numérico | possível código operacional ou número de unidade | alto | Não tratar como métrica |
| make | str | 0 | 0.00% | 6 | 5.00% | Peterbilt, Kenworth, Freightliner |  |  |  |  |  |  | Texto curto ou código descritivo. | possível categoria/status/código | médio | Validar domínio de valores |
| model_year | int64 | 0 | 0.00% | 7 | 5.83% | 2016, 2015, 2018 | 2015.0 | 2021.0 | 2015.8917 | 2015.0 | 0 | 0.00% | Numérico | possível ano/atributo temporal | alto | Validar significado |
| vin | str | 0 | 0.00% | 120 | 100.00% | 1VV205190335317039, 1NV753749606229960, 1NT803101860493229 |  |  |  |  |  |  | Texto curto ou código descritivo. | possível identificador operacional confidencial | alto | Sim |
| acquisition_date | str | 0 | 0.00% | 119 | 99.17% | 2017-04-27, 2018-10-04, 2020-09-17 |  |  |  |  |  |  | Texto com padrão provável de data. | possível data | médio | Validar formato antes de converter |
| acquisition_mileage | int64 | 0 | 0.00% | 120 | 100.00% | 18814, 26795, 11795 | 227.0 | 49556.0 | 26058.2167 | 26060.5 | 0 | 0.00% | Numérico | possível identificador operacional confidencial | baixo | Validar significado |
| fuel_type | str | 0 | 0.00% | 1 | 0.83% | Diesel |  |  |  |  |  |  | Texto curto ou código descritivo. | possível categoria/status/código | médio | Validar domínio de valores |
| tank_capacity_gallons | int64 | 0 | 0.00% | 3 | 2.50% | 200, 150, 250 | 150.0 | 250.0 | 201.6667 | 200.0 | 0 | 0.00% | Numérico | possível quantidade ou métrica contínua | médio | Validar unidade e agregação |
| status | str | 0 | 0.00% | 3 | 2.50% | Active, Maintenance, Inactive |  |  |  |  |  |  | Texto curto ou código descritivo. | possível categoria/status/código | médio | Validar domínio de valores |
| home_terminal | str | 0 | 0.00% | 24 | 20.00% | Omaha, Seattle, Atlanta |  |  |  |  |  |  | Texto curto ou código descritivo. | possível categoria/status/código | médio | Validar domínio de valores |

## 7. Regras de interpretação por comportamento dos dados

1. Uma coluna com alta cardinalidade, muitos valores únicos e valores repetidos raramente pode ser possível identificador.
2. Uma coluna com valores somente `True/False`, `0/1`, `sim/não`, `yes/no` ou equivalentes pode ser possível booleano.
3. Uma coluna numérica com valores entre 0 e 1 pode ser percentual, taxa, score ou índice em escala decimal, mas exige validação humana.
4. Uma coluna numérica com valores entre 0 e 100 pode ser percentual em escala 0 a 100, quantidade, nota ou métrica operacional, exigindo validação humana.
5. Uma coluna numérica positiva com casas decimais e grande variação pode ser valor financeiro, métrica contínua, preço, custo, receita ou medida operacional.
6. Uma coluna com poucos valores únicos e muitos registros pode ser categoria, status ou código.
7. Uma coluna textual longa pode ser descrição, observação ou campo livre.
8. Uma coluna com padrões de data em texto deve ser candidata a data, mesmo que o nome da coluna não indique data.
9. Uma coluna com números inteiros sequenciais pode ser identificador, código operacional ou número de unidade, não necessariamente métrica.
10. Campos com comportamento de média, taxa, percentual, preço unitário ou índice não devem ser somados diretamente.
11. Nomes de colunas devem ser tratados apenas como pistas auxiliares.
12. Quando comportamento dos dados e nomenclatura divergirem, o relatório registra conflito e pede validação humana.

## 8. Leitura inicial dos relacionamentos

| Relação hipotética | Chaves distintas A | Chaves distintas B | Cobertura percentual | IDs órfãos | Cardinalidade observada | Cardinalidade conceitual provável | Nível de confiança | Observação |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| loads.csv.load_id ↔ trips.csv.load_id | 85410 | 85410 | A→B 100.00% / B→A 100.00% | A sem B: 0; B sem A: 0 | 1:1 observado | 1:N potencial | alto | Hipótese de modelagem; cardinalidade observada não é verdade conceitual definitiva. |
| trips.csv.trip_id ↔ delivery_events.csv.trip_id | 85410 | 85410 | A→B 100.00% / B→A 100.00% | A sem B: 0; B sem A: 0 | 1:N observado | 1:N potencial | alto | Hipótese de modelagem; cardinalidade observada não é verdade conceitual definitiva. |
| customers.csv.customer_id ↔ loads.csv.customer_id | 200 | 200 | A→B 100.00% / B→A 100.00% | A sem B: 0; B sem A: 0 | 1:N observado | 1:N potencial | alto | Hipótese de modelagem; cardinalidade observada não é verdade conceitual definitiva. |
| routes.csv.route_id ↔ loads.csv.route_id | 58 | 58 | A→B 100.00% / B→A 100.00% | A sem B: 0; B sem A: 0 | 1:N observado | 1:N potencial | alto | Hipótese de modelagem; cardinalidade observada não é verdade conceitual definitiva. |
| drivers.csv.driver_id ↔ trips.csv.driver_id | 150 | 124 | A→B 82.67% / B→A 100.00% | A sem B: 26; B sem A: 0 | 1:N observado | 1:N potencial | alto | Hipótese de modelagem; cardinalidade observada não é verdade conceitual definitiva. |
| trucks.csv.truck_id ↔ trips.csv.truck_id | 120 | 92 | A→B 76.67% / B→A 100.00% | A sem B: 28; B sem A: 0 | 1:N observado | 1:N potencial | alto | Hipótese de modelagem; cardinalidade observada não é verdade conceitual definitiva. |
| trailers.csv.trailer_id ↔ trips.csv.trailer_id | 180 | 180 | A→B 100.00% / B→A 100.00% | A sem B: 0; B sem A: 0 | 1:N observado | 1:N potencial | alto | Hipótese de modelagem; cardinalidade observada não é verdade conceitual definitiva. |
| facilities.csv.facility_id ↔ delivery_events.csv.facility_id | 50 | 50 | A→B 100.00% / B→A 100.00% | A sem B: 0; B sem A: 0 | 1:N observado | 1:N potencial | alto | Hipótese de modelagem; cardinalidade observada não é verdade conceitual definitiva. |
| trips.csv.trip_id ↔ fuel_purchases.csv.trip_id | 85410 | 76939 | A→B 90.08% / B→A 100.00% | A sem B: 8471; B sem A: 0 | 1:N observado | 1:N potencial | alto | Hipótese de modelagem; cardinalidade observada não é verdade conceitual definitiva. |
| trucks.csv.truck_id ↔ fuel_purchases.csv.truck_id | 120 | 92 | A→B 76.67% / B→A 100.00% | A sem B: 28; B sem A: 0 | 1:N observado | 1:N potencial | alto | Hipótese de modelagem; cardinalidade observada não é verdade conceitual definitiva. |
| trucks.csv.truck_id ↔ maintenance_records.csv.truck_id | 120 | 120 | A→B 100.00% / B→A 100.00% | A sem B: 0; B sem A: 0 | 1:N observado | 1:N potencial | alto | Hipótese de modelagem; cardinalidade observada não é verdade conceitual definitiva. |
| trips.csv.trip_id ↔ safety_incidents.csv.trip_id | 85410 | 170 | A→B 0.20% / B→A 100.00% | A sem B: 85240; B sem A: 0 | 1:1 observado | 1:N potencial | alto | Hipótese de modelagem; cardinalidade observada não é verdade conceitual definitiva. |
| delivery_events.csv.facility_id ↔ facilities.csv.facility_id | 50 | 50 | A→B 100.00% / B→A 100.00% | A sem B: 0; B sem A: 0 | N:1 observado | cardinalidade conceitual exige validação | alto | Hipótese de modelagem; cardinalidade observada não é verdade conceitual definitiva. |
| delivery_events.csv.trip_id ↔ fuel_purchases.csv.trip_id | 85410 | 76939 | A→B 90.08% / B→A 100.00% | A sem B: 8471; B sem A: 0 | N:N observado | cardinalidade conceitual exige validação | alto | Hipótese de modelagem; cardinalidade observada não é verdade conceitual definitiva. |
| delivery_events.csv.load_id ↔ loads.csv.load_id | 85410 | 85410 | A→B 100.00% / B→A 100.00% | A sem B: 0; B sem A: 0 | N:1 observado | cardinalidade conceitual exige validação | alto | Hipótese de modelagem; cardinalidade observada não é verdade conceitual definitiva. |
| delivery_events.csv.trip_id ↔ safety_incidents.csv.trip_id | 85410 | 170 | A→B 0.20% / B→A 100.00% | A sem B: 85240; B sem A: 0 | N:1 observado | cardinalidade conceitual exige validação | alto | Hipótese de modelagem; cardinalidade observada não é verdade conceitual definitiva. |
| delivery_events.csv.load_id ↔ trips.csv.load_id | 85410 | 85410 | A→B 100.00% / B→A 100.00% | A sem B: 0; B sem A: 0 | N:1 observado | cardinalidade conceitual exige validação | alto | Hipótese de modelagem; cardinalidade observada não é verdade conceitual definitiva. |
| delivery_events.csv.trip_id ↔ trips.csv.trip_id | 85410 | 85410 | A→B 100.00% / B→A 100.00% | A sem B: 0; B sem A: 0 | N:1 observado | cardinalidade conceitual exige validação | alto | Hipótese de modelagem; cardinalidade observada não é verdade conceitual definitiva. |
| driver_monthly_metrics.csv.driver_id ↔ drivers.csv.driver_id | 124 | 150 | A→B 100.00% / B→A 82.67% | A sem B: 0; B sem A: 26 | N:1 observado | N:1 potencial com granularidade entidade + período; exige cuidado | alto | Tabela agregada mensal detectada; a relação com dimensão tende a ser N:1 por entidade, mas a granularidade entidade + período exige cuidado. |
| driver_monthly_metrics.csv.driver_id ↔ fuel_purchases.csv.driver_id | 124 | 124 | A→B 100.00% / B→A 100.00% | A sem B: 0; B sem A: 0 | repetição observada por entidade + período | N:1 potencial com granularidade entidade + período; exige cuidado | alto | Tabela agregada mensal detectada; a relação com dimensão tende a ser N:1 por entidade, mas a granularidade entidade + período exige cuidado. |
| driver_monthly_metrics.csv.driver_id ↔ safety_incidents.csv.driver_id | 124 | 92 | A→B 74.19% / B→A 100.00% | A sem B: 32; B sem A: 0 | repetição observada por entidade + período | N:1 potencial com granularidade entidade + período; exige cuidado | alto | Tabela agregada mensal detectada; a relação com dimensão tende a ser N:1 por entidade, mas a granularidade entidade + período exige cuidado. |
| driver_monthly_metrics.csv.driver_id ↔ trips.csv.driver_id | 124 | 124 | A→B 100.00% / B→A 100.00% | A sem B: 0; B sem A: 0 | repetição observada por entidade + período | N:1 potencial com granularidade entidade + período; exige cuidado | alto | Tabela agregada mensal detectada; a relação com dimensão tende a ser N:1 por entidade, mas a granularidade entidade + período exige cuidado. |
| drivers.csv.driver_id ↔ fuel_purchases.csv.driver_id | 150 | 124 | A→B 82.67% / B→A 100.00% | A sem B: 26; B sem A: 0 | 1:N observado | cardinalidade conceitual exige validação | alto | Hipótese de modelagem; cardinalidade observada não é verdade conceitual definitiva. |
| drivers.csv.driver_id ↔ safety_incidents.csv.driver_id | 150 | 92 | A→B 61.33% / B→A 100.00% | A sem B: 58; B sem A: 0 | 1:N observado | cardinalidade conceitual exige validação | alto | Hipótese de modelagem; cardinalidade observada não é verdade conceitual definitiva. |
| fuel_purchases.csv.truck_id ↔ maintenance_records.csv.truck_id | 92 | 120 | A→B 100.00% / B→A 76.67% | A sem B: 0; B sem A: 28 | N:N observado | cardinalidade conceitual exige validação | alto | Hipótese de modelagem; cardinalidade observada não é verdade conceitual definitiva. |
| fuel_purchases.csv.driver_id ↔ safety_incidents.csv.driver_id | 124 | 92 | A→B 74.19% / B→A 100.00% | A sem B: 32; B sem A: 0 | N:N observado | cardinalidade conceitual exige validação | alto | Hipótese de modelagem; cardinalidade observada não é verdade conceitual definitiva. |
| fuel_purchases.csv.trip_id ↔ safety_incidents.csv.trip_id | 76939 | 170 | A→B 0.20% / B→A 90.00% | A sem B: 76786; B sem A: 17 | N:1 observado | cardinalidade conceitual exige validação | alto | Hipótese de modelagem; cardinalidade observada não é verdade conceitual definitiva. |
| fuel_purchases.csv.truck_id ↔ safety_incidents.csv.truck_id | 92 | 80 | A→B 86.96% / B→A 100.00% | A sem B: 12; B sem A: 0 | N:N observado | cardinalidade conceitual exige validação | alto | Hipótese de modelagem; cardinalidade observada não é verdade conceitual definitiva. |
| fuel_purchases.csv.driver_id ↔ trips.csv.driver_id | 124 | 124 | A→B 100.00% / B→A 100.00% | A sem B: 0; B sem A: 0 | N:N observado | cardinalidade conceitual exige validação | alto | Hipótese de modelagem; cardinalidade observada não é verdade conceitual definitiva. |
| fuel_purchases.csv.trip_id ↔ trips.csv.trip_id | 76939 | 85410 | A→B 100.00% / B→A 90.08% | A sem B: 0; B sem A: 8471 | N:1 observado | cardinalidade conceitual exige validação | alto | Hipótese de modelagem; cardinalidade observada não é verdade conceitual definitiva. |
| fuel_purchases.csv.truck_id ↔ trips.csv.truck_id | 92 | 92 | A→B 100.00% / B→A 100.00% | A sem B: 0; B sem A: 0 | N:N observado | cardinalidade conceitual exige validação | alto | Hipótese de modelagem; cardinalidade observada não é verdade conceitual definitiva. |
| fuel_purchases.csv.truck_id ↔ truck_utilization_metrics.csv.truck_id | 92 | 92 | A→B 100.00% / B→A 100.00% | A sem B: 0; B sem A: 0 | repetição observada por entidade + período | N:1 potencial com granularidade entidade + período; exige cuidado | alto | Tabela agregada mensal detectada; a relação com dimensão tende a ser N:1 por entidade, mas a granularidade entidade + período exige cuidado. |
| fuel_purchases.csv.truck_id ↔ trucks.csv.truck_id | 92 | 120 | A→B 100.00% / B→A 76.67% | A sem B: 0; B sem A: 28 | N:1 observado | cardinalidade conceitual exige validação | alto | Hipótese de modelagem; cardinalidade observada não é verdade conceitual definitiva. |
| loads.csv.route_id ↔ routes.csv.route_id | 58 | 58 | A→B 100.00% / B→A 100.00% | A sem B: 0; B sem A: 0 | N:1 observado | cardinalidade conceitual exige validação | alto | Hipótese de modelagem; cardinalidade observada não é verdade conceitual definitiva. |
| maintenance_records.csv.truck_id ↔ safety_incidents.csv.truck_id | 120 | 80 | A→B 66.67% / B→A 100.00% | A sem B: 40; B sem A: 0 | N:N observado | cardinalidade conceitual exige validação | alto | Hipótese de modelagem; cardinalidade observada não é verdade conceitual definitiva. |
| maintenance_records.csv.truck_id ↔ trips.csv.truck_id | 120 | 92 | A→B 76.67% / B→A 100.00% | A sem B: 28; B sem A: 0 | N:N observado | cardinalidade conceitual exige validação | alto | Hipótese de modelagem; cardinalidade observada não é verdade conceitual definitiva. |
| maintenance_records.csv.truck_id ↔ truck_utilization_metrics.csv.truck_id | 120 | 92 | A→B 76.67% / B→A 100.00% | A sem B: 28; B sem A: 0 | repetição observada por entidade + período | N:1 potencial com granularidade entidade + período; exige cuidado | alto | Tabela agregada mensal detectada; a relação com dimensão tende a ser N:1 por entidade, mas a granularidade entidade + período exige cuidado. |
| maintenance_records.csv.truck_id ↔ trucks.csv.truck_id | 120 | 120 | A→B 100.00% / B→A 100.00% | A sem B: 0; B sem A: 0 | N:1 observado | cardinalidade conceitual exige validação | alto | Hipótese de modelagem; cardinalidade observada não é verdade conceitual definitiva. |
| safety_incidents.csv.driver_id ↔ trips.csv.driver_id | 92 | 124 | A→B 100.00% / B→A 74.19% | A sem B: 0; B sem A: 32 | N:N observado | cardinalidade conceitual exige validação | alto | Hipótese de modelagem; cardinalidade observada não é verdade conceitual definitiva. |
| safety_incidents.csv.trip_id ↔ trips.csv.trip_id | 170 | 85410 | A→B 100.00% / B→A 0.20% | A sem B: 0; B sem A: 85240 | 1:1 observado | cardinalidade conceitual exige validação | alto | Hipótese de modelagem; cardinalidade observada não é verdade conceitual definitiva. |
| safety_incidents.csv.truck_id ↔ trips.csv.truck_id | 80 | 92 | A→B 100.00% / B→A 86.96% | A sem B: 0; B sem A: 12 | N:N observado | cardinalidade conceitual exige validação | alto | Hipótese de modelagem; cardinalidade observada não é verdade conceitual definitiva. |
| safety_incidents.csv.truck_id ↔ truck_utilization_metrics.csv.truck_id | 80 | 92 | A→B 100.00% / B→A 86.96% | A sem B: 0; B sem A: 12 | repetição observada por entidade + período | N:1 potencial com granularidade entidade + período; exige cuidado | alto | Tabela agregada mensal detectada; a relação com dimensão tende a ser N:1 por entidade, mas a granularidade entidade + período exige cuidado. |
| safety_incidents.csv.truck_id ↔ trucks.csv.truck_id | 80 | 120 | A→B 100.00% / B→A 66.67% | A sem B: 0; B sem A: 40 | N:1 observado | cardinalidade conceitual exige validação | alto | Hipótese de modelagem; cardinalidade observada não é verdade conceitual definitiva. |
| trips.csv.truck_id ↔ truck_utilization_metrics.csv.truck_id | 92 | 92 | A→B 100.00% / B→A 100.00% | A sem B: 0; B sem A: 0 | repetição observada por entidade + período | N:1 potencial com granularidade entidade + período; exige cuidado | alto | Tabela agregada mensal detectada; a relação com dimensão tende a ser N:1 por entidade, mas a granularidade entidade + período exige cuidado. |
| trips.csv.truck_id ↔ trucks.csv.truck_id | 92 | 120 | A→B 100.00% / B→A 76.67% | A sem B: 0; B sem A: 28 | N:1 observado | cardinalidade conceitual exige validação | alto | Hipótese de modelagem; cardinalidade observada não é verdade conceitual definitiva. |
| truck_utilization_metrics.csv.truck_id ↔ trucks.csv.truck_id | 92 | 120 | A→B 100.00% / B→A 76.67% | A sem B: 0; B sem A: 28 | N:1 observado | N:1 potencial com granularidade entidade + período; exige cuidado | alto | Tabela agregada mensal detectada; a relação com dimensão tende a ser N:1 por entidade, mas a granularidade entidade + período exige cuidado. |

## 9. Campos que exigem cuidado de agregação

| Tabela | Coluna | Motivo do cuidado | Agregação preliminar sugerida | Nível de confiança | Validação humana necessária |
| --- | --- | --- | --- | --- | --- |
| customers.csv | account_status | status codificado ou categoria operacional | contagem | médio | Sim |
| driver_monthly_metrics.csv | average_mpg | média operacional; soma direta distorce interpretação | média ponderada | alto | Sim |
| driver_monthly_metrics.csv | on_time_delivery_rate | percentual, taxa, índice ou score | média ponderada | alto | Sim |
| driver_monthly_metrics.csv | average_idle_hours | média operacional; soma direta distorce interpretação | média ponderada | alto | Sim |
| drivers.csv | employment_status | status codificado ou categoria operacional | contagem | médio | Sim |
| fuel_purchases.csv | price_per_gallon | taxa monetária por unidade ou preço unitário | média ponderada | alto | Sim |
| loads.csv | load_status | status codificado ou categoria operacional | contagem | médio | Sim |
| routes.csv | base_rate_per_mile | taxa monetária por unidade ou preço unitário | média ponderada | alto | Sim |
| routes.csv | fuel_surcharge_rate | percentual, taxa, índice ou score | média ponderada | alto | Sim |
| trailers.csv | status | status codificado ou categoria operacional | contagem | médio | Sim |
| trips.csv | average_mpg | média operacional; soma direta distorce interpretação | média ponderada | alto | Sim |
| trips.csv | trip_status | status codificado ou categoria operacional | contagem | médio | Sim |
| truck_utilization_metrics.csv | average_mpg | média operacional; soma direta distorce interpretação | média ponderada | alto | Sim |
| truck_utilization_metrics.csv | utilization_rate | percentual, taxa, índice ou score | média ponderada | alto | Sim |
| trucks.csv | status | status codificado ou categoria operacional | contagem | médio | Sim |

## 10. Campos pessoais, identificáveis ou confidenciais

| Tabela | Coluna | Tipo de risco | Evidência | Recomendação preliminar para arquivos finais públicos | Nível de confiança | Validação humana necessária |
| --- | --- | --- | --- | --- | --- | --- |
| customers.csv | customer_name | dado comercial confidencial | Nome da coluna indica cliente identificado. | Avaliar anonimização ou uso controlado. | médio | Sim |
| drivers.csv | first_name | dado pessoal | Nome da coluna indica identificação de pessoa. | Remover, mascarar ou controlar acesso. | alto | Sim |
| drivers.csv | last_name | dado pessoal | Nome da coluna indica identificação de pessoa. | Remover, mascarar ou controlar acesso. | alto | Sim |
| drivers.csv | license_number | dado pessoal/identificável | Nome da coluna indica número de licença individual. | Remover, mascarar ou controlar acesso. | alto | Sim |
| drivers.csv | date_of_birth | dado pessoal | Nome da coluna indica identificação de pessoa. | Remover, mascarar ou controlar acesso. | alto | Sim |
| fuel_purchases.csv | fuel_card_number | identificador operacional confidencial | Nome da coluna indica identificador operacional sensível. | Remover, mascarar ou restringir em arquivos finais públicos. | alto | Sim |
| maintenance_records.csv | service_description | texto livre com possível risco | Campo textual livre pode conter informação sensível não padronizada. | Revisar conteúdo antes de qualquer publicação. | médio | Sim |
| safety_incidents.csv | description | texto livre com possível risco | Campo textual livre pode conter informação sensível não padronizada. | Revisar conteúdo antes de qualquer publicação. | médio | Sim |
| trailers.csv | vin | identificador operacional confidencial | Nome da coluna indica identificador operacional sensível. | Remover, mascarar ou restringir em arquivos finais públicos. | alto | Sim |
| trucks.csv | vin | identificador operacional confidencial | Nome da coluna indica identificador operacional sensível. | Remover, mascarar ou restringir em arquivos finais públicos. | alto | Sim |

## 11. Leitura de entrega dos dados para próximas etapas

### 11.1 Dados tratados

`dados/tratados/` deverá conter tabelas limpas e documentadas, com:

- tipos padronizados;
- datas convertidas;
- IDs preservados como texto;
- campos pessoais removidos, mascarados ou controlados quando necessário;
- nulos tratados ou documentados;
- sem alteração dos dados brutos.

### 11.2 Dados finais

`dados/finais/` deverá conter bases prontas para Power BI, como:

- tabelas fato e dimensão selecionadas;
- tabelas agregadas de KPIs, quando aprovadas;
- campos de data prontos para ordenação;
- campos percentuais em escala correta;
- campos de status descritivos quando aprovados;
- campos sensíveis removidos ou mascarados para uso público.

### 11.3 Escopo sugerido para V1

Esta sugestão é uma hipótese inicial baseada nas evidências observadas, não apenas nos nomes das tabelas.

**Tabelas candidatas ao escopo principal:**

- `delivery_events.csv`
- `loads.csv`
- `trips.csv`

**Tabelas candidatas ao escopo complementar:**

- `facilities.csv`
- `routes.csv`

**Tabelas candidatas a fase futura:**

Nenhum campo identificado automaticamente.

**Tabelas que exigem cuidado por conter dados pessoais, confidenciais ou agregados:**

- `customers.csv`
- `driver_monthly_metrics.csv`
- `drivers.csv`
- `fuel_purchases.csv`
- `maintenance_records.csv`
- `safety_incidents.csv`
- `trailers.csv`
- `truck_utilization_metrics.csv`
- `trucks.csv`

## 12. Pontos críticos antes do plano de tratamento

- confirmação do escopo da V1;
- tratamento de dados pessoais e confidenciais;
- validação de escala de percentuais, taxas, índices e scores;
- separação entre taxa percentual e taxa monetária por unidade;
- campos que não devem ser somados diretamente;
- nulos em IDs operacionais;
- significado de campos nulos relevantes;
- validação de relacionamentos observados;
- diferença entre cardinalidade observada e cardinalidade conceitual;
- definição de quais campos entram nos arquivos finais públicos;
- validação humana das hipóteses com baixa ou média confiança.

## 13. Recomendações iniciais do Agente ADA

As recomendações abaixo são hipóteses iniciais e dependem de validação humana.

- IDs devem ser tratados como texto.
- Datas devem ser convertidas em etapa futura.
- Campos financeiros devem permanecer numéricos e ser formatados como moeda no Power BI.
- Percentuais e taxas precisam de validação de escala.
- Taxas monetárias por unidade não devem ser confundidas com percentuais.
- Métricas de tempo devem permanecer numéricas, com unidade documentada.
- Campos pessoais e confidenciais não devem ir para arquivos finais públicos sem aprovação.
- Campos médios, percentuais, índices e preços unitários não devem ser somados diretamente.
- Dados brutos devem permanecer preservados.
- Power BI deve receber dados finais já tratados, documentados e aprovados.

## 14. Validação humana necessária

- aprovar ou ajustar o escopo da V1;
- confirmar quais tabelas serão usadas no primeiro ciclo analítico;
- confirmar significado de colunas ambíguas;
- validar colunas cujo comportamento estatístico e nome não sejam suficientes;
- definir regras de tratamento para dados pessoais, identificáveis ou confidenciais;
- confirmar escala correta de percentuais e taxas;
- definir tratamento para valores ausentes;
- validar regras para campos de status e flags operacionais;
- confirmar relacionamentos entre tabelas;
- definir quais campos podem entrar em arquivos finais públicos;
- aprovar qualquer transformação antes de sua execução.

## Status da Etapa 01:

- [ ] Aprovada
- [x] Aprovada com ressalvas
- [ ] Reprovada para avanço

## Observações da validação humana:

- A Etapa 01 está aprovada como inspeção segura e interpretação inicial dos dados brutos.
- A abordagem híbrida Python + IA foi considerada adequada para gerar evidências técnicas e hipóteses interpretativas.
- As classificações continuam sendo hipóteses e não decisões finais.
- A Etapa 02 deve tratar com atenção especial datas/períodos, campos confidenciais, taxas percentuais versus taxas monetárias, campos que não devem ser somados diretamente, valores ausentes e granularidade das tabelas agregadas.
- Nenhuma transformação deve ser aplicada sem validação humana.