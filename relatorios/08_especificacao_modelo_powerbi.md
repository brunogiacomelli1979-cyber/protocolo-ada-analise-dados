# Relatório da Etapa 08 — Especificação do Modelo Power BI e Medidas DAX

## 1. Objetivo da Etapa 08

Documentar como o modelo Power BI deve ser construído a partir dos dados finais validados, incluindo tabelas a importar, relacionamentos recomendados, medidas DAX candidatas, formatos, páginas do dashboard, cuidados de agregação e limitações.

Esta etapa é documental. Não altera dados brutos, tratados ou finais, não cria CSVs, não cria dashboard, não cria arquivo `.pbix` e não executa Power BI.

Python gera evidências. IA interpreta hipóteses. Humano valida decisões.

## 2. Contexto metodológico

A Etapa 08 faz a ponte entre Ask/Analyze e Share na metodologia Google Data Analytics adaptada ao Protocolo ADA.

Na Etapa 07, as perguntas analíticas, métricas e KPIs candidatos foram definidos com base nos dados finais disponíveis. Nesta etapa, essas definições são traduzidas para uma especificação de construção no Power BI: modelo, relacionamentos, medidas candidatas, formatos e páginas sugeridas.

O objetivo é especificar antes de montar o dashboard. Isso reduz risco de decisões improvisadas no Power BI, evita agregações automáticas perigosas e mantém rastreabilidade entre perguntas analíticas, campos disponíveis e medidas propostas.

## 3. Arquivos finais a importar no Power BI

| tabela a importar | arquivo | papel | chave principal | observação |
| --- | --- | --- | --- | --- |
| `dim_clientes` | `dados/finais/dim_clientes.csv` | Dimensão | `customer_id` | Segmenta cargas e receita por cliente, tipo, status e frete principal. |
| `dim_rotas` | `dados/finais/dim_rotas.csv` | Dimensão | `route_id` | Segmenta cargas e viagens por origem, destino, distância típica e taxas de rota. |
| `dim_caminhoes` | `dados/finais/dim_caminhoes.csv` | Dimensão | `truck_id` | Segmenta viagens e abastecimentos por caminhão, modelo, status e terminal. |
| `fato_cargas` | `dados/finais/fato_cargas.csv` | Fato | `load_id` | Registra cargas, receita, peso, peças, status e tipo de carga. |
| `fato_viagens` | `dados/finais/fato_viagens.csv` | Fato | `trip_id` | Registra viagens, distância, duração, consumo, eficiência e status. |
| `fato_eventos_entrega` | `dados/finais/fato_eventos_entrega.csv` | Fato | `event_id` | Registra eventos, horários, detenção e pontualidade. |
| `fato_abastecimentos` | `dados/finais/fato_abastecimentos.csv` | Fato | `fuel_purchase_id` | Registra abastecimentos, galões, preço por galão e custo total. |
| `dim_calendario` | `dados/finais/dim_calendario.csv` | Calendário | `data` | Suporta filtros temporais e séries por ano, mês, trimestre e dia da semana. |

Recomendação de nomenclatura: ao importar no Power BI, remover o sufixo `.csv` do nome das tabelas para facilitar leitura e escrita de medidas.

## 4. Modelo de dados recomendado

O modelo recomendado é um modelo estrela adaptado.

Dimensões principais:

* `dim_clientes`
* `dim_rotas`
* `dim_caminhoes`
* `dim_calendario`

Tabelas fato:

* `fato_cargas`
* `fato_viagens`
* `fato_eventos_entrega`
* `fato_abastecimentos`

O centro analítico do modelo é formado pelas tabelas fato. As dimensões devem filtrar as fatos por chaves estáveis e relacionamentos de um-para-muitos. Sempre que possível, a direção de filtro deve ser simples, da dimensão para a fato.

Há relacionamentos fato-fato possíveis, especialmente:

* `fato_viagens[load_id]` com `fato_cargas[load_id]`
* `fato_eventos_entrega[trip_id]` com `fato_viagens[trip_id]`
* `fato_abastecimentos[trip_id]` com `fato_viagens[trip_id]`

Esses relacionamentos devem ser usados com cautela. Eles ajudam a navegar entre processos operacionais, mas podem criar caminhos ambíguos quando combinados com dimensões compartilhadas e calendário. A V1 deve priorizar relacionamentos dimensão-fato e usar relacionamentos fato-fato apenas quando necessários para medidas específicas.

## 5. Relacionamentos recomendados

| tabela origem | coluna origem | tabela destino | coluna destino | cardinalidade esperada | direção de filtro recomendada | obrigatoriedade | cuidado/observação |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `dim_clientes` | `customer_id` | `fato_cargas` | `customer_id` | 1:N | Simples: `dim_clientes` filtra `fato_cargas` | Obrigatório | Relacionamento dimensão-fato validado sem chaves órfãs. |
| `dim_rotas` | `route_id` | `fato_cargas` | `route_id` | 1:N | Simples: `dim_rotas` filtra `fato_cargas` | Obrigatório | Base para receita e volume por rota. |
| `fato_cargas` | `load_id` | `fato_viagens` | `load_id` | 1:1 observado | Simples, se usado: `fato_cargas` filtra `fato_viagens` | Opcional na V1 | É relacionamento fato-fato; evitar bidirecional salvo necessidade comprovada. |
| `dim_caminhoes` | `truck_id` | `fato_viagens` | `truck_id` | 1:N | Simples: `dim_caminhoes` filtra `fato_viagens` | Recomendado | Há nulos preservados em `fato_viagens[truck_id]`; não remover automaticamente. |
| `fato_viagens` | `trip_id` | `fato_eventos_entrega` | `trip_id` | 1:N | Simples, se usado: `fato_viagens` filtra `fato_eventos_entrega` | Opcional na V1 | É relacionamento fato-fato; útil para eventos por viagem. |
| `fato_viagens` | `trip_id` | `fato_abastecimentos` | `trip_id` | 1:N | Simples, se usado: `fato_viagens` filtra `fato_abastecimentos` | Opcional na V1 | É relacionamento fato-fato; usar com cuidado em custo por milha. |
| `dim_caminhoes` | `truck_id` | `fato_abastecimentos` | `truck_id` | 1:N | Simples: `dim_caminhoes` filtra `fato_abastecimentos` | Recomendado | Há nulos preservados em `fato_abastecimentos[truck_id]`; reportar não atribuídos. |

Direção bidirecional não é recomendada para a V1. Caso alguma pergunta dependa de propagação entre fatos, preferir medidas DAX explícitas ou páginas separadas antes de habilitar filtro bidirecional.

## 6. Relacionamentos com a dimensão calendário

Relacionamentos temporais recomendados:

| tabela fato/dimensão | campo de data | relacionamento com `dim_calendario[data]` | status recomendado | observação |
| --- | --- | --- | --- | --- |
| `fato_cargas` | `load_date` | `dim_calendario[data]` -> `fato_cargas[load_date]` | Ativo | Data principal para receita e cargas. |
| `fato_viagens` | `dispatch_date` | `dim_calendario[data]` -> `fato_viagens[dispatch_date]` | Ativo | Data principal para viagens, distância e consumo. |
| `fato_eventos_entrega` | `scheduled_datetime` | `dim_calendario[data]` -> `fato_eventos_entrega[scheduled_datetime]` | Ativo ou inativo conforme o modelo | Data de agenda do evento; se houver hora, converter tipo para data no modelo. |
| `fato_eventos_entrega` | `actual_datetime` | `dim_calendario[data]` -> `fato_eventos_entrega[actual_datetime]` | Inativo recomendado | Data real do evento; usar medida com `USERELATIONSHIP` se necessário. |
| `fato_abastecimentos` | `purchase_date` | `dim_calendario[data]` -> `fato_abastecimentos[purchase_date]` | Ativo | Data principal para custos e galões comprados. |
| `dim_clientes` | `contract_start_date` | `dim_calendario[data]` -> `dim_clientes[contract_start_date]` | Opcional/inativo | Usar apenas para análises de início de contrato. |
| `dim_caminhoes` | `acquisition_date` | `dim_calendario[data]` -> `dim_caminhoes[acquisition_date]` | Opcional/inativo | Usar apenas para análises de aquisição de frota. |

Cuidado importante: uma mesma tabela fato pode ter múltiplas datas. O Power BI só deve ter uma relação ativa por caminho analítico quando houver risco de ambiguidade. Para `fato_eventos_entrega`, escolher `scheduled_datetime` ou `actual_datetime` como data principal da página e documentar a escolha.

Se campos com sufixo `datetime` forem importados como data/hora, validar no Power BI se a relação com `dim_calendario[data]` funciona corretamente. Quando houver componente de hora, criar ajuste dentro do modelo somente se necessário e documentar a decisão.

## 7. Medidas DAX candidatas

As fórmulas abaixo são candidatas para V1. Elas devem ser criadas como medidas explícitas, preferencialmente em uma tabela organizadora chamada `Medidas`, criada manualmente no Power BI. KPIs sem meta continuam sendo métricas candidatas, não KPIs oficiais.

### Receita Total

* Tabela recomendada: `Medidas`
* Objetivo: medir receita bruta das cargas.
* Tipo: aditiva.
* Formato sugerido: moeda.
* Cuidados: não representa lucro ou margem.

```DAX
Receita Total =
SUM ( fato_cargas[revenue] )
```

### Total de Cargas

* Tabela recomendada: `Medidas`
* Objetivo: contar cargas únicas.
* Tipo: aditiva para contagem.
* Formato sugerido: número inteiro.
* Cuidados: usar contagem distinta.

```DAX
Total de Cargas =
DISTINCTCOUNT ( fato_cargas[load_id] )
```

### Total de Viagens

* Tabela recomendada: `Medidas`
* Objetivo: contar viagens únicas.
* Tipo: aditiva para contagem.
* Formato sugerido: número inteiro.
* Cuidados: uma viagem não equivale necessariamente a entrega concluída.

```DAX
Total de Viagens =
DISTINCTCOUNT ( fato_viagens[trip_id] )
```

### Distância Total

* Tabela recomendada: `Medidas`
* Objetivo: medir milhas reais percorridas.
* Tipo: aditiva.
* Formato sugerido: número decimal ou inteiro com unidade em milhas.
* Cuidados: validar filtros por status de viagem se necessário.

```DAX
Distância Total =
SUM ( fato_viagens[actual_distance_miles] )
```

### Custo Total de Combustível

* Tabela recomendada: `Medidas`
* Objetivo: medir gasto total registrado com abastecimentos.
* Tipo: aditiva.
* Formato sugerido: moeda.
* Cuidados: não inclui outros custos operacionais.

```DAX
Custo Total de Combustível =
SUM ( fato_abastecimentos[total_cost] )
```

### Galões Comprados

* Tabela recomendada: `Medidas`
* Objetivo: medir volume total comprado em abastecimentos.
* Tipo: aditiva.
* Formato sugerido: decimal com unidade em galões.
* Cuidados: não confundir galões comprados com combustível consumido na viagem.

```DAX
Galões Comprados =
SUM ( fato_abastecimentos[gallons] )
```

### Preço Médio Ponderado por Galão

* Tabela recomendada: `Medidas`
* Objetivo: medir preço unitário médio ponderado pelo volume comprado.
* Tipo: razão de agregados.
* Formato sugerido: moeda com 2 a 3 casas decimais.
* Cuidados: não somar `price_per_gallon`; usar `total_cost / gallons`.

```DAX
Preço Médio Ponderado por Galão =
DIVIDE ( [Custo Total de Combustível], [Galões Comprados] )
```

### MPG Médio Ponderado

* Tabela recomendada: `Medidas`
* Objetivo: medir eficiência média de combustível por razão ponderada.
* Tipo: razão de agregados.
* Formato sugerido: decimal.
* Cuidados: não somar `average_mpg`; validar se `fuel_gallons_used` é confiável.

```DAX
MPG Médio Ponderado =
DIVIDE (
    SUM ( fato_viagens[actual_distance_miles] ),
    SUM ( fato_viagens[fuel_gallons_used] )
)
```

### Taxa de Pontualidade

* Tabela recomendada: `Medidas`
* Objetivo: medir proporção de eventos pontuais.
* Tipo: razão de agregados.
* Formato sugerido: percentual.
* Cuidados: confirmar a regra de negócio de `on_time_flag` antes de tratar como SLA oficial.

```DAX
Eventos Pontuais =
CALCULATE (
    DISTINCTCOUNT ( fato_eventos_entrega[event_id] ),
    fato_eventos_entrega[on_time_flag] = TRUE ()
)

Total de Eventos com Flag =
CALCULATE (
    DISTINCTCOUNT ( fato_eventos_entrega[event_id] ),
    NOT ( ISBLANK ( fato_eventos_entrega[on_time_flag] ) )
)

Taxa de Pontualidade =
DIVIDE ( [Eventos Pontuais], [Total de Eventos com Flag] )
```

Se `on_time_flag` for importado como texto ou número, adaptar a condição após validação do tipo no Power BI.

### Detenção Total

* Tabela recomendada: `Medidas`
* Objetivo: medir minutos totais de detenção.
* Tipo: aditiva.
* Formato sugerido: número inteiro com unidade em minutos.
* Cuidados: não explica causa da detenção.

```DAX
Detenção Total =
SUM ( fato_eventos_entrega[detention_minutes] )
```

### Detenção Média por Evento

* Tabela recomendada: `Medidas`
* Objetivo: medir severidade média de detenção por evento.
* Tipo: razão de agregados.
* Formato sugerido: decimal com unidade em minutos.
* Cuidados: não calcular como média de médias.

```DAX
Detenção Média por Evento =
DIVIDE (
    [Detenção Total],
    DISTINCTCOUNT ( fato_eventos_entrega[event_id] )
)
```

### Registros sem Caminhão Informado

* Tabela recomendada: `Medidas`
* Objetivo: monitorar qualidade de dados em viagens e abastecimentos.
* Tipo: qualidade de dados.
* Formato sugerido: número inteiro.
* Cuidados: nulos não devem ser removidos ou imputados automaticamente.

```DAX
Viagens sem Caminhão Informado =
CALCULATE (
    DISTINCTCOUNT ( fato_viagens[trip_id] ),
    ISBLANK ( fato_viagens[truck_id] )
)

Abastecimentos sem Caminhão Informado =
CALCULATE (
    DISTINCTCOUNT ( fato_abastecimentos[fuel_purchase_id] ),
    ISBLANK ( fato_abastecimentos[truck_id] )
)

Registros sem Caminhão Informado =
[Viagens sem Caminhão Informado] + [Abastecimentos sem Caminhão Informado]
```

### Percentual de Registros sem Caminhão Informado

* Tabela recomendada: `Medidas`
* Objetivo: medir impacto relativo dos nulos em `truck_id`.
* Tipo: qualidade de dados / razão de agregados.
* Formato sugerido: percentual.
* Cuidados: mistura denominadores de viagens e abastecimentos; usar como indicador geral de qualidade, não métrica operacional de negócio.

```DAX
Total Registros com Caminhão Aplicável =
[Total de Viagens] + DISTINCTCOUNT ( fato_abastecimentos[fuel_purchase_id] )

% Registros sem Caminhão Informado =
DIVIDE ( [Registros sem Caminhão Informado], [Total Registros com Caminhão Aplicável] )
```

### Ticket Médio por Carga

* Tabela recomendada: `Medidas`
* Objetivo: medir receita média por carga.
* Tipo: razão de agregados.
* Formato sugerido: moeda.
* Cuidados: sensível a outliers e mix de clientes/rotas.

```DAX
Ticket Médio por Carga =
DIVIDE ( [Receita Total], [Total de Cargas] )
```

### Peso Total Transportado

* Tabela recomendada: `Medidas`
* Objetivo: medir volume físico em libras.
* Tipo: aditiva.
* Formato sugerido: número decimal ou inteiro com unidade em libras.
* Cuidados: não confundir peso com quantidade de peças.

```DAX
Peso Total Transportado =
SUM ( fato_cargas[weight_lbs] )
```

### Tempo Ocioso Total

* Tabela recomendada: `Medidas`
* Objetivo: medir horas totais de ociosidade registradas.
* Tipo: aditiva.
* Formato sugerido: decimal com unidade em horas.
* Cuidados: não prova causa da ociosidade.

```DAX
Tempo Ocioso Total =
SUM ( fato_viagens[idle_time_hours] )
```

## 8. Medidas prioritárias para V1

Priorizar um conjunto enxuto para a primeira versão:

| prioridade | medida | motivo |
| --- | --- | --- |
| 1 | Receita Total | Métrica executiva central e aditiva. |
| 2 | Total de Cargas | Volume operacional/comercial básico. |
| 3 | Total de Viagens | Volume operacional básico. |
| 4 | Distância Total | Esforço operacional em milhas. |
| 5 | Custo Total de Combustível | Principal custo direto disponível. |
| 6 | Galões Comprados | Volume de combustível adquirido. |
| 7 | Preço Médio Ponderado por Galão | Custo unitário calculado como razão de agregados. |
| 8 | MPG Médio Ponderado | Eficiência calculada por razão de agregados. |
| 9 | Taxa de Pontualidade | Indicador candidato de serviço, ainda sem meta oficial. |
| 10 | Detenção Total | Medida operacional aditiva de espera. |
| 11 | Registros sem Caminhão Informado | Indicador de qualidade para nulos operacionais. |

## 9. Medidas que devem ficar fora da V1

| medida/indicador | motivo para ficar fora da V1 |
| --- | --- |
| Lucro ou margem | Não há custos completos, impostos, pedágios, mão de obra ou regra de margem. |
| Rentabilidade por cliente | Há receita por cliente, mas não há custo total por cliente com regra validada. |
| SLA oficial | `on_time_flag` permite métrica candidata, mas SLA exige regra formal e meta. |
| Eficiência por motorista | Não há dimensão de motoristas e há nulos em `driver_id`. |
| Forecast | Exige objetivo preditivo, validação de série temporal e método estatístico próprio. |
| Causalidade | As bases permitem análise descritiva e correlações, mas não provam causa e efeito. |

## 10. Formatação recomendada no Power BI

| tipo | aplicar em | recomendação |
| --- | --- | --- |
| Moeda | `Receita Total`, `Custo Total de Combustível`, `Ticket Médio por Carga`, `Preço Médio Ponderado por Galão` | Usar moeda com separador de milhar e 2 casas decimais. |
| Número inteiro | `Total de Cargas`, `Total de Viagens`, contagens de eventos e registros sem caminhão | Sem casas decimais. |
| Decimal | `Distância Total`, `Galões Comprados`, `MPG Médio Ponderado`, duração média | 1 a 2 casas decimais conforme legibilidade. |
| Percentual | `Taxa de Pontualidade`, `% Registros sem Caminhão Informado` | Percentual com 1 ou 2 casas decimais. |
| Duração | `Duração total`, `Duração média`, `Tempo Ocioso Total` | Exibir em horas; não converter para dias sem necessidade. |
| Milhas | `actual_distance_miles`, `typical_distance_miles`, `Distância Total` | Nomear visual com unidade explícita. |
| Galões | `gallons`, `fuel_gallons_used`, `Galões Comprados` | Nomear visual com unidade explícita. |
| Libras | `weight_lbs`, `Peso Total Transportado` | Nomear visual com unidade explícita. |
| Minutos | `detention_minutes`, `Detenção Total` | Nomear visual com unidade explícita. |

Não transformar `fuel_surcharge_rate` em percentual sem confirmar escala. Não somar `average_mpg`, `price_per_gallon`, `base_rate_per_mile` ou `fuel_surcharge_rate`.

## 11. Campos que devem ser ocultados ou usados com cuidado

| grupo | campos | recomendação |
| --- | --- | --- |
| Chaves técnicas | `customer_id`, `route_id`, `truck_id`, `load_id`, `trip_id`, `event_id`, `fuel_purchase_id` | Manter no modelo para relacionamento, mas ocultar de usuários finais quando houver nomes/atributos mais amigáveis. |
| Campos sensíveis mascarados | `dim_clientes[customer_name]` | Pode ser usado como identificador analítico mascarado; deixar claro que não é nome real. |
| Campos não aditivos | `average_mpg`, `price_per_gallon`, `base_rate_per_mile`, `fuel_surcharge_rate` | Não permitir soma automática; preferir medidas explícitas. |
| Campos com nulos operacionais | `fato_viagens[driver_id]`, `fato_viagens[truck_id]`, `fato_viagens[trailer_id]`, `fato_abastecimentos[driver_id]`, `fato_abastecimentos[truck_id]` | Não remover nem imputar; exibir como qualidade de dados quando impactarem indicadores. |
| Datas alternativas | `actual_datetime`, `contract_start_date`, `acquisition_date` | Usar com relações inativas ou páginas específicas para evitar ambiguidade temporal. |

## 12. Páginas recomendadas do dashboard

| página | objetivo | perguntas respondidas | KPIs principais | visuais sugeridos | filtros/slicers recomendados | limitações |
| --- | --- | --- | --- | --- | --- | --- |
| Visão Executiva | Sintetizar desempenho geral. | Qual foi a receita, volume, distância e custo no período? | Receita Total, Total de Cargas, Total de Viagens, Distância Total, Custo Total de Combustível, MPG Médio Ponderado. | Cards, linha temporal, barras por mês, matriz resumo. | Período, cliente, rota, status de carga, status de viagem. | Sem lucro/margem; KPIs sem metas oficiais. |
| Clientes e Receita | Analisar concentração comercial. | Quais clientes e segmentos geram receita e cargas? | Receita Total, Total de Cargas, Ticket Médio por Carga. | Ranking de clientes, barras por tipo de cliente, linha temporal. | Período, tipo de cliente, status da conta, tipo de frete principal. | `customer_name` é mascarado; não há rentabilidade. |
| Rotas e Cargas | Avaliar rotas, origens, destinos e mix. | Quais rotas concentram receita, carga e peso? | Receita Total, Total de Cargas, Peso Total Transportado. | Mapa ou barras por estado, ranking de rotas, matriz origem-destino. | Período, origem, destino, tipo de carga, booking type. | Não somar taxas por milha ou surcharge. |
| Viagens e Eficiência | Monitorar execução operacional. | Quantas viagens ocorreram, quanta distância foi percorrida e qual a eficiência? | Total de Viagens, Distância Total, MPG Médio Ponderado, Tempo Ocioso Total. | Cards, linha por mês, ranking de caminhões, barras por status. | Período, caminhão, status da viagem, rota. | Nulos em `truck_id`; eficiência não prova causa. |
| Entregas e Eventos | Acompanhar eventos, pontualidade e detenção. | Quantos eventos ocorreram e qual a taxa de pontualidade? | Taxa de Pontualidade, Detenção Total, Detenção Média por Evento. | Barras por tipo de evento, linha temporal, ranking de estados/cidades. | Período, tipo de evento, cidade, estado. | `on_time_flag` exige validação antes de virar SLA oficial. |
| Combustível e Custos | Analisar abastecimentos e custo unitário. | Quanto foi gasto, quantos galões foram comprados e qual preço médio? | Custo Total de Combustível, Galões Comprados, Preço Médio Ponderado por Galão. | Cards, linha temporal, ranking por caminhão, barras por estado/local. | Período, caminhão, estado, cidade. | Compras podem não coincidir com consumo no mesmo período. |
| Qualidade dos Dados | Dar transparência às limitações. | Onde há nulos e campos com risco de agregação? | Registros sem Caminhão Informado, % Registros sem Caminhão Informado. | Cards de qualidade, tabela de campos críticos, barras por tabela/campo. | Tabela, campo, período. | Qualidade de dados não deve ser confundida com desempenho operacional. |

## 13. Boas práticas Power BI aplicadas

* Usar modelo estrela ou estrela adaptado.
* Usar `dim_calendario` como tabela calendário central.
* Criar medidas explícitas em vez de arrastar campos numéricos diretamente.
* Evitar agregações automáticas perigosas.
* Documentar medidas, fórmulas e limitações.
* Usar nomes amigáveis para tabelas, colunas e medidas.
* Manter direção de filtro simples sempre que possível.
* Evitar relacionamento bidirecional sem justificativa explícita.
* Separar métricas de negócio de indicadores de qualidade de dados.
* Preservar nulos operacionais e reportar seu impacto.
* Submeter decisões de KPIs e relações ambíguas à validação humana.

## 14. Riscos e limitações

* Nulos operacionais em `driver_id`, `truck_id` e `trailer_id` podem afetar análises por motorista, caminhão e trailer.
* `average_mpg`, `price_per_gallon`, `base_rate_per_mile` e `fuel_surcharge_rate` são campos não aditivos e não devem ser somados.
* Relacionamentos fato-fato podem criar ambiguidade e devem ser usados com cautela.
* Não há metas oficiais, portanto KPIs ainda são métricas candidatas.
* Não há campos completos para lucro, margem ou rentabilidade.
* Não há dimensão de motoristas.
* Não há regra oficial de SLA, apenas métrica candidata baseada em `on_time_flag`.
* Correlação entre cliente, rota, caminhão, custo e eficiência não deve ser interpretada como causalidade.
* Percentuais e taxas não devem ser transformados sem confirmação da escala.

## 15. Checklist para construção manual no Power BI

1. Importar os 8 arquivos de `dados/finais/`.
2. Renomear tabelas removendo `.csv`, se necessário.
3. Conferir tipos de dados: datas, números, textos e flags.
4. Marcar `dim_calendario` como tabela de datas, usando `data`.
5. Criar relacionamentos dimensão-fato principais com direção simples.
6. Criar relacionamentos de calendário com as datas principais das fatos.
7. Avaliar relações inativas para datas alternativas, especialmente `actual_datetime`.
8. Avaliar relacionamentos fato-fato somente quando necessários para medidas específicas.
9. Criar uma tabela organizadora de medidas, chamada `Medidas`.
10. Criar primeiro as medidas prioritárias da V1.
11. Configurar formatos de moeda, percentual, inteiro, decimal e unidades.
12. Ocultar chaves técnicas do painel de campos quando não forem úteis ao usuário final.
13. Conferir se campos não aditivos não estão sendo somados automaticamente.
14. Criar página de Qualidade dos Dados antes ou junto das páginas analíticas.
15. Montar páginas do dashboard conforme a especificação da Etapa 08.
16. Validar totais principais contra os CSVs finais ou relatórios anteriores.
17. Registrar decisões humanas sobre SLA, metas, filtros, nulos e relações opcionais.
18. Só depois disso avançar para refinamento visual e narrativa do dashboard.

## 16. Recomendação para avanço

O projeto pode avançar para construção manual do dashboard no Power BI.

Recomendação objetiva: avançar com uma V1 enxuta, usando modelo estrela adaptado, filtros simples, tabela calendário, medidas explícitas e as medidas prioritárias documentadas nesta etapa. Indicadores de lucro, margem, SLA oficial, eficiência por motorista, forecast e causalidade devem permanecer fora da V1 até validação humana e regras de negócio adicionais.

## 17. Decisão da Etapa 08

<!-- INICIO_VALIDACAO_HUMANA -->
Status da Etapa 08:

* [ ] Aprovada
* [x] Aprovada com ressalvas
* [ ] Reprovada para avanço

Observações da validação humana:

* A Etapa 08 está aprovada como especificação documental do modelo Power BI e das medidas DAX candidatas.
* A etapa não alterou dados brutos, tratados ou finais, não criou CSVs, não criou dashboard, não criou arquivo `.pbix` e não executou o Power BI.
* O relatório documentou o modelo estrela adaptado, as tabelas fato, dimensões, dimensão calendário, relacionamentos recomendados, medidas prioritárias da V1, formatações, páginas sugeridas e checklist de construção manual.
* As ressalvas principais para avanço são: validar no Power BI os tipos de dados importados, especialmente datas e `on_time_flag`; evitar relacionamento bidirecional; usar relacionamentos fato-fato apenas quando necessário; e garantir que campos não aditivos não sejam somados automaticamente.
* As medidas propostas devem ser tratadas como candidatas até validação manual no Power BI.
* A próxima etapa pode avançar para construção manual do dashboard no Power BI, começando por uma V1 enxuta, com medidas explícitas, tabela calendário, filtros simples e validação dos totais principais.

<!-- FIM_VALIDACAO_HUMANA -->

## 18. Confirmações finais

* A Etapa 08 foi criada como documentação de especificação do modelo Power BI.
* Dados brutos não foram alterados.
* Dados tratados não foram alterados.
* Dados finais não foram alterados.
* Nenhum CSV foi criado.
* Nenhum dashboard foi criado.
* Nenhum arquivo `.pbix` foi criado.
* O Power BI não foi executado.
* Nenhum campo inexistente foi usado nas medidas candidatas.
* Medidas foram propostas apenas com base nos dados finais disponíveis.
* Percentuais e taxas foram documentados com cautela, sem transformação de escala.
* O projeto pode avançar para construção manual do dashboard no Power BI.
