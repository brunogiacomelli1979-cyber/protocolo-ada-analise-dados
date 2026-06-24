# Relatório da Etapa 07 — Definição de Perguntas Analíticas e KPIs

## 1. Objetivo da Etapa 07

Definir perguntas analíticas, KPIs e métricas possíveis para o Power BI com base nos dados finais disponíveis e validados nas etapas anteriores do Protocolo ADA.

Esta etapa não cria medidas DAX definitivas, não cria dashboard e não altera dados. O objetivo é transformar a base validada em um mapa analítico claro, documentando o que pode ser respondido com segurança, quais indicadores fazem sentido e quais exigem validação humana antes de virar métrica oficial.

Python gera evidências. IA interpreta hipóteses. Humano valida decisões.

## 2. Contexto metodológico

Este é um projeto orientado por base disponível. Isso significa que as perguntas analíticas não foram definidas antes da descoberta dos dados; elas são derivadas somente depois que os arquivos foram entendidos, tratados, modelados em tabelas finais e validados.

A metodologia de referência principal é Google Data Analytics, adaptada ao contexto do projeto:

* Data Discovery: inspeção inicial e entendimento das bases.
* Prepare: organização das fontes e definição do plano de tratamento.
* Process: padronização, limpeza e criação dos dados finais.
* Ask: definição das perguntas analíticas possíveis com base em dados validados.
* Analyze: cálculo das métricas e construção das medidas.
* Share: criação do relatório ou dashboard no Power BI.
* Act: interpretação, recomendações e tomada de decisão.

A Etapa 07 corresponde principalmente ao momento Ask, com preparação para Analyze. As perguntas abaixo são derivadas dos 8 arquivos finais em `dados/finais/`, validados na Etapa 06 com 45 alertas OK, 9 alertas Atenção e 0 alertas Crítico.

## 3. Bases finais consideradas

| arquivo final | papel analítico | granularidade esperada |
| --- | --- | --- |
| `dim_clientes.csv` | Dimensão de clientes para segmentar receita, cargas e perfil comercial. | Uma linha por `customer_id`. |
| `dim_rotas.csv` | Dimensão de rotas para analisar origem, destino, distância típica e taxas por rota. | Uma linha por `route_id`. |
| `dim_caminhoes.csv` | Dimensão de caminhões para segmentar viagens e abastecimentos por veículo, frota e status. | Uma linha por `truck_id`. |
| `fato_cargas.csv` | Tabela fato de cargas, receita, peso, peças, tipo de carga e status comercial/operacional. | Uma linha por `load_id`. |
| `fato_viagens.csv` | Tabela fato de viagens, distância real, duração, consumo, eficiência e status da viagem. | Uma linha por `trip_id`. |
| `fato_eventos_entrega.csv` | Tabela fato de eventos de entrega, horários, atrasos, detenção e pontualidade por evento. | Uma linha por `event_id`. |
| `fato_abastecimentos.csv` | Tabela fato de abastecimentos, galões, custo total e preço por galão. | Uma linha por `fuel_purchase_id`. |
| `dim_calendario.csv` | Dimensão de tempo para filtros, séries temporais e análise por ano, mês, trimestre e dia da semana. | Uma linha por `data`. |

As perguntas e KPIs abaixo usam apenas campos existentes nesses arquivos. Nenhum campo novo é assumido como disponível nesta etapa.

## 4. Perguntas analíticas possíveis

### Visão executiva

* Qual é a receita total transportada no período?
* Quantas cargas, viagens, eventos de entrega e abastecimentos foram registrados?
* Como receita, volume de cargas, distância percorrida, galões consumidos e custo de combustível evoluem ao longo do tempo?
* Qual é o custo de combustível em relação à receita das cargas, quando os relacionamentos permitirem a análise?
* Quais períodos concentram maior operação, receita ou custo?

### Clientes e receita

* Quais clientes concentram maior receita?
* Como a receita varia por tipo de cliente, tipo de frete principal e status da conta?
* Qual é o ticket médio por carga por cliente?
* Quais clientes possuem maior volume de cargas?
* Existe concentração de receita em poucos clientes?

### Cargas e tipos de frete

* Quantas cargas foram movimentadas por tipo de carga?
* Quais tipos de carga geram maior receita?
* Qual é a distribuição de peso e peças por tipo de carga?
* Como os status de carga se distribuem no período?
* Quais tipos de booking estão associados a maior volume ou receita?

### Rotas e distância

* Quais rotas concentram maior receita, volume de cargas ou distância típica?
* Quais origens e destinos aparecem com maior frequência?
* Como a receita se distribui por estado de origem e destino?
* Quais rotas têm maiores taxas por milha ou surcharge, considerando que esses campos não devem ser somados?
* Existe diferença relevante entre distância típica da rota e distância real da viagem, quando analisadas por relacionamento?

### Viagens e eficiência operacional

* Quantas viagens foram realizadas no período?
* Qual é a distância total percorrida?
* Qual é a duração total e média das viagens?
* Qual é o consumo total de combustível registrado em viagens?
* Qual é a eficiência média de combustível, considerando que `average_mpg` não deve ser somado diretamente?
* Quais caminhões concentram maior distância, consumo ou quantidade de viagens?
* Como os status de viagem se distribuem?

### Entregas e eventos

* Quantos eventos de entrega foram registrados por tipo de evento?
* Qual é o volume de eventos pontuais e não pontuais, usando `on_time_flag`?
* Qual é o total e a média de minutos de detenção?
* Quais locais ou estados concentram maior detenção?
* Como eventos e detenção evoluem ao longo do tempo?

### Combustível e custos

* Qual é o custo total de combustível?
* Quantos galões foram comprados?
* Qual é o preço médio por galão, calculado por regra adequada e não por soma de `price_per_gallon`?
* Quais caminhões concentram maior custo ou volume de abastecimento?
* Como custo, galões e preço médio evoluem ao longo do tempo?
* Qual é a relação entre custo de combustível e distância, quando a análise usar relacionamentos validados?

### Qualidade/limitações dos dados

* Quais campos operacionais possuem nulos preservados?
* Qual percentual de viagens não possui `driver_id`, `truck_id` ou `trailer_id`?
* Qual percentual de abastecimentos não possui `driver_id` ou `truck_id`?
* Quais KPIs podem ser afetados por nulos em relacionamentos?
* Quais campos exigem regra especial de agregação no Power BI?

## 5. KPIs e métricas recomendados

### Diferença entre métrica, KPI e dimensão de análise

* Métrica: medida quantitativa calculável, como receita total, número de cargas ou custo de combustível.
* KPI: métrica usada para acompanhar desempenho contra uma intenção de gestão, objetivo ou meta. Nesta etapa, os KPIs são candidatos, pois metas e limites ainda não foram definidos.
* Dimensão de análise: campo usado para segmentar métricas, como cliente, rota, caminhão, tipo de carga, estado, mês ou status.

### Catálogo recomendado

| nome | pergunta que responde | objetivo | tabela(s) de origem | campos necessários | fórmula conceitual | granularidade | regra de agregação | cuidados no Power BI | limitações |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Receita total | Qual receita foi gerada pelas cargas? | Medir resultado financeiro bruto das cargas. | `fato_cargas.csv` | `revenue` | Soma de `revenue`. | Carga. | Aditiva. | Formatar como moeda; filtrar por data de `load_date`. | Não representa lucro; não desconta combustível, acessoriais ou outros custos. |
| Total de cargas | Quantas cargas foram registradas? | Medir volume operacional/comercial. | `fato_cargas.csv` | `load_id` | Contagem distinta de `load_id`. | Carga. | Aditiva por período se a chave não se repetir entre períodos. | Usar contagem distinta, não contagem simples se houver risco futuro de duplicidade. | Mede registros, não necessariamente entregas concluídas. |
| Ticket médio por carga | Qual é a receita média por carga? | Avaliar valor médio das cargas. | `fato_cargas.csv` | `revenue`, `load_id` | Receita total / total de cargas. | Carga. | Não aditiva. | Calcular como razão de agregados, não média de médias. | Sensível a outliers e mix de clientes/rotas. |
| Receita por cliente | Quais clientes geram maior receita? | Identificar concentração e relevância comercial. | `fato_cargas.csv`, `dim_clientes.csv` | `customer_id`, `customer_name`, `revenue` | Soma de `revenue` por cliente. | Cliente/carga. | Aditiva para receita; ranking por dimensão. | `customer_name` está mascarado; usar como identificador analítico, não nome real. | Não mede margem nem rentabilidade. |
| Receita por tipo de cliente | Como a receita se distribui por tipo de cliente? | Comparar segmentos comerciais. | `fato_cargas.csv`, `dim_clientes.csv` | `customer_id`, `customer_type`, `revenue` | Soma de `revenue` por `customer_type`. | Tipo de cliente. | Aditiva para receita. | Validar categorias e filtros de status de conta. | Diferença entre segmentos não implica causalidade. |
| Receita por rota | Quais rotas concentram maior receita? | Priorizar rotas relevantes no negócio. | `fato_cargas.csv`, `dim_rotas.csv` | `route_id`, `revenue`, `origin_state`, `destination_state` | Soma de `revenue` por rota. | Rota/carga. | Aditiva para receita. | Evitar somar `base_rate_per_mile` e `fuel_surcharge_rate`. | Receita por rota depende do mix de cargas e clientes. |
| Peso total transportado | Qual volume físico foi transportado? | Medir escala operacional em peso. | `fato_cargas.csv` | `weight_lbs` | Soma de `weight_lbs`. | Carga. | Aditiva. | Formatar unidade em libras; evitar misturar com peças sem contexto. | Peso não mede complexidade da operação. |
| Total de peças | Quantas peças foram transportadas? | Medir volume físico complementar. | `fato_cargas.csv` | `pieces` | Soma de `pieces`. | Carga. | Aditiva. | Confirmar significado operacional de peça antes de comparar clientes. | Pode variar por tipo de frete. |
| Cargas por status | Como as cargas se distribuem por status? | Monitorar situação operacional/comercial das cargas. | `fato_cargas.csv` | `load_id`, `load_status` | Contagem de cargas por `load_status`. | Carga/status. | Aditiva para contagem. | Usar barras ou matriz por período e status. | Status precisa de definição de negócio para interpretação. |
| Total de viagens | Quantas viagens foram registradas? | Medir volume de viagens. | `fato_viagens.csv` | `trip_id` | Contagem distinta de `trip_id`. | Viagem. | Aditiva por período se a chave não se repetir entre períodos. | Relacionar com `dispatch_date` para análise temporal. | Uma viagem pode não representar uma entrega finalizada. |
| Distância total percorrida | Quantas milhas reais foram percorridas? | Medir esforço operacional. | `fato_viagens.csv` | `actual_distance_miles` | Soma de `actual_distance_miles`. | Viagem. | Aditiva. | Validar filtros por status de viagem se necessário. | Não compara automaticamente com distância planejada. |
| Duração total de viagens | Quantas horas foram consumidas em viagens? | Medir tempo operacional agregado. | `fato_viagens.csv` | `actual_duration_hours` | Soma de `actual_duration_hours`. | Viagem. | Aditiva. | Usar também média por viagem para leitura operacional. | Não separa tempo produtivo, espera e paradas. |
| Duração média por viagem | Qual é a duração média das viagens? | Avaliar padrão operacional de tempo. | `fato_viagens.csv` | `actual_duration_hours`, `trip_id` | Soma de horas / total de viagens. | Viagem. | Não aditiva. | Calcular como razão de agregados. | Sensível a rotas longas e outliers. |
| Consumo total de combustível em viagens | Quantos galões foram usados nas viagens? | Medir consumo operacional informado em viagem. | `fato_viagens.csv` | `fuel_gallons_used` | Soma de `fuel_gallons_used`. | Viagem. | Aditiva. | Não confundir com galões comprados em abastecimentos. | Pode diferir de compras por estoque, timing ou registro. |
| MPG médio ponderado | Qual é a eficiência média de combustível? | Avaliar eficiência operacional. | `fato_viagens.csv` | `actual_distance_miles`, `fuel_gallons_used`, `average_mpg` | Preferencial: soma de `actual_distance_miles` / soma de `fuel_gallons_used`; alternativa só com validação: média de `average_mpg`. | Viagem. | Não aditiva. | Não somar `average_mpg`; preferir razão ponderada. | Requer validar se `fuel_gallons_used` está completo e coerente. |
| Tempo ocioso total | Quanto tempo ocioso foi registrado? | Medir possível ineficiência operacional. | `fato_viagens.csv` | `idle_time_hours` | Soma de `idle_time_hours`. | Viagem. | Aditiva. | Comparar por período, rota ou caminhão com cuidado. | Não explica causa do tempo ocioso. |
| Eventos de entrega | Quantos eventos foram registrados? | Medir volume de eventos logísticos. | `fato_eventos_entrega.csv` | `event_id`, `event_type` | Contagem distinta de `event_id`. | Evento. | Aditiva. | Segmentar por `event_type`, local e período. | Eventos não equivalem diretamente a entregas únicas. |
| Taxa de pontualidade | Qual proporção de eventos foi pontual? | Acompanhar cumprimento de agenda. | `fato_eventos_entrega.csv` | `on_time_flag`, `event_id` | Eventos com `on_time_flag` verdadeiro / total de eventos com flag válida. | Evento. | Não aditiva. | Tratar como proporção; não somar percentuais entre períodos. | Exige confirmar regra de `on_time_flag` e se todos os tipos de evento entram no denominador. |
| Detenção total | Quantos minutos de detenção foram registrados? | Medir impacto operacional de espera/detenção. | `fato_eventos_entrega.csv` | `detention_minutes` | Soma de `detention_minutes`. | Evento. | Aditiva. | Segmentar por local, estado e tipo de evento. | Não identifica causa da detenção. |
| Detenção média por evento | Qual é a detenção média por evento? | Avaliar severidade média de detenção. | `fato_eventos_entrega.csv` | `detention_minutes`, `event_id` | Soma de `detention_minutes` / total de eventos. | Evento. | Não aditiva. | Calcular como razão de agregados. | Pode ser distorcida por eventos sem detenção ou outliers. |
| Galões comprados | Quantos galões foram comprados? | Medir volume de abastecimento. | `fato_abastecimentos.csv` | `gallons` | Soma de `gallons`. | Abastecimento. | Aditiva. | Usar `purchase_date` para análise temporal. | Não equivale necessariamente ao combustível consumido no mesmo período. |
| Custo total de combustível | Qual foi o custo total de abastecimento? | Medir gasto direto registrado com combustível. | `fato_abastecimentos.csv` | `total_cost` | Soma de `total_cost`. | Abastecimento. | Aditiva. | Formatar como moeda; relacionar com caminhão quando `truck_id` existir. | Não inclui outros custos operacionais. |
| Preço médio ponderado por galão | Qual foi o preço médio pago por galão? | Avaliar custo unitário de combustível. | `fato_abastecimentos.csv` | `total_cost`, `gallons`, `price_per_gallon` | Soma de `total_cost` / soma de `gallons`. | Abastecimento. | Não aditiva. | Não somar `price_per_gallon`; usar razão ponderada. | Exige consistência entre `total_cost`, `gallons` e `price_per_gallon`. |
| Custo de combustível por milha | Quanto combustível custou por milha percorrida? | Aproximar eficiência econômica operacional. | `fato_abastecimentos.csv`, `fato_viagens.csv` | `trip_id`, `total_cost`, `actual_distance_miles` | Soma de `total_cost` / soma de `actual_distance_miles`. | Viagem/abastecimento. | Não aditiva. | Usar relacionamento por `trip_id`; evitar períodos em que compra e viagem não sejam comparáveis. | Pode misturar timing de compra e consumo. |
| Viagens por caminhão | Quais caminhões concentram mais viagens? | Entender uso da frota. | `fato_viagens.csv`, `dim_caminhoes.csv` | `truck_id`, `trip_id`, `unit_number`, `status` | Contagem distinta de `trip_id` por caminhão. | Caminhão/viagem. | Aditiva para contagem. | Nulos em `truck_id` devem aparecer como categoria de qualidade ou ser filtrados conscientemente. | Não mede disponibilidade real da frota. |
| Custo de combustível por caminhão | Quais caminhões concentram maior custo de abastecimento? | Avaliar distribuição de custo por veículo. | `fato_abastecimentos.csv`, `dim_caminhoes.csv` | `truck_id`, `total_cost`, `unit_number` | Soma de `total_cost` por caminhão. | Caminhão/abastecimento. | Aditiva. | Nulos em `truck_id` devem ser tratados como não atribuídos, não como erro automático. | Custo pode depender da rota, carga, distância e operação. |
| Registros sem caminhão informado | Qual parte da operação não tem `truck_id`? | Monitorar qualidade e completude operacional. | `fato_viagens.csv`, `fato_abastecimentos.csv` | `truck_id`, `trip_id`, `fuel_purchase_id` | Registros com `truck_id` nulo / total de registros. | Viagem ou abastecimento. | Não aditiva. | Criar medida separada por tabela; não misturar denominadores. | Nulo pode ser condição operacional legítima ou lacuna de cadastro. |

## 6. KPIs que NÃO devem ser criados nesta fase

Alguns indicadores parecem úteis, mas não devem virar KPI oficial ainda:

| indicador candidato | motivo para não criar agora | validação necessária |
| --- | --- | --- |
| Lucro ou margem por carga | Não há campos completos de custo total, impostos, pedágios, mão de obra ou outros custos operacionais. | Definir modelo de custos e regra de margem. |
| Rentabilidade por cliente | Há receita, mas não há custo total por cliente com regra validada. | Definir rateio de custos e escopo financeiro. |
| SLA oficial de entrega | Existe `on_time_flag`, mas a regra de pontualidade precisa ser confirmada. | Validar o significado de `scheduled_datetime`, `actual_datetime` e `on_time_flag`. |
| Custo total por rota | Há combustível e cargas, mas não há regra completa para alocar abastecimentos e outros custos por rota. | Definir relação entre viagem, rota, carga e abastecimento. |
| Eficiência de motorista | Existem `driver_id` em fatos, mas não há dimensão de motoristas e há nulos preservados. | Criar/validar dimensão de motoristas e regra de atribuição. |
| Utilização real da frota | Há viagens por caminhão, mas não há calendário de disponibilidade, manutenção ou capacidade operacional diária. | Definir disponibilidade, horas úteis e frota ativa por período. |
| Atraso médio oficial | Há datas de evento e detenção, mas a definição de atraso precisa ser validada por tipo de evento. | Definir quais eventos entram na métrica e como calcular atraso. |
| Forecast de receita, combustível ou demanda | O projeto ainda está na definição de perguntas e KPIs. | Validar histórico, sazonalidade e objetivo de previsão. |
| Causalidade entre rota, cliente, caminhão e eficiência | As bases permitem correlações, não prova causal direta. | Exigir desenho analítico específico, controles e validação humana. |

## 7. Campos com risco de agregação indevida

| campo | tabela | tipo de risco | orientação |
| --- | --- | --- | --- |
| `average_mpg` | `fato_viagens.csv` | Média operacional não aditiva. | Não somar. Preferir `SUM(actual_distance_miles) / SUM(fuel_gallons_used)` quando os campos forem válidos. |
| `price_per_gallon` | `fato_abastecimentos.csv` | Preço unitário não aditivo. | Não somar. Preferir `SUM(total_cost) / SUM(gallons)`. |
| `base_rate_per_mile` | `dim_rotas.csv` | Taxa por unidade de distância, não valor total. | Não somar por rota. Usar como atributo, média simples apenas com contexto ou cálculo ponderado se houver regra. |
| `fuel_surcharge_rate` | `dim_rotas.csv` | Taxa/percentual com escala a confirmar. | Não somar e não transformar em percentual sem confirmar escala. |

Médias, preços unitários, taxas e percentuais devem ser tratados como medidas não aditivas ou semi-aditivas, dependendo do contexto. Em Power BI, eles devem ser calculados com medidas explícitas e não arrastados diretamente como soma automática.

## 8. Tratamento dos nulos operacionais nos KPIs

Nulos operacionais não devem ser tratados automaticamente como erro. A Etapa 06 registrou nulos preservados e aprovou o avanço com ressalvas. Nesta etapa, a regra é documentar o impacto, não remover nem imputar.

| tabela | campo | impacto nos KPIs | recomendação |
| --- | --- | --- | --- |
| `fato_viagens.csv` | `driver_id` | Afeta métricas por motorista e qualquer leitura de produtividade individual. | Não criar KPI oficial por motorista nesta fase; criar métrica de registros sem motorista, se necessário. |
| `fato_viagens.csv` | `truck_id` | Afeta viagens, distância, consumo e eficiência por caminhão. | Mostrar categoria "não informado" ou indicador de qualidade; não descartar automaticamente. |
| `fato_viagens.csv` | `trailer_id` | Afeta análises por trailer, caso sejam propostas no futuro. | Não criar KPIs por trailer nesta fase. |
| `fato_abastecimentos.csv` | `driver_id` | Afeta custo ou abastecimento por motorista. | Não criar KPI por motorista usando abastecimentos nesta fase. |
| `fato_abastecimentos.csv` | `truck_id` | Afeta custo, galões e preço médio por caminhão. | Separar abastecimentos sem caminhão informado e reportar como limitação. |

Regras gerais:

* Não remover registros nulos nesta etapa.
* Não imputar `driver_id`, `truck_id` ou `trailer_id`.
* Não converter nulos em zero.
* Não ocultar nulos sem deixar claro o impacto no denominador.
* Quando o KPI depender de uma dimensão com nulos, exibir a parcela não atribuída ou documentar o filtro usado.

## 9. Recomendações para páginas do Power BI

| página sugerida | objetivo | métricas principais | dimensões/filtros recomendados |
| --- | --- | --- | --- |
| Visão Executiva | Dar leitura rápida do desempenho geral. | Receita total, total de cargas, total de viagens, distância total, custo de combustível, galões comprados, preço médio ponderado por galão. | Período, cliente, rota, status de carga, status de viagem. |
| Clientes e Receita | Entender concentração e perfil comercial. | Receita por cliente, ticket médio por carga, cargas por cliente, receita por tipo de cliente. | Cliente mascarado, tipo de cliente, tipo de frete principal, status da conta, período. |
| Rotas e Cargas | Avaliar rotas, origens, destinos e mix de carga. | Receita por rota, cargas por rota, peso total, peças, cargas por tipo e status. | Origem, destino, estado, tipo de carga, booking type, período. |
| Viagens e Eficiência | Acompanhar execução operacional. | Total de viagens, distância total, duração média, consumo total, MPG ponderado, tempo ocioso. | Caminhão, status da viagem, rota, período. |
| Entregas e Eventos | Monitorar eventos, pontualidade e detenção. | Eventos por tipo, taxa de pontualidade, detenção total, detenção média. | Tipo de evento, cidade, estado, período. |
| Combustível e Custos | Analisar abastecimentos e custos unitários. | Custo total, galões comprados, preço médio ponderado por galão, custo por caminhão, custo por milha quando aplicável. | Caminhão, estado/local de abastecimento, período. |
| Qualidade dos Dados | Tornar limitações visíveis e auditáveis. | Registros sem `driver_id`, sem `truck_id`, sem `trailer_id`, campos com risco de agregação, status da validação. | Tabela, campo, período, tipo de registro. |

As páginas devem começar com perguntas claras e terminar com limitações visíveis. Isso reduz o risco de interpretar correlação como causalidade e evita que o dashboard pareça mais conclusivo do que os dados permitem.

## 10. Limitações da Etapa 07

* Esta etapa define perguntas, métricas e KPIs candidatos; ela não implementa medidas DAX definitivas.
* Não foram criados CSVs, dashboards, visuais ou transformações adicionais.
* Não foram inventados campos além dos existentes nos dados finais.
* Não há metas de negócio, portanto os KPIs ainda não possuem faixas de sucesso, alerta ou criticidade.
* Não há dimensão de motoristas, então KPIs por motorista devem aguardar nova modelagem ou validação.
* Não há campos completos para lucro, margem, custo total operacional ou rentabilidade.
* Percentuais e taxas não foram transformados porque a escala precisa ser confirmada.
* Médias e preços unitários não devem ser somados diretamente.
* Relações observadas nos dados permitem análise descritiva, mas não provam causalidade.

## 11. Recomendação para avanço

O projeto pode avançar para a etapa de modelagem Power BI e definição de medidas, desde que as ressalvas documentadas sejam mantidas no desenho do modelo.

Recomendação objetiva: avançar para a modelagem no Power BI e para a especificação das medidas DAX, priorizando métricas aditivas e razões de agregados já documentadas nesta etapa. Indicadores que dependem de regra de negócio, metas, margem, SLA oficial, motorista ou causalidade devem permanecer fora do escopo até validação humana adicional.

## 12. Decisão da Etapa 07

<!-- INICIO_VALIDACAO_HUMANA -->
Status da Etapa 07:

* [ ] Aprovada
* [x] Aprovada com ressalvas
* [ ] Reprovada para avanço

Observações da validação humana:

* A Etapa 07 está aprovada como etapa documental de definição de perguntas analíticas, métricas e KPIs candidatos.
* A etapa respeitou o contexto do projeto orientado por base disponível, derivando perguntas a partir dos dados finais já validados.
* Não foram alterados dados brutos, tratados ou finais.
* Não foram criados CSVs, dashboards ou medidas DAX definitivas.
* As perguntas analíticas foram organizadas por temas relevantes para o futuro dashboard Power BI.
* O catálogo de métricas documentou origem, campos necessários, fórmula conceitual, granularidade, regra de agregação, cuidados e limitações.
* As ressalvas principais para avanço são: priorizar um conjunto enxuto de métricas na V1, validar com cuidado indicadores não aditivos e manter fora do escopo KPIs que dependem de regra de negócio adicional, como margem, SLA oficial, rentabilidade e eficiência por motorista.
* A próxima etapa pode avançar para especificação do modelo Power BI e definição controlada das medidas DAX.

<!-- FIM_VALIDACAO_HUMANA -->

## 13. Confirmações finais

* A Etapa 07 foi criada como documentação analítica.
* Dados brutos não foram alterados.
* Dados tratados não foram alterados.
* Dados finais não foram alterados.
* Nenhum CSV foi criado.
* Nenhum dashboard foi criado.
* Nenhuma medida DAX definitiva foi criada.
* Nenhum KPI foi proposto sem base nos arquivos finais disponíveis.
* Campos de risco de agregação foram documentados.
* Nulos operacionais foram tratados como ponto de atenção, não como erro automático.
* O projeto pode avançar para modelagem Power BI e definição controlada de medidas.
