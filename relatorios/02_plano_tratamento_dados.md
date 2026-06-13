# Relatório da Etapa 02 — Plano de Tratamento e Padronização dos Dados

Gerado em: 2026-06-13 07:00:52

## 1. Objetivo da etapa

Esta etapa tem como objetivo transformar as evidências da Etapa 01 em um plano de tratamento, sem alterar os dados. O plano organiza propostas, riscos, exemplos e validações necessárias antes de qualquer transformação futura.

Python gera evidências. IA interpreta hipóteses. Humano valida decisões.

## 2. Confirmação de segurança

- Dados brutos não foram alterados.
- Nenhuma transformação foi aplicada.
- Nenhum dado tratado foi criado.
- Nenhum dado final foi criado.
- Nenhum KPI final foi criado.
- Nenhum dashboard foi gerado.
- Este relatório é apenas um plano para validação humana.

## 3. Fontes utilizadas

- Arquivos CSV lidos em `dados/brutos/`: `customers.csv`, `delivery_events.csv`, `driver_monthly_metrics.csv`, `drivers.csv`, `facilities.csv`, `fuel_purchases.csv`, `loads.csv`, `maintenance_records.csv`, `routes.csv`, `safety_incidents.csv`, `trailers.csv`, `trips.csv`, `truck_utilization_metrics.csv`, `trucks.csv`.
- Relatório de referência: `relatorios/01_relatorio_inspecao_dados.md`.
- Status da referência: Relatório encontrado com 1566 linhas e 93863 caracteres.
- Observação: o plano foi criado com base em evidências técnicas, hipóteses interpretativas e validação pendente.

## 4. Escopo preliminar da V1

### 4.1 Tabelas candidatas ao escopo principal da V1

| tabela | papel provável | motivo de entrada na V1 | riscos ou cuidados | validação humana necessária |
| --- | --- | --- | --- | --- |
| loads.csv | possível fato operacional de cargas | base provável para fluxo operacional, relacionamentos e visualizações iniciais | validar granularidade, chaves, nulos e campos sensíveis antes de tratar | Sim |
| trips.csv | possível fato operacional de viagens | base provável para fluxo operacional, relacionamentos e visualizações iniciais | validar granularidade, chaves, nulos e campos sensíveis antes de tratar | Sim |
| delivery_events.csv | possível fato de eventos de coleta/entrega | base provável para fluxo operacional, relacionamentos e visualizações iniciais | validar granularidade, chaves, nulos e campos sensíveis antes de tratar | Sim |
| routes.csv | possível dimensão de rotas | base provável para fluxo operacional, relacionamentos e visualizações iniciais | validar granularidade, chaves, nulos e campos sensíveis antes de tratar | Sim |
| customers.csv | possível dimensão de clientes | base provável para fluxo operacional, relacionamentos e visualizações iniciais | validar granularidade, chaves, nulos e campos sensíveis antes de tratar | Sim |
| fuel_purchases.csv | possível fato/transação de abastecimentos | base provável para fluxo operacional, relacionamentos e visualizações iniciais | validar granularidade, chaves, nulos e campos sensíveis antes de tratar | Sim |
| trucks.csv | possível dimensão de caminhões/frota | base provável para fluxo operacional, relacionamentos e visualizações iniciais | validar granularidade, chaves, nulos e campos sensíveis antes de tratar | Sim |

### 4.2 Tabelas candidatas ao escopo complementar ou futuro

| tabela | motivo para ficar fora do núcleo inicial ou entrar como complementar | riscos | possível uso futuro | validação humana necessária |
| --- | --- | --- | --- | --- |
| drivers.csv | contém dados pessoais/identificáveis de motoristas | exposição de dados pessoais e necessidade de regra LGPD | dimensão de motoristas para análises privadas ou controladas | Sim |
| driver_monthly_metrics.csv | tabela agregada mensal por motorista, fora do núcleo transacional inicial | risco de duplicar ou misturar métricas agregadas com fatos operacionais | análises mensais de desempenho de motoristas, se aprovado | Sim |
| truck_utilization_metrics.csv | tabela agregada mensal por caminhão, fora do núcleo transacional inicial | risco de granularidade entidade + período e agregação incorreta | análises mensais de utilização da frota, se aprovado | Sim |
| maintenance_records.csv | manutenção pode entrar como escopo complementar após estabilizar cargas, viagens e frota | risco de custo/manutenção ser interpretado fora da granularidade correta | análise de manutenção, disponibilidade e custos operacionais | Sim |
| safety_incidents.csv | dados sensíveis de risco operacional e baixa ocorrência | risco de exposição e interpretação estatística frágil por baixa frequência | análise de segurança operacional em fase futura ou restrita | Sim |
| trailers.csv | dimensão complementar de equipamento | risco baixo, mas depende de validação da necessidade no modelo V1 | segmentação por tipo/status de carreta | Sim |
| facilities.csv | dimensão complementar de instalações | risco baixo, mas depende de validação da necessidade geográfica/operacional | análises por instalação, cidade, estado ou tipo de local | Sim |

Nenhuma tabela está sendo excluída nesta etapa. O escopo é apenas uma hipótese para validação humana.

## 5. Plano de tratamento por tabela e coluna

| tabela | coluna | tipo atual identificado | papel técnico provável | problema ou oportunidade | tratamento proposto | exemplo de antes | exemplo de depois | nível de risco | impacto esperado no Power BI | validação humana necessária |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| customers.csv | customer_id | str | ID/chave | risco de conversão indevida para número ou perda de zeros à esquerda | manter como texto e validar chave primária/estrangeira | CUST00001 | CUST00001 | médio | melhora relacionamentos no modelo | Sim |
| customers.csv | customer_name | str | dado comercial confidencial | pode expor informação pessoal, identificável, comercial ou operacional sensível | remover, mascarar ou manter apenas em ambiente privado, conforme aprovação | Metro Wholesale | [removido/mascarado/controlado] | alto | reduz risco de exposição em relatórios e arquivos finais | Sim |
| customers.csv | customer_type | str | categoria/status/código | domínio de valores pode precisar de documentação ou padronização futura | manter como texto; padronizar apenas se inconsistência for comprovada | Dedicated | Dedicated | baixo | melhora filtros, segmentações e rótulos no Power BI | Sim |
| customers.csv | credit_terms_days | int64 | tempo/duração/quantidade temporal | unidade precisa estar documentada | manter numérico; documentar unidade e não converter para data | 60 | 60 | médio | permite medidas de tempo coerentes no Power BI | Sim |
| customers.csv | primary_freight_type | str | categoria/status/código | domínio de valores pode precisar de documentação ou padronização futura | manter como texto; padronizar apenas se inconsistência for comprovada | General | General | baixo | melhora filtros, segmentações e rótulos no Power BI | Sim |
| customers.csv | account_status | str | categoria/status/código | domínio de valores pode precisar de documentação ou padronização futura | manter como texto; padronizar apenas se inconsistência for comprovada | Inactive | Inactive | baixo | melhora filtros, segmentações e rótulos no Power BI | Sim |
| customers.csv | contract_start_date | str | data, data/hora ou período | precisa de formato validado antes da conversão | converter em etapa futura para data/data-hora ou período mensal | 2020-02-20 | data/período padronizado | médio | permite ordenação temporal e filtros corretos no Power BI | Sim |
| customers.csv | annual_revenue_potential | int64 | campo financeiro | moeda, arredondamento e agregação precisam ser validados | manter numérico; formatar como moeda apenas no Power BI | 985117 | 985117 | médio | permite análises financeiras sem arredondamento prematuro | Sim |
| delivery_events.csv | event_id | str | ID/chave | risco de conversão indevida para número ou perda de zeros à esquerda | manter como texto e validar chave primária/estrangeira | EVT00000001 | EVT00000001 | médio | melhora relacionamentos no modelo | Sim |
| delivery_events.csv | load_id | str | ID/chave | risco de conversão indevida para número ou perda de zeros à esquerda | manter como texto e validar chave primária/estrangeira | LOAD00000001 | LOAD00000001 | médio | melhora relacionamentos no modelo | Sim |
| delivery_events.csv | trip_id | str | ID/chave | risco de conversão indevida para número ou perda de zeros à esquerda | manter como texto e validar chave primária/estrangeira | TRIP00000001 | TRIP00000001 | médio | melhora relacionamentos no modelo | Sim |
| delivery_events.csv | event_type | str | categoria/status/código | domínio de valores pode precisar de documentação ou padronização futura | manter como texto; padronizar apenas se inconsistência for comprovada | Pickup | Pickup | baixo | melhora filtros, segmentações e rótulos no Power BI | Sim |
| delivery_events.csv | facility_id | str | ID/chave | risco de conversão indevida para número ou perda de zeros à esquerda | manter como texto e validar chave primária/estrangeira | FAC00034 | FAC00034 | médio | melhora relacionamentos no modelo | Sim |
| delivery_events.csv | scheduled_datetime | str | data, data/hora ou período | precisa de formato validado antes da conversão | converter em etapa futura para data/data-hora ou período mensal | 2022-01-01 18:00:00.000000 | data/período padronizado | médio | permite ordenação temporal e filtros corretos no Power BI | Sim |
| delivery_events.csv | actual_datetime | str | data, data/hora ou período | precisa de formato validado antes da conversão | converter em etapa futura para data/data-hora ou período mensal | 2022-01-01 20:58:55.918185 | data/período padronizado | médio | permite ordenação temporal e filtros corretos no Power BI | Sim |
| delivery_events.csv | detention_minutes | int64 | tempo/duração/quantidade temporal | unidade precisa estar documentada | manter numérico; documentar unidade e não converter para data | 0 | 0 | médio | permite medidas de tempo coerentes no Power BI | Sim |
| delivery_events.csv | on_time_flag | bool | booleano/flag operacional | não deve ser tratado como métrica numérica principal | manter como booleano; criar descrição amigável apenas se aprovado | False | False | baixo | permite filtros e cálculo de taxas com regra documentada | Sim |
| delivery_events.csv | location_city | str | categoria/status/código | domínio de valores pode precisar de documentação ou padronização futura | manter como texto; padronizar apenas se inconsistência for comprovada | Houston | Houston | baixo | melhora filtros, segmentações e rótulos no Power BI | Sim |
| delivery_events.csv | location_state | str | categoria/status/código | domínio de valores pode precisar de documentação ou padronização futura | manter como texto; padronizar apenas se inconsistência for comprovada | TX | TX | baixo | melhora filtros, segmentações e rótulos no Power BI | Sim |
| driver_monthly_metrics.csv | driver_id | str | ID/chave | risco de conversão indevida para número ou perda de zeros à esquerda | manter como texto e validar chave primária/estrangeira | DRV00001 | DRV00001 | médio | melhora relacionamentos no modelo | Sim |
| driver_monthly_metrics.csv | month | str | data, data/hora ou período | precisa de formato validado antes da conversão | converter em etapa futura para data/data-hora ou período mensal | 2022-01-01 | data/período padronizado | médio | permite ordenação temporal e filtros corretos no Power BI | Sim |
| driver_monthly_metrics.csv | trips_completed | int64 | ambíguo / exige validação humana | evidência insuficiente para definir tratamento automático | não aplicar tratamento antes de validação humana | 26 | 26 | médio | evita tratamento indevido por inferência fraca | Sim |
| driver_monthly_metrics.csv | total_miles | int64 | ambíguo / exige validação humana | evidência insuficiente para definir tratamento automático | não aplicar tratamento antes de validação humana | 36620 | 36620 | médio | evita tratamento indevido por inferência fraca | Sim |
| driver_monthly_metrics.csv | total_revenue | float64 | campo financeiro | moeda, arredondamento e agregação precisam ser validados | manter numérico; formatar como moeda apenas no Power BI | 79141.59 | 79141.59 | médio | permite análises financeiras sem arredondamento prematuro | Sim |
| driver_monthly_metrics.csv | average_mpg | float64 | ambíguo / exige validação humana | evidência insuficiente para definir tratamento automático | não aplicar tratamento antes de validação humana | 6.61 | 6.61 | médio | evita tratamento indevido por inferência fraca | Sim |
| driver_monthly_metrics.csv | total_fuel_gallons | float64 | métrica numérica operacional: volume total de combustível | unidade e regra de agregação precisam ser documentadas | manter numérico; documentar unidade em galões | 5574.7 | 5574.7 | médio | permite medidas operacionais mais claras no Power BI | Sim |
| driver_monthly_metrics.csv | on_time_delivery_rate | float64 | percentual/taxa/índice | escala precisa ser validada antes de formatar como percentual | validar escala; não multiplicar por 100 sem aprovação | 0.385 | 0.385 | alto | evita percentuais incorretos no Power BI | Sim |
| driver_monthly_metrics.csv | average_idle_hours | float64 | tempo/duração/quantidade temporal | unidade precisa estar documentada | manter numérico; documentar unidade e não converter para data | 8.2 | 8.2 | médio | permite medidas de tempo coerentes no Power BI | Sim |
| drivers.csv | driver_id | str | ID/chave | risco de conversão indevida para número ou perda de zeros à esquerda | manter como texto e validar chave primária/estrangeira | DRV00001 | DRV00001 | médio | melhora relacionamentos no modelo | Sim |
| drivers.csv | first_name | str | dado pessoal | pode expor informação pessoal, identificável, comercial ou operacional sensível | remover, mascarar ou manter apenas em ambiente privado, conforme aprovação | Jennifer | [removido/mascarado/controlado] | alto | reduz risco de exposição em relatórios e arquivos finais | Sim |
| drivers.csv | last_name | str | dado pessoal | pode expor informação pessoal, identificável, comercial ou operacional sensível | remover, mascarar ou manter apenas em ambiente privado, conforme aprovação | Hernandez | [removido/mascarado/controlado] | alto | reduz risco de exposição em relatórios e arquivos finais | Sim |
| drivers.csv | hire_date | str | data, data/hora ou período | precisa de formato validado antes da conversão | converter em etapa futura para data/data-hora ou período mensal | 2014-10-31 | data/período padronizado | médio | permite ordenação temporal e filtros corretos no Power BI | Sim |
| drivers.csv | termination_date | str | data, data/hora ou período | precisa de formato validado antes da conversão | converter em etapa futura para data/data-hora ou período mensal | 2021-05-17 | data/período padronizado | médio | permite ordenação temporal e filtros corretos no Power BI | Sim |
| drivers.csv | license_number | str | dado pessoal/identificável | pode expor informação pessoal, identificável, comercial ou operacional sensível | remover, mascarar ou manter apenas em ambiente privado, conforme aprovação | DL673510887 | [removido/mascarado/controlado] | alto | reduz risco de exposição em relatórios e arquivos finais | Sim |
| drivers.csv | license_state | str | categoria/status/código | domínio de valores pode precisar de documentação ou padronização futura | manter como texto; padronizar apenas se inconsistência for comprovada | WA | WA | baixo | melhora filtros, segmentações e rótulos no Power BI | Sim |
| drivers.csv | date_of_birth | str | dado pessoal | pode expor informação pessoal, identificável, comercial ou operacional sensível | remover, mascarar ou manter apenas em ambiente privado, conforme aprovação | 1973-11-07 | [removido/mascarado/controlado] | alto | reduz risco de exposição em relatórios e arquivos finais | Sim |
| drivers.csv | home_terminal | str | categoria/status/código | domínio de valores pode precisar de documentação ou padronização futura | manter como texto; padronizar apenas se inconsistência for comprovada | Denver | Denver | baixo | melhora filtros, segmentações e rótulos no Power BI | Sim |
| drivers.csv | employment_status | str | categoria/status/código | domínio de valores pode precisar de documentação ou padronização futura | manter como texto; padronizar apenas se inconsistência for comprovada | Active | Active | baixo | melhora filtros, segmentações e rótulos no Power BI | Sim |
| drivers.csv | cdl_class | str | categoria/status/código | domínio de valores pode precisar de documentação ou padronização futura | manter como texto; padronizar apenas se inconsistência for comprovada | A | A | baixo | melhora filtros, segmentações e rótulos no Power BI | Sim |
| drivers.csv | years_experience | int64 | tempo/duração/quantidade temporal | unidade precisa estar documentada | manter numérico; documentar unidade e não converter para data | 3 | 3 | médio | permite medidas de tempo coerentes no Power BI | Sim |
| facilities.csv | facility_id | str | ID/chave | risco de conversão indevida para número ou perda de zeros à esquerda | manter como texto e validar chave primária/estrangeira | FAC00001 | FAC00001 | médio | melhora relacionamentos no modelo | Sim |
| facilities.csv | facility_name | str | ambíguo / exige validação humana | evidência insuficiente para definir tratamento automático | não aplicar tratamento antes de validação humana | Houston Distribution Center | Houston Distribution Center | médio | evita tratamento indevido por inferência fraca | Sim |
| facilities.csv | facility_type | str | categoria/status/código | domínio de valores pode precisar de documentação ou padronização futura | manter como texto; padronizar apenas se inconsistência for comprovada | Cross-Dock | Cross-Dock | baixo | melhora filtros, segmentações e rótulos no Power BI | Sim |
| facilities.csv | city | str | categoria/status/código | domínio de valores pode precisar de documentação ou padronização futura | manter como texto; padronizar apenas se inconsistência for comprovada | Houston | Houston | baixo | melhora filtros, segmentações e rótulos no Power BI | Sim |
| facilities.csv | state | str | categoria/status/código | domínio de valores pode precisar de documentação ou padronização futura | manter como texto; padronizar apenas se inconsistência for comprovada | TX | TX | baixo | melhora filtros, segmentações e rótulos no Power BI | Sim |
| facilities.csv | latitude | float64 | ambíguo / exige validação humana | evidência insuficiente para definir tratamento automático | não aplicar tratamento antes de validação humana | 29.7604 | 29.7604 | médio | evita tratamento indevido por inferência fraca | Sim |
| facilities.csv | longitude | float64 | ambíguo / exige validação humana | evidência insuficiente para definir tratamento automático | não aplicar tratamento antes de validação humana | -95.3698 | -95.3698 | médio | evita tratamento indevido por inferência fraca | Sim |
| facilities.csv | dock_doors | int64 | métrica numérica operacional: quantidade/capacidade operacional | unidade e regra de agregação precisam ser documentadas | manter numérico; validar se representa capacidade | 125 | 125 | médio | permite medidas operacionais mais claras no Power BI | Sim |
| facilities.csv | operating_hours | str | texto/categoria/faixa operacional de horário | representa faixa de funcionamento, não métrica numérica de duração | manter como texto; padronizar valores apenas se houver inconsistência comprovada | 24/7 | 24/7 | baixo | melhora filtros e descrições operacionais no Power BI | Sim |
| fuel_purchases.csv | fuel_purchase_id | str | ID/chave | risco de conversão indevida para número ou perda de zeros à esquerda | manter como texto e validar chave primária/estrangeira | FUEL00000001 | FUEL00000001 | médio | melhora relacionamentos no modelo | Sim |
| fuel_purchases.csv | trip_id | str | ID/chave | risco de conversão indevida para número ou perda de zeros à esquerda | manter como texto e validar chave primária/estrangeira | TRIP00051284 | TRIP00051284 | médio | melhora relacionamentos no modelo | Sim |
| fuel_purchases.csv | truck_id | str | ID/chave | risco de conversão indevida para número ou perda de zeros à esquerda | manter como texto e validar chave primária/estrangeira | TRK00045 | TRK00045 | médio | melhora relacionamentos no modelo | Sim |
| fuel_purchases.csv | driver_id | str | ID/chave | risco de conversão indevida para número ou perda de zeros à esquerda | manter como texto e validar chave primária/estrangeira | DRV00102 | DRV00102 | médio | melhora relacionamentos no modelo | Sim |
| fuel_purchases.csv | purchase_date | str | data, data/hora ou período | precisa de formato validado antes da conversão | converter em etapa futura para data/data-hora ou período mensal | 2023-10-22 05:00:00 | data/período padronizado | médio | permite ordenação temporal e filtros corretos no Power BI | Sim |
| fuel_purchases.csv | location_city | str | categoria/status/código | domínio de valores pode precisar de documentação ou padronização futura | manter como texto; padronizar apenas se inconsistência for comprovada | Columbus | Columbus | baixo | melhora filtros, segmentações e rótulos no Power BI | Sim |
| fuel_purchases.csv | location_state | str | categoria/status/código | domínio de valores pode precisar de documentação ou padronização futura | manter como texto; padronizar apenas se inconsistência for comprovada | MN | MN | baixo | melhora filtros, segmentações e rótulos no Power BI | Sim |
| fuel_purchases.csv | gallons | float64 | métrica numérica operacional: volume de combustível | unidade e regra de agregação precisam ser documentadas | manter numérico; documentar unidade em galões | 131.6 | 131.6 | médio | permite medidas operacionais mais claras no Power BI | Sim |
| fuel_purchases.csv | price_per_gallon | float64 | taxa monetária por unidade/preço unitário | não deve ser somado diretamente | manter numérico e definir agregação futura, preferencialmente média ponderada | 3.399 | 3.399 | alto | evita distorção de valores unitários no Power BI | Sim |
| fuel_purchases.csv | total_cost | float64 | campo financeiro | moeda, arredondamento e agregação precisam ser validados | manter numérico; formatar como moeda apenas no Power BI | 447.31 | 447.31 | médio | permite análises financeiras sem arredondamento prematuro | Sim |
| fuel_purchases.csv | fuel_card_number | str | identificador operacional confidencial | pode expor informação pessoal, identificável, comercial ou operacional sensível | remover, mascarar ou manter apenas em ambiente privado, conforme aprovação | FC567161 | [removido/mascarado/controlado] | alto | reduz risco de exposição em relatórios e arquivos finais | Sim |
| loads.csv | load_id | str | ID/chave | risco de conversão indevida para número ou perda de zeros à esquerda | manter como texto e validar chave primária/estrangeira | LOAD00000001 | LOAD00000001 | médio | melhora relacionamentos no modelo | Sim |
| loads.csv | customer_id | str | ID/chave | risco de conversão indevida para número ou perda de zeros à esquerda | manter como texto e validar chave primária/estrangeira | CUST00183 | CUST00183 | médio | melhora relacionamentos no modelo | Sim |
| loads.csv | route_id | str | ID/chave | risco de conversão indevida para número ou perda de zeros à esquerda | manter como texto e validar chave primária/estrangeira | RTE00019 | RTE00019 | médio | melhora relacionamentos no modelo | Sim |
| loads.csv | load_date | str | data, data/hora ou período | precisa de formato validado antes da conversão | converter em etapa futura para data/data-hora ou período mensal | 2022-01-01 | data/período padronizado | médio | permite ordenação temporal e filtros corretos no Power BI | Sim |
| loads.csv | load_type | str | categoria/status/código | domínio de valores pode precisar de documentação ou padronização futura | manter como texto; padronizar apenas se inconsistência for comprovada | Dry Van | Dry Van | baixo | melhora filtros, segmentações e rótulos no Power BI | Sim |
| loads.csv | weight_lbs | int64 | métrica numérica operacional: peso | unidade e regra de agregação precisam ser documentadas | manter numérico; documentar unidade em libras | 19178 | 19178 | médio | permite medidas operacionais mais claras no Power BI | Sim |
| loads.csv | pieces | int64 | métrica numérica operacional: quantidade/contagem | unidade e regra de agregação precisam ser documentadas | manter numérico; validar se representa peças transportadas | 13 | 13 | médio | permite medidas operacionais mais claras no Power BI | Sim |
| loads.csv | revenue | float64 | campo financeiro | moeda, arredondamento e agregação precisam ser validados | manter numérico; formatar como moeda apenas no Power BI | 3045.23 | 3045.23 | médio | permite análises financeiras sem arredondamento prematuro | Sim |
| loads.csv | fuel_surcharge | float64 | campo financeiro | moeda, arredondamento e agregação precisam ser validados | manter numérico; formatar como moeda apenas no Power BI | 406.72 | 406.72 | médio | permite análises financeiras sem arredondamento prematuro | Sim |
| loads.csv | accessorial_charges | int64 | campo financeiro | moeda, arredondamento e agregação precisam ser validados | manter numérico; formatar como moeda apenas no Power BI | 100 | 100 | médio | permite análises financeiras sem arredondamento prematuro | Sim |
| loads.csv | load_status | str | categoria/status/código | domínio de valores pode precisar de documentação ou padronização futura | manter como texto; padronizar apenas se inconsistência for comprovada | Completed | Completed | baixo | melhora filtros, segmentações e rótulos no Power BI | Sim |
| loads.csv | booking_type | str | categoria/status/código | domínio de valores pode precisar de documentação ou padronização futura | manter como texto; padronizar apenas se inconsistência for comprovada | Spot | Spot | baixo | melhora filtros, segmentações e rótulos no Power BI | Sim |
| maintenance_records.csv | maintenance_id | str | ID/chave | risco de conversão indevida para número ou perda de zeros à esquerda | manter como texto e validar chave primária/estrangeira | MAINT00000001 | MAINT00000001 | médio | melhora relacionamentos no modelo | Sim |
| maintenance_records.csv | truck_id | str | ID/chave | risco de conversão indevida para número ou perda de zeros à esquerda | manter como texto e validar chave primária/estrangeira | TRK00085 | TRK00085 | médio | melhora relacionamentos no modelo | Sim |
| maintenance_records.csv | maintenance_date | str | data, data/hora ou período | precisa de formato validado antes da conversão | converter em etapa futura para data/data-hora ou período mensal | 2022-01-01 | data/período padronizado | médio | permite ordenação temporal e filtros corretos no Power BI | Sim |
| maintenance_records.csv | maintenance_type | str | categoria/status/código | domínio de valores pode precisar de documentação ou padronização futura | manter como texto; padronizar apenas se inconsistência for comprovada | Inspection | Inspection | baixo | melhora filtros, segmentações e rótulos no Power BI | Sim |
| maintenance_records.csv | odometer_reading | int64 | métrica numérica operacional: leitura de odômetro | unidade e regra de agregação precisam ser documentadas | manter numérico; documentar unidade | 400255 | 400255 | médio | permite medidas operacionais mais claras no Power BI | Sim |
| maintenance_records.csv | labor_hours | float64 | tempo/duração/quantidade temporal | unidade precisa estar documentada | manter numérico; documentar unidade e não converter para data | 7.8 | 7.8 | médio | permite medidas de tempo coerentes no Power BI | Sim |
| maintenance_records.csv | labor_cost | float64 | campo financeiro | moeda, arredondamento e agregação precisam ser validados | manter numérico; formatar como moeda apenas no Power BI | 781.42 | 781.42 | médio | permite análises financeiras sem arredondamento prematuro | Sim |
| maintenance_records.csv | parts_cost | float64 | campo financeiro | moeda, arredondamento e agregação precisam ser validados | manter numérico; formatar como moeda apenas no Power BI | 10.41 | 10.41 | médio | permite análises financeiras sem arredondamento prematuro | Sim |
| maintenance_records.csv | total_cost | float64 | campo financeiro | moeda, arredondamento e agregação precisam ser validados | manter numérico; formatar como moeda apenas no Power BI | 791.83 | 791.83 | médio | permite análises financeiras sem arredondamento prematuro | Sim |
| maintenance_records.csv | facility_location | str | categoria/status/código | domínio de valores pode precisar de documentação ou padronização futura | manter como texto; padronizar apenas se inconsistência for comprovada | Kansas City | Kansas City | baixo | melhora filtros, segmentações e rótulos no Power BI | Sim |
| maintenance_records.csv | downtime_hours | float64 | tempo/duração/quantidade temporal | unidade precisa estar documentada | manter numérico; documentar unidade e não converter para data | 22.2 | 22.2 | médio | permite medidas de tempo coerentes no Power BI | Sim |
| maintenance_records.csv | service_description | str | texto livre com possível risco | pode expor informação pessoal, identificável, comercial ou operacional sensível | remover, mascarar ou manter apenas em ambiente privado, conforme aprovação | Emergency Inspection | [removido/mascarado/controlado] | alto | reduz risco de exposição em relatórios e arquivos finais | Sim |
| routes.csv | route_id | str | ID/chave | risco de conversão indevida para número ou perda de zeros à esquerda | manter como texto e validar chave primária/estrangeira | RTE00001 | RTE00001 | médio | melhora relacionamentos no modelo | Sim |
| routes.csv | origin_city | str | categoria/status/código | domínio de valores pode precisar de documentação ou padronização futura | manter como texto; padronizar apenas se inconsistência for comprovada | Atlanta | Atlanta | baixo | melhora filtros, segmentações e rótulos no Power BI | Sim |
| routes.csv | origin_state | str | categoria/status/código | domínio de valores pode precisar de documentação ou padronização futura | manter como texto; padronizar apenas se inconsistência for comprovada | GA | GA | baixo | melhora filtros, segmentações e rótulos no Power BI | Sim |
| routes.csv | destination_city | str | categoria/status/código | domínio de valores pode precisar de documentação ou padronização futura | manter como texto; padronizar apenas se inconsistência for comprovada | Chicago | Chicago | baixo | melhora filtros, segmentações e rótulos no Power BI | Sim |
| routes.csv | destination_state | str | categoria/status/código | domínio de valores pode precisar de documentação ou padronização futura | manter como texto; padronizar apenas se inconsistência for comprovada | IL | IL | baixo | melhora filtros, segmentações e rótulos no Power BI | Sim |
| routes.csv | typical_distance_miles | int64 | métrica numérica operacional: distância padrão | unidade e regra de agregação precisam ser documentadas | manter numérico; documentar unidade em milhas | 677 | 677 | médio | permite medidas operacionais mais claras no Power BI | Sim |
| routes.csv | base_rate_per_mile | float64 | taxa monetária por unidade/preço unitário | não deve ser somado diretamente | manter numérico e definir agregação futura, preferencialmente média ponderada | 1.7 | 1.7 | alto | evita distorção de valores unitários no Power BI | Sim |
| routes.csv | fuel_surcharge_rate | float64 | percentual/taxa/índice | escala precisa ser validada antes de formatar como percentual | validar escala; não multiplicar por 100 sem aprovação | 0.19 | 0.19 | alto | evita percentuais incorretos no Power BI | Sim |
| routes.csv | typical_transit_days | int64 | tempo/duração/quantidade temporal | unidade precisa estar documentada | manter numérico; documentar unidade e não converter para data | 1 | 1 | médio | permite medidas de tempo coerentes no Power BI | Sim |
| safety_incidents.csv | incident_id | str | ID/chave | risco de conversão indevida para número ou perda de zeros à esquerda | manter como texto e validar chave primária/estrangeira | INC00000001 | INC00000001 | médio | melhora relacionamentos no modelo | Sim |
| safety_incidents.csv | trip_id | str | ID/chave | risco de conversão indevida para número ou perda de zeros à esquerda | manter como texto e validar chave primária/estrangeira | TRIP00036079 | TRIP00036079 | médio | melhora relacionamentos no modelo | Sim |
| safety_incidents.csv | truck_id | str | ID/chave | risco de conversão indevida para número ou perda de zeros à esquerda | manter como texto e validar chave primária/estrangeira | TRK00006 | TRK00006 | médio | melhora relacionamentos no modelo | Sim |
| safety_incidents.csv | driver_id | str | ID/chave | risco de conversão indevida para número ou perda de zeros à esquerda | manter como texto e validar chave primária/estrangeira | DRV00006 | DRV00006 | médio | melhora relacionamentos no modelo | Sim |
| safety_incidents.csv | incident_date | str | data, data/hora ou período | precisa de formato validado antes da conversão | converter em etapa futura para data/data-hora ou período mensal | 2023-04-09 14:00:00 | data/período padronizado | médio | permite ordenação temporal e filtros corretos no Power BI | Sim |
| safety_incidents.csv | incident_type | str | categoria/status/código | domínio de valores pode precisar de documentação ou padronização futura | manter como texto; padronizar apenas se inconsistência for comprovada | Moving Violation | Moving Violation | baixo | melhora filtros, segmentações e rótulos no Power BI | Sim |
| safety_incidents.csv | location_city | str | categoria/status/código | domínio de valores pode precisar de documentação ou padronização futura | manter como texto; padronizar apenas se inconsistência for comprovada | Columbus | Columbus | baixo | melhora filtros, segmentações e rótulos no Power BI | Sim |
| safety_incidents.csv | location_state | str | categoria/status/código | domínio de valores pode precisar de documentação ou padronização futura | manter como texto; padronizar apenas se inconsistência for comprovada | PA | PA | baixo | melhora filtros, segmentações e rótulos no Power BI | Sim |
| safety_incidents.csv | at_fault_flag | bool | booleano/flag operacional | não deve ser tratado como métrica numérica principal | manter como booleano; criar descrição amigável apenas se aprovado | True | True | baixo | permite filtros e cálculo de taxas com regra documentada | Sim |
| safety_incidents.csv | injury_flag | bool | booleano/flag operacional | não deve ser tratado como métrica numérica principal | manter como booleano; criar descrição amigável apenas se aprovado | False | False | baixo | permite filtros e cálculo de taxas com regra documentada | Sim |
| safety_incidents.csv | vehicle_damage_cost | float64 | campo financeiro | moeda, arredondamento e agregação precisam ser validados | manter numérico; formatar como moeda apenas no Power BI | 12629.26 | 12629.26 | médio | permite análises financeiras sem arredondamento prematuro | Sim |
| safety_incidents.csv | cargo_damage_cost | float64 | campo financeiro | moeda, arredondamento e agregação precisam ser validados | manter numérico; formatar como moeda apenas no Power BI | 0.0 | 0.0 | médio | permite análises financeiras sem arredondamento prematuro | Sim |
| safety_incidents.csv | claim_amount | float64 | campo financeiro | moeda, arredondamento e agregação precisam ser validados | manter numérico; formatar como moeda apenas no Power BI | 12629.26 | 12629.26 | médio | permite análises financeiras sem arredondamento prematuro | Sim |
| safety_incidents.csv | preventable_flag | bool | booleano/flag operacional | não deve ser tratado como métrica numérica principal | manter como booleano; criar descrição amigável apenas se aprovado | True | True | baixo | permite filtros e cálculo de taxas com regra documentada | Sim |
| safety_incidents.csv | description | str | texto livre com possível risco | pode expor informação pessoal, identificável, comercial ou operacional sensível | remover, mascarar ou manter apenas em ambiente privado, conforme aprovação | Severe incident involving equipment | [removido/mascarado/controlado] | alto | reduz risco de exposição em relatórios e arquivos finais | Sim |
| trailers.csv | trailer_id | str | ID/chave | risco de conversão indevida para número ou perda de zeros à esquerda | manter como texto e validar chave primária/estrangeira | TRL00001 | TRL00001 | médio | melhora relacionamentos no modelo | Sim |
| trailers.csv | trailer_number | int64 | código/número operacional | não deve ser tratado como métrica, mesmo quando armazenado como número | manter como texto/código operacional; validar uso em filtros ou identificação | 4290 | 4290 | médio | evita soma, média ou ordenação numérica indevida no Power BI | Sim |
| trailers.csv | trailer_type | str | categoria/status/código | domínio de valores pode precisar de documentação ou padronização futura | manter como texto; padronizar apenas se inconsistência for comprovada | Refrigerated | Refrigerated | baixo | melhora filtros, segmentações e rótulos no Power BI | Sim |
| trailers.csv | length_feet | int64 | métrica numérica operacional: comprimento | unidade e regra de agregação precisam ser documentadas | manter numérico; documentar unidade em pés | 53 | 53 | médio | permite medidas operacionais mais claras no Power BI | Sim |
| trailers.csv | model_year | int64 | ano/modelo, atributo temporal | não deve ser tratado como quantidade operacional | manter como ano/atributo; validar formato e uso como segmentação | 2016 | 2016 | baixo | permite análise por ano de modelo sem somas indevidas | Sim |
| trailers.csv | vin | str | identificador operacional confidencial | pode expor informação pessoal, identificável, comercial ou operacional sensível | remover, mascarar ou manter apenas em ambiente privado, conforme aprovação | 1AV889081755621178 | [removido/mascarado/controlado] | alto | reduz risco de exposição em relatórios e arquivos finais | Sim |
| trailers.csv | acquisition_date | str | data, data/hora ou período | precisa de formato validado antes da conversão | converter em etapa futura para data/data-hora ou período mensal | 2018-05-11 | data/período padronizado | médio | permite ordenação temporal e filtros corretos no Power BI | Sim |
| trailers.csv | status | str | categoria/status/código | domínio de valores pode precisar de documentação ou padronização futura | manter como texto; padronizar apenas se inconsistência for comprovada | Active | Active | baixo | melhora filtros, segmentações e rótulos no Power BI | Sim |
| trailers.csv | current_location | str | categoria/status/código | domínio de valores pode precisar de documentação ou padronização futura | manter como texto; padronizar apenas se inconsistência for comprovada | Kansas City | Kansas City | baixo | melhora filtros, segmentações e rótulos no Power BI | Sim |
| trips.csv | trip_id | str | ID/chave | risco de conversão indevida para número ou perda de zeros à esquerda | manter como texto e validar chave primária/estrangeira | TRIP00000001 | TRIP00000001 | médio | melhora relacionamentos no modelo | Sim |
| trips.csv | load_id | str | ID/chave | risco de conversão indevida para número ou perda de zeros à esquerda | manter como texto e validar chave primária/estrangeira | LOAD00000001 | LOAD00000001 | médio | melhora relacionamentos no modelo | Sim |
| trips.csv | driver_id | str | ID/chave | risco de conversão indevida para número ou perda de zeros à esquerda | manter como texto e validar chave primária/estrangeira | DRV00117 | DRV00117 | médio | melhora relacionamentos no modelo | Sim |
| trips.csv | truck_id | str | ID/chave | risco de conversão indevida para número ou perda de zeros à esquerda | manter como texto e validar chave primária/estrangeira | TRK00035 | TRK00035 | médio | melhora relacionamentos no modelo | Sim |
| trips.csv | trailer_id | str | ID/chave | risco de conversão indevida para número ou perda de zeros à esquerda | manter como texto e validar chave primária/estrangeira | TRL00167 | TRL00167 | médio | melhora relacionamentos no modelo | Sim |
| trips.csv | dispatch_date | str | data, data/hora ou período | precisa de formato validado antes da conversão | converter em etapa futura para data/data-hora ou período mensal | 2022-01-01 | data/período padronizado | médio | permite ordenação temporal e filtros corretos no Power BI | Sim |
| trips.csv | actual_distance_miles | int64 | métrica numérica operacional: distância | unidade e regra de agregação precisam ser documentadas | manter numérico; documentar unidade em milhas | 1314 | 1314 | médio | permite medidas operacionais mais claras no Power BI | Sim |
| trips.csv | actual_duration_hours | float64 | tempo/duração/quantidade temporal | unidade precisa estar documentada | manter numérico; documentar unidade e não converter para data | 26.2 | 26.2 | médio | permite medidas de tempo coerentes no Power BI | Sim |
| trips.csv | fuel_gallons_used | float64 | métrica numérica operacional: volume de combustível | unidade e regra de agregação precisam ser documentadas | manter numérico; documentar unidade em galões | 183.8 | 183.8 | médio | permite medidas operacionais mais claras no Power BI | Sim |
| trips.csv | average_mpg | float64 | ambíguo / exige validação humana | evidência insuficiente para definir tratamento automático | não aplicar tratamento antes de validação humana | 7.15 | 7.15 | médio | evita tratamento indevido por inferência fraca | Sim |
| trips.csv | idle_time_hours | float64 | tempo/duração/quantidade temporal | unidade precisa estar documentada | manter numérico; documentar unidade e não converter para data | 3.5 | 3.5 | médio | permite medidas de tempo coerentes no Power BI | Sim |
| trips.csv | trip_status | str | categoria/status/código | domínio de valores pode precisar de documentação ou padronização futura | manter como texto; padronizar apenas se inconsistência for comprovada | Completed | Completed | baixo | melhora filtros, segmentações e rótulos no Power BI | Sim |
| truck_utilization_metrics.csv | truck_id | str | ID/chave | risco de conversão indevida para número ou perda de zeros à esquerda | manter como texto e validar chave primária/estrangeira | TRK00001 | TRK00001 | médio | melhora relacionamentos no modelo | Sim |
| truck_utilization_metrics.csv | month | str | data, data/hora ou período | precisa de formato validado antes da conversão | converter em etapa futura para data/data-hora ou período mensal | 2022-01-01 | data/período padronizado | médio | permite ordenação temporal e filtros corretos no Power BI | Sim |
| truck_utilization_metrics.csv | trips_completed | int64 | ambíguo / exige validação humana | evidência insuficiente para definir tratamento automático | não aplicar tratamento antes de validação humana | 22 | 22 | médio | evita tratamento indevido por inferência fraca | Sim |
| truck_utilization_metrics.csv | total_miles | int64 | ambíguo / exige validação humana | evidência insuficiente para definir tratamento automático | não aplicar tratamento antes de validação humana | 39269 | 39269 | médio | evita tratamento indevido por inferência fraca | Sim |
| truck_utilization_metrics.csv | total_revenue | float64 | campo financeiro | moeda, arredondamento e agregação precisam ser validados | manter numérico; formatar como moeda apenas no Power BI | 84792.02 | 84792.02 | médio | permite análises financeiras sem arredondamento prematuro | Sim |
| truck_utilization_metrics.csv | average_mpg | float64 | ambíguo / exige validação humana | evidência insuficiente para definir tratamento automático | não aplicar tratamento antes de validação humana | 6.78 | 6.78 | médio | evita tratamento indevido por inferência fraca | Sim |
| truck_utilization_metrics.csv | maintenance_events | int64 | ambíguo / exige validação humana | evidência insuficiente para definir tratamento automático | não aplicar tratamento antes de validação humana | 2 | 2 | médio | evita tratamento indevido por inferência fraca | Sim |
| truck_utilization_metrics.csv | maintenance_cost | float64 | campo financeiro | moeda, arredondamento e agregação precisam ser validados | manter numérico; formatar como moeda apenas no Power BI | 4380.98 | 4380.98 | médio | permite análises financeiras sem arredondamento prematuro | Sim |
| truck_utilization_metrics.csv | downtime_hours | float64 | tempo/duração/quantidade temporal | unidade precisa estar documentada | manter numérico; documentar unidade e não converter para data | 63.1 | 63.1 | médio | permite medidas de tempo coerentes no Power BI | Sim |
| truck_utilization_metrics.csv | utilization_rate | float64 | percentual/taxa/índice | escala precisa ser validada antes de formatar como percentual | validar escala; não multiplicar por 100 sem aprovação | 0.71 | 0.71 | alto | evita percentuais incorretos no Power BI | Sim |
| trucks.csv | truck_id | str | ID/chave | risco de conversão indevida para número ou perda de zeros à esquerda | manter como texto e validar chave primária/estrangeira | TRK00001 | TRK00001 | médio | melhora relacionamentos no modelo | Sim |
| trucks.csv | unit_number | int64 | código/número operacional | não deve ser tratado como métrica, mesmo quando armazenado como número | manter como texto/código operacional; validar uso em filtros ou identificação | 3463 | 3463 | médio | evita soma, média ou ordenação numérica indevida no Power BI | Sim |
| trucks.csv | make | str | categoria/status/código | domínio de valores pode precisar de documentação ou padronização futura | manter como texto; padronizar apenas se inconsistência for comprovada | Peterbilt | Peterbilt | baixo | melhora filtros, segmentações e rótulos no Power BI | Sim |
| trucks.csv | model_year | int64 | ano/modelo, atributo temporal | não deve ser tratado como quantidade operacional | manter como ano/atributo; validar formato e uso como segmentação | 2016 | 2016 | baixo | permite análise por ano de modelo sem somas indevidas | Sim |
| trucks.csv | vin | str | identificador operacional confidencial | pode expor informação pessoal, identificável, comercial ou operacional sensível | remover, mascarar ou manter apenas em ambiente privado, conforme aprovação | 1VV205190335317039 | [removido/mascarado/controlado] | alto | reduz risco de exposição em relatórios e arquivos finais | Sim |
| trucks.csv | acquisition_date | str | data, data/hora ou período | precisa de formato validado antes da conversão | converter em etapa futura para data/data-hora ou período mensal | 2017-04-27 | data/período padronizado | médio | permite ordenação temporal e filtros corretos no Power BI | Sim |
| trucks.csv | acquisition_mileage | int64 | métrica numérica operacional: quilometragem de aquisição | unidade e regra de agregação precisam ser documentadas | manter numérico; documentar unidade | 18814 | 18814 | médio | permite medidas operacionais mais claras no Power BI | Sim |
| trucks.csv | fuel_type | str | categoria/status/código | domínio de valores pode precisar de documentação ou padronização futura | manter como texto; padronizar apenas se inconsistência for comprovada | Diesel | Diesel | baixo | melhora filtros, segmentações e rótulos no Power BI | Sim |
| trucks.csv | tank_capacity_gallons | int64 | métrica numérica operacional: capacidade de tanque | unidade e regra de agregação precisam ser documentadas | manter numérico; documentar unidade em galões | 200 | 200 | médio | permite medidas operacionais mais claras no Power BI | Sim |
| trucks.csv | status | str | categoria/status/código | domínio de valores pode precisar de documentação ou padronização futura | manter como texto; padronizar apenas se inconsistência for comprovada | Active | Active | baixo | melhora filtros, segmentações e rótulos no Power BI | Sim |
| trucks.csv | home_terminal | str | categoria/status/código | domínio de valores pode precisar de documentação ou padronização futura | manter como texto; padronizar apenas se inconsistência for comprovada | Omaha | Omaha | baixo | melhora filtros, segmentações e rótulos no Power BI | Sim |

## 6. Regras gerais de tratamento propostas

### 6.1 IDs e chaves

- Manter IDs como texto.
- Não converter IDs para número.
- Preservar zeros à esquerda.
- Não preencher IDs ausentes automaticamente.
- Validar chaves primárias e estrangeiras antes da modelagem.
- Campos aplicáveis: `load_id`, `trip_id`, `customer_id`, `route_id`, `driver_id`, `truck_id`, `trailer_id`, `event_id`, `facility_id`, `maintenance_id`, `incident_id`, `fuel_purchase_id`.

### 6.2 Datas e períodos

- Converter campos de data para tipo data ou data/hora em etapa futura.
- Tratar `month` como período de referência mensal, não como simples categoria.
- Validar formato antes da conversão.
- Não alterar fuso horário sem regra aprovada.
- Campos aplicáveis: `load_date`, `dispatch_date`, `scheduled_datetime`, `actual_datetime`, `purchase_date`, `maintenance_date`, `incident_date`, `contract_start_date`, `hire_date`, `termination_date`, `date_of_birth`, `acquisition_date`, `month`.

### 6.3 Campos financeiros

- Manter como numéricos.
- Formatar como moeda apenas no Power BI.
- Validar moeda.
- Evitar arredondamento prematuro.
- Campos aplicáveis: `revenue`, `fuel_surcharge`, `accessorial_charges`, `annual_revenue_potential`, `total_revenue`, `total_cost`, `maintenance_cost`, `labor_cost`, `parts_cost`, `vehicle_damage_cost`, `cargo_damage_cost`, `claim_amount`.

### 6.4 Percentuais, taxas, índices e escalas

- Validar escala antes de formatar como percentual.
- Diferenciar percentual/taxa operacional de taxa monetária por unidade.
- Não multiplicar por 100 sem aprovação.
- Registrar campos com valores acima de 1 para investigação quando aplicável.
- Campos aplicáveis: `on_time_delivery_rate`, `utilization_rate`, `fuel_surcharge_rate`.
- `base_rate_per_mile` deve ser tratado como taxa monetária por milha, não percentual.
- `price_per_gallon` deve ser tratado como preço unitário, não percentual.

### 6.5 Campos que não devem ser somados diretamente

| campo | agregação preliminar proposta | validação necessária |
| --- | --- | --- |
| `average_mpg` | média ponderada ou validação futura | Sim |
| `average_idle_hours` | média ponderada ou validação futura | Sim |
| `on_time_delivery_rate` | média ponderada ou validação futura | Sim |
| `utilization_rate` | média ponderada ou validação futura | Sim |
| `fuel_surcharge_rate` | média ponderada ou validação futura | Sim |
| `base_rate_per_mile` | média ponderada ou validação futura | Sim |
| `price_per_gallon` | média ponderada ou validação futura | Sim |

### 6.6 Métricas de duração, tempo e quantidade

- Manter como numéricas.
- Documentar unidade.
- Não converter duração em data.
- Validar unidade antes do Power BI.
- Campos aplicáveis: `detention_minutes`, `actual_duration_hours`, `idle_time_hours`, `average_idle_hours`, `downtime_hours`, `labor_hours`, `typical_transit_days`, `credit_terms_days`, `years_experience`.

### 6.7 Campos categóricos, status e códigos

- Manter como texto.
- Padronizar valores apenas se houver inconsistência comprovada.
- Documentar domínio de valores.
- Avaliar criação futura de descrições amigáveis para Power BI.
- Campos aplicáveis: `customer_type`, `primary_freight_type`, `account_status`, `event_type`, `load_type`, `load_status`, `booking_type`, `trip_status`, `employment_status`, `facility_type`, `maintenance_type`, `incident_type`, `status`, `make`, `fuel_type`, `home_terminal`, `location_city`, `location_state`, `origin_city`, `origin_state`, `destination_city`, `destination_state`.

### 6.8 Booleanos e flags

- Manter como booleano.
- Criar descrição amigável apenas em camada final, se aprovado.
- Não tratar como métrica numérica principal.
- Usar para taxas somente com regra documentada.
- Campos aplicáveis: `on_time_flag`, `at_fault_flag`, `injury_flag`, `preventable_flag`.

### 6.9 Dados pessoais, identificáveis e confidenciais

| campo | tipo de risco | recomendação preliminar | impacto no Power BI | validação humana |
| --- | --- | --- | --- | --- |
| `first_name` | dado pessoal | remover, mascarar ou manter em ambiente privado | reduz exposição de pessoas | Sim |
| `last_name` | dado pessoal | remover, mascarar ou manter em ambiente privado | reduz exposição de pessoas | Sim |
| `date_of_birth` | dado pessoal | remover, mascarar ou controlar acesso | reduz risco LGPD | Sim |
| `license_number` | dado pessoal/identificável | remover, mascarar ou controlar acesso | reduz exposição de documento | Sim |
| `vin` | identificador operacional confidencial | remover, mascarar ou restringir | protege ativos/frota | Sim |
| `fuel_card_number` | identificador operacional confidencial | remover, mascarar ou restringir | protege operação financeira | Sim |
| `customer_name` | dado comercial confidencial | anonimizar ou controlar acesso | evita exposição comercial | Sim |
| `description` | texto livre com possível risco | revisar antes de publicar | evita exposição não estruturada | Sim |
| `service_description` | texto livre com possível risco | revisar antes de publicar | evita exposição não estruturada | Sim |

## 7. Valores ausentes e interpretação de nulos

| tabela | coluna | quantidade de nulos | percentual de nulos | interpretação provável | risco de tratamento incorreto | tratamento proposto | validação humana necessária |
| --- | --- | --- | --- | --- | --- | --- | --- |
| drivers.csv | termination_date | 124 | 82.67% | provavelmente indica motorista ativo, não erro | preencher ou remover automaticamente pode distorcer a leitura operacional | não tratar automaticamente; documentar e validar regra de negócio | Sim |
| trips.csv | driver_id | 1714 | 2.01% | pode indicar viagem sem motorista associado ou falha de registro | preencher ou remover automaticamente pode distorcer a leitura operacional | não tratar automaticamente; documentar e validar regra de negócio | Sim |
| trips.csv | truck_id | 1672 | 1.96% | pode indicar viagem sem caminhão associado ou falha de registro | preencher ou remover automaticamente pode distorcer a leitura operacional | não tratar automaticamente; documentar e validar regra de negócio | Sim |
| trips.csv | trailer_id | 1680 | 1.97% | pode indicar viagem sem carreta associada ou falha de registro | preencher ou remover automaticamente pode distorcer a leitura operacional | não tratar automaticamente; documentar e validar regra de negócio | Sim |
| fuel_purchases.csv | driver_id | 3988 | 2.03% | pode indicar compra sem motorista associado | preencher ou remover automaticamente pode distorcer a leitura operacional | não tratar automaticamente; documentar e validar regra de negócio | Sim |
| fuel_purchases.csv | truck_id | 3880 | 1.98% | pode indicar compra sem caminhão associado | preencher ou remover automaticamente pode distorcer a leitura operacional | não tratar automaticamente; documentar e validar regra de negócio | Sim |
| safety_incidents.csv | driver_id | 1 | 0.59% | pode indicar incidente sem motorista associado | preencher ou remover automaticamente pode distorcer a leitura operacional | não tratar automaticamente; documentar e validar regra de negócio | Sim |
| safety_incidents.csv | truck_id | 1 | 0.59% | pode indicar incidente sem caminhão associado | preencher ou remover automaticamente pode distorcer a leitura operacional | não tratar automaticamente; documentar e validar regra de negócio | Sim |

## 8. Relacionamentos e modelagem preliminar

| relacionamento candidato | tipo provável | risco | impacto no Power BI | validação necessária |
| --- | --- | --- | --- | --- |
| `loads.load_id` ↔ `trips.load_id` | 1:1 observado/provável, com validação conceitual pendente | validar se toda carga deve ter exatamente uma viagem antes da modelagem | afeta cardinalidade, filtros, duplicação de linhas e agregações | Sim |
| `trips.trip_id` ↔ `delivery_events.trip_id` | 1:N potencial | duplicação de viagens ao juntar eventos | afeta cardinalidade, filtros, duplicação de linhas e agregações | Sim |
| `loads.customer_id` ↔ `customers.customer_id` | N:1 potencial | cliente ausente ou duplicado afeta segmentação | afeta cardinalidade, filtros, duplicação de linhas e agregações | Sim |
| `loads.route_id` ↔ `routes.route_id` | N:1 potencial | rota ausente afeta análises por origem/destino | afeta cardinalidade, filtros, duplicação de linhas e agregações | Sim |
| `trips.driver_id` ↔ `drivers.driver_id` | N:1 potencial | envolve dados pessoais de motorista | afeta cardinalidade, filtros, duplicação de linhas e agregações | Sim |
| `trips.truck_id` ↔ `trucks.truck_id` | N:1 potencial | vínculo com frota precisa ser validado | afeta cardinalidade, filtros, duplicação de linhas e agregações | Sim |
| `trips.trailer_id` ↔ `trailers.trailer_id` | N:1 potencial | vínculo com carreta/equipamento precisa ser validado | afeta cardinalidade, filtros, duplicação de linhas e agregações | Sim |
| `delivery_events.facility_id` ↔ `facilities.facility_id` | N:1 potencial | eventos podem duplicar instalações | afeta cardinalidade, filtros, duplicação de linhas e agregações | Sim |
| `fuel_purchases.trip_id` ↔ `trips.trip_id` | N:1 potencial | abastecimentos podem ocorrer múltiplas vezes por viagem | afeta cardinalidade, filtros, duplicação de linhas e agregações | Sim |
| `fuel_purchases.truck_id` ↔ `trucks.truck_id` | N:1 potencial | custo de combustível exige granularidade correta | afeta cardinalidade, filtros, duplicação de linhas e agregações | Sim |
| `maintenance_records.truck_id` ↔ `trucks.truck_id` | N:1 potencial | manutenções podem ocorrer várias vezes por caminhão | afeta cardinalidade, filtros, duplicação de linhas e agregações | Sim |
| `safety_incidents.trip_id` ↔ `trips.trip_id` | N:1 potencial | incidentes podem ser zero, um ou vários por viagem | afeta cardinalidade, filtros, duplicação de linhas e agregações | Sim |

A cardinalidade observada não deve ser confundida com cardinalidade conceitual. Tabelas agregadas mensais exigem cuidado com granularidade entidade + período. Também é necessário evitar duplicar medidas ao juntar tabelas fato com tabelas de eventos.

## 9. Entrega prevista para dados tratados

Arquivos que poderão ser criados futuramente em `dados/tratados/`, sem criação nesta etapa:

- `customers_tratado.csv`;
- `loads_tratado.csv`;
- `trips_tratado.csv`;
- `delivery_events_tratado.csv`;
- `routes_tratado.csv`;
- `fuel_purchases_tratado.csv`;
- `trucks_tratado.csv`.

Esses arquivos representam um núcleo inicial hipotético para V1. As tabelas complementares não estão descartadas; elas podem entrar em fases futuras ou em tratamentos adicionais após validação humana. Os nomes ainda são hipóteses e dependem de aprovação.

## 10. Entrega prevista para dados finais

Possíveis arquivos futuros para `dados/finais/`, prontos para Power BI:

- `fato_cargas.csv`;
- `fato_viagens.csv`;
- `fato_eventos_entrega.csv`;
- `fato_abastecimentos.csv`;
- `dim_clientes.csv`;
- `dim_rotas.csv`;
- `dim_caminhoes.csv`;
- `dim_calendario.csv`.

A camada final da V1 usa um núcleo inicial para reduzir risco e complexidade, mas tabelas complementares podem entrar em fases futuras. A camada final deve remover ou mascarar campos sensíveis e evitar granularidade incorreta.

## 11. Decisões pendentes antes da Etapa 03

- Escopo final da V1.
- Tabelas que entram em `dados/tratados/`.
- Tabelas que entram em `dados/finais/`.
- Tratamento de campos pessoais e confidenciais.
- Tratamento de nulos.
- Escala de percentuais.
- Regra de agregação para médias, taxas e preços unitários.
- Relacionamento e granularidade no modelo.
- Campos que serão removidos, mascarados ou mantidos.
- Nomes finais das tabelas para Power BI.

## 12. Decisão da Etapa 02

<!-- INICIO_VALIDACAO_HUMANA -->
Status da Etapa 02:

* [ ] Aprovada
* [x] Aprovada com ressalvas
* [ ] Reprovada para avanço

Observações da validação humana:

* A Etapa 02 está aprovada como plano documental de tratamento e padronização dos dados.
* Nenhuma transformação foi aplicada aos dados brutos nesta etapa.
* O plano define propostas de tratamento por tabela e coluna, mantendo validação humana obrigatória antes da execução.
* A abordagem preserva os dados brutos, separa campos sensíveis, diferencia métricas operacionais, campos financeiros, percentuais, taxas, IDs, datas, categorias e booleanos.
* As ressalvas para a próxima etapa envolvem a confirmação do escopo final da V1, tratamento de dados pessoais/confidenciais, regras de nulos, escala de percentuais, agregação de médias/taxas/preços unitários e validação da granularidade do modelo.
* A Etapa 03 só deve aplicar transformações aprovadas com base neste plano.
<!-- FIM_VALIDACAO_HUMANA -->


## 13. Confirmações finais de segurança

- Dados brutos não foram alterados.
- Nenhuma transformação foi aplicada.
- Nenhum arquivo tratado foi criado.
- Nenhum arquivo final foi criado.
- Nenhum KPI final foi criado.
- Nenhum dashboard foi gerado.
- Relatório criado apenas como plano de tratamento para validação humana.
