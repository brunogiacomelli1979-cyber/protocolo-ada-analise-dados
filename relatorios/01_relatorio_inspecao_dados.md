# Relatório de Inspeção Segura dos Dados Brutos

Gerado em: 2026-06-12 15:51:58

Este relatório foi gerado por leitura dos arquivos em `dados/brutos/`, sem alteração dos arquivos originais.

Todas as classificações automáticas são hipóteses iniciais e precisam de validação humana antes de qualquer tratamento.

## Documentação de estrutura da base

- `DATABASE_SCHEMA.txt` foi encontrado e lido apenas para confirmar a existência de documentação estrutural da base. Linhas: 87. Caracteres: 2750. O script não depende exclusivamente dele para decidir tipos ou regras.

## Arquivos CSV inspecionados

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

**Tipos de dados identificados pelo pandas:**

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

| Coluna | Valores nulos | Percentual nulo |
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

**Possíveis colunas de identificação:**

- `customer_id`

**Possíveis colunas de data/hora:**

- `contract_start_date`

**Possíveis campos numéricos:**

- `credit_terms_days`
- `annual_revenue_potential`

**Possíveis campos categóricos:**

Nenhum campo identificado automaticamente.

**Possíveis campos booleanos:**

Nenhum campo identificado automaticamente.

**Possíveis campos financeiros:**

- `annual_revenue_potential`

**Possíveis campos percentuais ou taxas:**

Nenhum campo identificado automaticamente.

**Possíveis métricas de tempo/duração:**

- `credit_terms_days`

**Possíveis campos sensíveis ou pessoais:**

- `customer_name`

**Observações iniciais sobre riscos de privacidade:**

Foram identificadas colunas com nomes que podem indicar dados pessoais ou sensíveis. Essa é uma hipótese inicial e exige validação humana antes de uso, exposição ou compartilhamento.

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

**Tipos de dados identificados pelo pandas:**

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

| Coluna | Valores nulos | Percentual nulo |
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

**Possíveis colunas de identificação:**

- `event_id`
- `load_id`
- `trip_id`
- `facility_id`

**Possíveis colunas de data/hora:**

- `scheduled_datetime`
- `actual_datetime`

**Possíveis campos numéricos:**

- `detention_minutes`

**Possíveis campos categóricos:**

Nenhum campo identificado automaticamente.

**Possíveis campos booleanos:**

- `on_time_flag`

**Possíveis campos financeiros:**

Nenhum campo identificado automaticamente.

**Possíveis campos percentuais ou taxas:**

Nenhum campo identificado automaticamente.

**Possíveis métricas de tempo/duração:**

- `detention_minutes`

**Possíveis campos sensíveis ou pessoais:**

Nenhum campo identificado automaticamente.

**Observações iniciais sobre riscos de privacidade:**

Nenhum campo sensível ou pessoal foi identificado automaticamente pelo nome da coluna.

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

**Tipos de dados identificados pelo pandas:**

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

| Coluna | Valores nulos | Percentual nulo |
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

**Possíveis colunas de identificação:**

- `driver_id`

**Possíveis colunas de data/hora:**

Nenhum campo identificado automaticamente.

**Possíveis campos numéricos:**

- `trips_completed`
- `total_miles`
- `total_revenue`
- `average_mpg`
- `total_fuel_gallons`
- `on_time_delivery_rate`
- `average_idle_hours`

**Possíveis campos categóricos:**

Nenhum campo identificado automaticamente.

**Possíveis campos booleanos:**

Nenhum campo identificado automaticamente.

**Possíveis campos financeiros:**

- `total_revenue`

**Possíveis campos percentuais ou taxas:**

- `on_time_delivery_rate`

**Possíveis métricas de tempo/duração:**

- `average_idle_hours`

**Possíveis campos sensíveis ou pessoais:**

Nenhum campo identificado automaticamente.

**Observações iniciais sobre riscos de privacidade:**

Nenhum campo sensível ou pessoal foi identificado automaticamente pelo nome da coluna.

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

**Tipos de dados identificados pelo pandas:**

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

| Coluna | Valores nulos | Percentual nulo |
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

**Possíveis colunas de identificação:**

- `driver_id`

**Possíveis colunas de data/hora:**

- `hire_date`
- `termination_date`
- `date_of_birth`

**Possíveis campos numéricos:**

- `years_experience`

**Possíveis campos categóricos:**

Nenhum campo identificado automaticamente.

**Possíveis campos booleanos:**

Nenhum campo identificado automaticamente.

**Possíveis campos financeiros:**

Nenhum campo identificado automaticamente.

**Possíveis campos percentuais ou taxas:**

Nenhum campo identificado automaticamente.

**Possíveis métricas de tempo/duração:**

Nenhum campo identificado automaticamente.

**Possíveis campos sensíveis ou pessoais:**

- `first_name`
- `last_name`
- `license_number`
- `date_of_birth`

**Observações iniciais sobre riscos de privacidade:**

Foram identificadas colunas com nomes que podem indicar dados pessoais ou sensíveis. Essa é uma hipótese inicial e exige validação humana antes de uso, exposição ou compartilhamento.

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

**Tipos de dados identificados pelo pandas:**

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

| Coluna | Valores nulos | Percentual nulo |
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

**Possíveis colunas de identificação:**

- `facility_id`

**Possíveis colunas de data/hora:**

Nenhum campo identificado automaticamente.

**Possíveis campos numéricos:**

- `latitude`
- `longitude`
- `dock_doors`

**Possíveis campos categóricos:**

Nenhum campo identificado automaticamente.

**Possíveis campos booleanos:**

Nenhum campo identificado automaticamente.

**Possíveis campos financeiros:**

Nenhum campo identificado automaticamente.

**Possíveis campos percentuais ou taxas:**

Nenhum campo identificado automaticamente.

**Possíveis métricas de tempo/duração:**

- `operating_hours`

**Possíveis campos sensíveis ou pessoais:**

Nenhum campo identificado automaticamente.

**Observações iniciais sobre riscos de privacidade:**

Nenhum campo sensível ou pessoal foi identificado automaticamente pelo nome da coluna. `facility_name` foi registrado como dado operacional de instalação, não como dado pessoal.

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

**Tipos de dados identificados pelo pandas:**

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

| Coluna | Valores nulos | Percentual nulo |
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

**Possíveis colunas de identificação:**

- `fuel_purchase_id`
- `trip_id`
- `truck_id`
- `driver_id`

**Possíveis colunas de data/hora:**

- `purchase_date`

**Possíveis campos numéricos:**

- `gallons`
- `price_per_gallon`
- `total_cost`

**Possíveis campos categóricos:**

Nenhum campo identificado automaticamente.

**Possíveis campos booleanos:**

Nenhum campo identificado automaticamente.

**Possíveis campos financeiros:**

- `price_per_gallon`
- `total_cost`

**Possíveis campos percentuais ou taxas:**

Nenhum campo identificado automaticamente.

**Possíveis métricas de tempo/duração:**

Nenhum campo identificado automaticamente.

**Possíveis campos sensíveis ou pessoais:**

Nenhum campo identificado automaticamente.

**Observações iniciais sobre riscos de privacidade:**

Nenhum campo sensível ou pessoal foi identificado automaticamente pelo nome da coluna.

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

**Tipos de dados identificados pelo pandas:**

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

| Coluna | Valores nulos | Percentual nulo |
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

**Possíveis colunas de identificação:**

- `load_id`
- `customer_id`
- `route_id`

**Possíveis colunas de data/hora:**

- `load_date`

**Possíveis campos numéricos:**

- `weight_lbs`
- `pieces`
- `revenue`
- `fuel_surcharge`
- `accessorial_charges`

**Possíveis campos categóricos:**

Nenhum campo identificado automaticamente.

**Possíveis campos booleanos:**

Nenhum campo identificado automaticamente.

**Possíveis campos financeiros:**

- `revenue`
- `fuel_surcharge`
- `accessorial_charges`

**Possíveis campos percentuais ou taxas:**

Nenhum campo identificado automaticamente.

**Possíveis métricas de tempo/duração:**

Nenhum campo identificado automaticamente.

**Possíveis campos sensíveis ou pessoais:**

Nenhum campo identificado automaticamente.

**Observações iniciais sobre riscos de privacidade:**

Nenhum campo sensível ou pessoal foi identificado automaticamente pelo nome da coluna.

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

**Tipos de dados identificados pelo pandas:**

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

| Coluna | Valores nulos | Percentual nulo |
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

**Possíveis colunas de identificação:**

- `maintenance_id`
- `truck_id`

**Possíveis colunas de data/hora:**

- `maintenance_date`

**Possíveis campos numéricos:**

- `odometer_reading`
- `labor_hours`
- `labor_cost`
- `parts_cost`
- `total_cost`
- `downtime_hours`

**Possíveis campos categóricos:**

Nenhum campo identificado automaticamente.

**Possíveis campos booleanos:**

Nenhum campo identificado automaticamente.

**Possíveis campos financeiros:**

- `labor_cost`
- `parts_cost`
- `total_cost`

**Possíveis campos percentuais ou taxas:**

Nenhum campo identificado automaticamente.

**Possíveis métricas de tempo/duração:**

- `labor_hours`
- `downtime_hours`

**Possíveis campos sensíveis ou pessoais:**

Nenhum campo identificado automaticamente.

**Observações iniciais sobre riscos de privacidade:**

Nenhum campo sensível ou pessoal foi identificado automaticamente pelo nome da coluna.

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

**Tipos de dados identificados pelo pandas:**

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

| Coluna | Valores nulos | Percentual nulo |
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

**Possíveis colunas de identificação:**

- `route_id`

**Possíveis colunas de data/hora:**

Nenhum campo identificado automaticamente.

**Possíveis campos numéricos:**

- `typical_distance_miles`
- `base_rate_per_mile`
- `fuel_surcharge_rate`
- `typical_transit_days`

**Possíveis campos categóricos:**

Nenhum campo identificado automaticamente.

**Possíveis campos booleanos:**

Nenhum campo identificado automaticamente.

**Possíveis campos financeiros:**

- `base_rate_per_mile`
- `fuel_surcharge_rate`

**Possíveis campos percentuais ou taxas:**

- `base_rate_per_mile`
- `fuel_surcharge_rate`

**Possíveis métricas de tempo/duração:**

- `typical_transit_days`

**Possíveis campos sensíveis ou pessoais:**

Nenhum campo identificado automaticamente.

**Observações iniciais sobre riscos de privacidade:**

Nenhum campo sensível ou pessoal foi identificado automaticamente pelo nome da coluna.

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

**Tipos de dados identificados pelo pandas:**

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

| Coluna | Valores nulos | Percentual nulo |
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

**Possíveis colunas de identificação:**

- `incident_id`
- `trip_id`
- `truck_id`
- `driver_id`

**Possíveis colunas de data/hora:**

- `incident_date`

**Possíveis campos numéricos:**

- `vehicle_damage_cost`
- `cargo_damage_cost`
- `claim_amount`

**Possíveis campos categóricos:**

Nenhum campo identificado automaticamente.

**Possíveis campos booleanos:**

- `at_fault_flag`
- `injury_flag`
- `preventable_flag`

**Possíveis campos financeiros:**

- `vehicle_damage_cost`
- `cargo_damage_cost`
- `claim_amount`

**Possíveis campos percentuais ou taxas:**

Nenhum campo identificado automaticamente.

**Possíveis métricas de tempo/duração:**

Nenhum campo identificado automaticamente.

**Possíveis campos sensíveis ou pessoais:**

Nenhum campo identificado automaticamente.

**Observações iniciais sobre riscos de privacidade:**

Nenhum campo sensível ou pessoal foi identificado automaticamente pelo nome da coluna.

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

**Tipos de dados identificados pelo pandas:**

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

| Coluna | Valores nulos | Percentual nulo |
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

**Possíveis colunas de identificação:**

- `trailer_id`

**Possíveis colunas de data/hora:**

- `acquisition_date`

**Possíveis campos numéricos:**

- `trailer_number`
- `length_feet`
- `model_year`

**Possíveis campos categóricos:**

Nenhum campo identificado automaticamente.

**Possíveis campos booleanos:**

Nenhum campo identificado automaticamente.

**Possíveis campos financeiros:**

Nenhum campo identificado automaticamente.

**Possíveis campos percentuais ou taxas:**

Nenhum campo identificado automaticamente.

**Possíveis métricas de tempo/duração:**

Nenhum campo identificado automaticamente.

**Possíveis campos sensíveis ou pessoais:**

Nenhum campo identificado automaticamente.

**Observações iniciais sobre riscos de privacidade:**

Nenhum campo sensível ou pessoal foi identificado automaticamente pelo nome da coluna.

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

**Tipos de dados identificados pelo pandas:**

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

| Coluna | Valores nulos | Percentual nulo |
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

**Possíveis colunas de identificação:**

- `trip_id`
- `load_id`
- `driver_id`
- `truck_id`
- `trailer_id`

**Possíveis colunas de data/hora:**

- `dispatch_date`

**Possíveis campos numéricos:**

- `actual_distance_miles`
- `actual_duration_hours`
- `fuel_gallons_used`
- `average_mpg`
- `idle_time_hours`

**Possíveis campos categóricos:**

Nenhum campo identificado automaticamente.

**Possíveis campos booleanos:**

Nenhum campo identificado automaticamente.

**Possíveis campos financeiros:**

Nenhum campo identificado automaticamente.

**Possíveis campos percentuais ou taxas:**

Nenhum campo identificado automaticamente.

**Possíveis métricas de tempo/duração:**

- `actual_duration_hours`
- `idle_time_hours`

**Possíveis campos sensíveis ou pessoais:**

Nenhum campo identificado automaticamente.

**Observações iniciais sobre riscos de privacidade:**

Nenhum campo sensível ou pessoal foi identificado automaticamente pelo nome da coluna.

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

**Tipos de dados identificados pelo pandas:**

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

| Coluna | Valores nulos | Percentual nulo |
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

**Possíveis colunas de identificação:**

- `truck_id`

**Possíveis colunas de data/hora:**

Nenhum campo identificado automaticamente.

**Possíveis campos numéricos:**

- `trips_completed`
- `total_miles`
- `total_revenue`
- `average_mpg`
- `maintenance_events`
- `maintenance_cost`
- `downtime_hours`
- `utilization_rate`

**Possíveis campos categóricos:**

Nenhum campo identificado automaticamente.

**Possíveis campos booleanos:**

Nenhum campo identificado automaticamente.

**Possíveis campos financeiros:**

- `total_revenue`
- `maintenance_cost`

**Possíveis campos percentuais ou taxas:**

- `utilization_rate`

**Possíveis métricas de tempo/duração:**

- `downtime_hours`

**Possíveis campos sensíveis ou pessoais:**

Nenhum campo identificado automaticamente.

**Observações iniciais sobre riscos de privacidade:**

Nenhum campo sensível ou pessoal foi identificado automaticamente pelo nome da coluna.

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

**Tipos de dados identificados pelo pandas:**

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

| Coluna | Valores nulos | Percentual nulo |
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

**Possíveis colunas de identificação:**

- `truck_id`

**Possíveis colunas de data/hora:**

- `acquisition_date`

**Possíveis campos numéricos:**

- `unit_number`
- `model_year`
- `acquisition_mileage`
- `tank_capacity_gallons`

**Possíveis campos categóricos:**

Nenhum campo identificado automaticamente.

**Possíveis campos booleanos:**

Nenhum campo identificado automaticamente.

**Possíveis campos financeiros:**

Nenhum campo identificado automaticamente.

**Possíveis campos percentuais ou taxas:**

Nenhum campo identificado automaticamente.

**Possíveis métricas de tempo/duração:**

Nenhum campo identificado automaticamente.

**Possíveis campos sensíveis ou pessoais:**

Nenhum campo identificado automaticamente.

**Observações iniciais sobre riscos de privacidade:**

Nenhum campo sensível ou pessoal foi identificado automaticamente pelo nome da coluna.

**Amostra controlada de até 3 linhas:**

| truck_id | unit_number | make | model_year | vin | acquisition_date | acquisition_mileage | fuel_type | tank_capacity_gallons | status | home_terminal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TRK00001 | 3463 | Peterbilt | 2016 | 1VV205190335317039 | 2017-04-27 | 18814 | Diesel | 200 | Active | Omaha |
| TRK00002 | 6461 | Kenworth | 2015 | 1NV753749606229960 | 2018-10-04 | 26795 | Diesel | 150 | Active | Seattle |
| TRK00003 | 2335 | Peterbilt | 2018 | 1NT803101860493229 | 2020-09-17 | 11795 | Diesel | 150 | Maintenance | Atlanta |

## Erros de leitura

Nenhum erro de leitura foi registrado.

## Recomendações iniciais do Agente ADA

As recomendações abaixo são hipóteses automáticas preliminares. Elas não são decisões finais e exigem validação humana antes de qualquer tratamento.

### `customers.csv`

- Colunas que provavelmente precisam ser avaliadas para conversão de data/hora: contract_start_date.
- Colunas que provavelmente devem ser tratadas como texto/ID: customer_id.
- Colunas que provavelmente são métricas numéricas: credit_terms_days, annual_revenue_potential.
- Colunas que provavelmente são valores financeiros: annual_revenue_potential.
- Colunas que provavelmente são percentuais ou taxas e exigem validação da escala antes do uso no Power BI: nenhuma identificada automaticamente.
- Colunas que provavelmente são métricas de tempo/duração: credit_terms_days.
- Colunas que exigem atenção por valores ausentes: nenhuma identificada automaticamente.
- Colunas com possível risco de privacidade: customer_name.
- Pontos que exigem validação humana antes de qualquer tratamento: tipos de dados, regras de negócio, tratamento de nulos, duplicidades, campos sensíveis, escala de taxas/percentuais e critérios de uso em relatórios.

### `delivery_events.csv`

- Colunas que provavelmente precisam ser avaliadas para conversão de data/hora: scheduled_datetime, actual_datetime.
- Colunas que provavelmente devem ser tratadas como texto/ID: event_id, load_id, trip_id, facility_id.
- Colunas que provavelmente são métricas numéricas: detention_minutes.
- Colunas que provavelmente são valores financeiros: nenhuma identificada automaticamente.
- Colunas que provavelmente são percentuais ou taxas e exigem validação da escala antes do uso no Power BI: nenhuma identificada automaticamente.
- Colunas que provavelmente são métricas de tempo/duração: detention_minutes.
- Colunas que exigem atenção por valores ausentes: nenhuma identificada automaticamente.
- Colunas com possível risco de privacidade: nenhuma identificada automaticamente.
- Pontos que exigem validação humana antes de qualquer tratamento: tipos de dados, regras de negócio, tratamento de nulos, duplicidades, campos sensíveis, escala de taxas/percentuais e critérios de uso em relatórios.

### `driver_monthly_metrics.csv`

- Colunas que provavelmente precisam ser avaliadas para conversão de data/hora: nenhuma identificada automaticamente.
- Colunas que provavelmente devem ser tratadas como texto/ID: driver_id.
- Colunas que provavelmente são métricas numéricas: trips_completed, total_miles, total_revenue, average_mpg, total_fuel_gallons, on_time_delivery_rate, average_idle_hours.
- Colunas que provavelmente são valores financeiros: total_revenue.
- Colunas que provavelmente são percentuais ou taxas e exigem validação da escala antes do uso no Power BI: on_time_delivery_rate.
- Colunas que provavelmente são métricas de tempo/duração: average_idle_hours.
- Colunas que exigem atenção por valores ausentes: nenhuma identificada automaticamente.
- Colunas com possível risco de privacidade: nenhuma identificada automaticamente.
- Pontos que exigem validação humana antes de qualquer tratamento: tipos de dados, regras de negócio, tratamento de nulos, duplicidades, campos sensíveis, escala de taxas/percentuais e critérios de uso em relatórios.

### `drivers.csv`

- Colunas que provavelmente precisam ser avaliadas para conversão de data/hora: hire_date, termination_date, date_of_birth.
- Colunas que provavelmente devem ser tratadas como texto/ID: driver_id.
- Colunas que provavelmente são métricas numéricas: years_experience.
- Colunas que provavelmente são valores financeiros: nenhuma identificada automaticamente.
- Colunas que provavelmente são percentuais ou taxas e exigem validação da escala antes do uso no Power BI: nenhuma identificada automaticamente.
- Colunas que provavelmente são métricas de tempo/duração: nenhuma identificada automaticamente.
- Colunas que exigem atenção por valores ausentes: termination_date.
- Colunas com possível risco de privacidade: first_name, last_name, license_number, date_of_birth.
- Pontos que exigem validação humana antes de qualquer tratamento: tipos de dados, regras de negócio, tratamento de nulos, duplicidades, campos sensíveis, escala de taxas/percentuais e critérios de uso em relatórios.

### `facilities.csv`

- Colunas que provavelmente precisam ser avaliadas para conversão de data/hora: nenhuma identificada automaticamente.
- Colunas que provavelmente devem ser tratadas como texto/ID: facility_id.
- Colunas que provavelmente são métricas numéricas: latitude, longitude, dock_doors.
- Colunas que provavelmente são valores financeiros: nenhuma identificada automaticamente.
- Colunas que provavelmente são percentuais ou taxas e exigem validação da escala antes do uso no Power BI: nenhuma identificada automaticamente.
- Colunas que provavelmente são métricas de tempo/duração: operating_hours.
- Colunas que exigem atenção por valores ausentes: nenhuma identificada automaticamente.
- Colunas com possível risco de privacidade: nenhuma identificada automaticamente.
- Pontos que exigem validação humana antes de qualquer tratamento: tipos de dados, regras de negócio, tratamento de nulos, duplicidades, campos sensíveis, escala de taxas/percentuais e critérios de uso em relatórios.

### `fuel_purchases.csv`

- Colunas que provavelmente precisam ser avaliadas para conversão de data/hora: purchase_date.
- Colunas que provavelmente devem ser tratadas como texto/ID: fuel_purchase_id, trip_id, truck_id, driver_id.
- Colunas que provavelmente são métricas numéricas: gallons, price_per_gallon, total_cost.
- Colunas que provavelmente são valores financeiros: price_per_gallon, total_cost.
- Colunas que provavelmente são percentuais ou taxas e exigem validação da escala antes do uso no Power BI: nenhuma identificada automaticamente.
- Colunas que provavelmente são métricas de tempo/duração: nenhuma identificada automaticamente.
- Colunas que exigem atenção por valores ausentes: truck_id, driver_id.
- Colunas com possível risco de privacidade: nenhuma identificada automaticamente.
- Pontos que exigem validação humana antes de qualquer tratamento: tipos de dados, regras de negócio, tratamento de nulos, duplicidades, campos sensíveis, escala de taxas/percentuais e critérios de uso em relatórios.

### `loads.csv`

- Colunas que provavelmente precisam ser avaliadas para conversão de data/hora: load_date.
- Colunas que provavelmente devem ser tratadas como texto/ID: load_id, customer_id, route_id.
- Colunas que provavelmente são métricas numéricas: weight_lbs, pieces, revenue, fuel_surcharge, accessorial_charges.
- Colunas que provavelmente são valores financeiros: revenue, fuel_surcharge, accessorial_charges.
- Colunas que provavelmente são percentuais ou taxas e exigem validação da escala antes do uso no Power BI: nenhuma identificada automaticamente.
- Colunas que provavelmente são métricas de tempo/duração: nenhuma identificada automaticamente.
- Colunas que exigem atenção por valores ausentes: nenhuma identificada automaticamente.
- Colunas com possível risco de privacidade: nenhuma identificada automaticamente.
- Pontos que exigem validação humana antes de qualquer tratamento: tipos de dados, regras de negócio, tratamento de nulos, duplicidades, campos sensíveis, escala de taxas/percentuais e critérios de uso em relatórios.

### `maintenance_records.csv`

- Colunas que provavelmente precisam ser avaliadas para conversão de data/hora: maintenance_date.
- Colunas que provavelmente devem ser tratadas como texto/ID: maintenance_id, truck_id.
- Colunas que provavelmente são métricas numéricas: odometer_reading, labor_hours, labor_cost, parts_cost, total_cost, downtime_hours.
- Colunas que provavelmente são valores financeiros: labor_cost, parts_cost, total_cost.
- Colunas que provavelmente são percentuais ou taxas e exigem validação da escala antes do uso no Power BI: nenhuma identificada automaticamente.
- Colunas que provavelmente são métricas de tempo/duração: labor_hours, downtime_hours.
- Colunas que exigem atenção por valores ausentes: nenhuma identificada automaticamente.
- Colunas com possível risco de privacidade: nenhuma identificada automaticamente.
- Pontos que exigem validação humana antes de qualquer tratamento: tipos de dados, regras de negócio, tratamento de nulos, duplicidades, campos sensíveis, escala de taxas/percentuais e critérios de uso em relatórios.

### `routes.csv`

- Colunas que provavelmente precisam ser avaliadas para conversão de data/hora: nenhuma identificada automaticamente.
- Colunas que provavelmente devem ser tratadas como texto/ID: route_id.
- Colunas que provavelmente são métricas numéricas: typical_distance_miles, base_rate_per_mile, fuel_surcharge_rate, typical_transit_days.
- Colunas que provavelmente são valores financeiros: base_rate_per_mile, fuel_surcharge_rate.
- Colunas que provavelmente são percentuais ou taxas e exigem validação da escala antes do uso no Power BI: base_rate_per_mile, fuel_surcharge_rate.
- Colunas que provavelmente são métricas de tempo/duração: typical_transit_days.
- Colunas que exigem atenção por valores ausentes: nenhuma identificada automaticamente.
- Colunas com possível risco de privacidade: nenhuma identificada automaticamente.
- Pontos que exigem validação humana antes de qualquer tratamento: tipos de dados, regras de negócio, tratamento de nulos, duplicidades, campos sensíveis, escala de taxas/percentuais e critérios de uso em relatórios.

### `safety_incidents.csv`

- Colunas que provavelmente precisam ser avaliadas para conversão de data/hora: incident_date.
- Colunas que provavelmente devem ser tratadas como texto/ID: incident_id, trip_id, truck_id, driver_id.
- Colunas que provavelmente são métricas numéricas: vehicle_damage_cost, cargo_damage_cost, claim_amount.
- Colunas que provavelmente são valores financeiros: vehicle_damage_cost, cargo_damage_cost, claim_amount.
- Colunas que provavelmente são percentuais ou taxas e exigem validação da escala antes do uso no Power BI: nenhuma identificada automaticamente.
- Colunas que provavelmente são métricas de tempo/duração: nenhuma identificada automaticamente.
- Colunas que exigem atenção por valores ausentes: truck_id, driver_id.
- Colunas com possível risco de privacidade: nenhuma identificada automaticamente.
- Pontos que exigem validação humana antes de qualquer tratamento: tipos de dados, regras de negócio, tratamento de nulos, duplicidades, campos sensíveis, escala de taxas/percentuais e critérios de uso em relatórios.

### `trailers.csv`

- Colunas que provavelmente precisam ser avaliadas para conversão de data/hora: acquisition_date.
- Colunas que provavelmente devem ser tratadas como texto/ID: trailer_id.
- Colunas que provavelmente são métricas numéricas: trailer_number, length_feet, model_year.
- Colunas que provavelmente são valores financeiros: nenhuma identificada automaticamente.
- Colunas que provavelmente são percentuais ou taxas e exigem validação da escala antes do uso no Power BI: nenhuma identificada automaticamente.
- Colunas que provavelmente são métricas de tempo/duração: nenhuma identificada automaticamente.
- Colunas que exigem atenção por valores ausentes: nenhuma identificada automaticamente.
- Colunas com possível risco de privacidade: nenhuma identificada automaticamente.
- Pontos que exigem validação humana antes de qualquer tratamento: tipos de dados, regras de negócio, tratamento de nulos, duplicidades, campos sensíveis, escala de taxas/percentuais e critérios de uso em relatórios.

### `trips.csv`

- Colunas que provavelmente precisam ser avaliadas para conversão de data/hora: dispatch_date.
- Colunas que provavelmente devem ser tratadas como texto/ID: trip_id, load_id, driver_id, truck_id, trailer_id.
- Colunas que provavelmente são métricas numéricas: actual_distance_miles, actual_duration_hours, fuel_gallons_used, average_mpg, idle_time_hours.
- Colunas que provavelmente são valores financeiros: nenhuma identificada automaticamente.
- Colunas que provavelmente são percentuais ou taxas e exigem validação da escala antes do uso no Power BI: nenhuma identificada automaticamente.
- Colunas que provavelmente são métricas de tempo/duração: actual_duration_hours, idle_time_hours.
- Colunas que exigem atenção por valores ausentes: driver_id, truck_id, trailer_id.
- Colunas com possível risco de privacidade: nenhuma identificada automaticamente.
- Pontos que exigem validação humana antes de qualquer tratamento: tipos de dados, regras de negócio, tratamento de nulos, duplicidades, campos sensíveis, escala de taxas/percentuais e critérios de uso em relatórios.

### `truck_utilization_metrics.csv`

- Colunas que provavelmente precisam ser avaliadas para conversão de data/hora: nenhuma identificada automaticamente.
- Colunas que provavelmente devem ser tratadas como texto/ID: truck_id.
- Colunas que provavelmente são métricas numéricas: trips_completed, total_miles, total_revenue, average_mpg, maintenance_events, maintenance_cost, downtime_hours, utilization_rate.
- Colunas que provavelmente são valores financeiros: total_revenue, maintenance_cost.
- Colunas que provavelmente são percentuais ou taxas e exigem validação da escala antes do uso no Power BI: utilization_rate.
- Colunas que provavelmente são métricas de tempo/duração: downtime_hours.
- Colunas que exigem atenção por valores ausentes: nenhuma identificada automaticamente.
- Colunas com possível risco de privacidade: nenhuma identificada automaticamente.
- Pontos que exigem validação humana antes de qualquer tratamento: tipos de dados, regras de negócio, tratamento de nulos, duplicidades, campos sensíveis, escala de taxas/percentuais e critérios de uso em relatórios.

### `trucks.csv`

- Colunas que provavelmente precisam ser avaliadas para conversão de data/hora: acquisition_date.
- Colunas que provavelmente devem ser tratadas como texto/ID: truck_id.
- Colunas que provavelmente são métricas numéricas: unit_number, model_year, acquisition_mileage, tank_capacity_gallons.
- Colunas que provavelmente são valores financeiros: nenhuma identificada automaticamente.
- Colunas que provavelmente são percentuais ou taxas e exigem validação da escala antes do uso no Power BI: nenhuma identificada automaticamente.
- Colunas que provavelmente são métricas de tempo/duração: nenhuma identificada automaticamente.
- Colunas que exigem atenção por valores ausentes: nenhuma identificada automaticamente.
- Colunas com possível risco de privacidade: nenhuma identificada automaticamente.
- Pontos que exigem validação humana antes de qualquer tratamento: tipos de dados, regras de negócio, tratamento de nulos, duplicidades, campos sensíveis, escala de taxas/percentuais e critérios de uso em relatórios.

## Confirmações de segurança

- Dados brutos não foram alterados.
- Nenhuma transformação foi aplicada.
- Nenhum KPI foi criado.
- Nenhuma conclusão analítica foi tomada.
- Relatório gerado apenas para inspeção inicial.
