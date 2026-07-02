# Boas Práticas do Protocolo ADA

## Preservação e organização dos dados

* Preservar dados brutos sem alteração.
* Separar dados brutos, tratados e finais.
* Criar dados derivados somente em pastas apropriadas.
* Evitar sobrescrever arquivos sem necessidade.
* Documentar a origem e finalidade de cada arquivo.

## Tratamento responsável

* Não imputar nulos sem regra de negócio.
* Não remover outliers automaticamente.
* Não excluir registros apenas porque parecem incomuns.
* Registrar campos ausentes e valores inesperados.
* Tratar dados sensíveis com remoção, mascaramento ou restrição de uso.
* Diferenciar erro técnico de característica legítima do processo.

## Documentação de decisões

* Registrar decisões humanas em relatórios.
* Preservar validação humana em relatórios regenerados.
* Documentar por que uma regra foi aplicada.
* Documentar também o que não foi feito.
* Registrar limitações e riscos de interpretação.
* Evitar conclusões que os dados não sustentam.

## Métricas, KPIs e agregações

* Diferenciar métrica, KPI e dimensão.
* Tratar KPIs sem meta como métricas candidatas.
* Não somar médias.
* Não somar taxas.
* Não somar preços unitários.
* Usar razões de agregados para médias ponderadas.
* Confirmar escala antes de formatar percentuais.
* Separar indicadores de negócio de indicadores de qualidade dos dados.

## BI e modelagem

* Usar modelo estrela sempre que possível.
* Usar tabela calendário para análises temporais.
* Criar medidas explícitas no Power BI.
* Evitar arrastar campos numéricos diretamente para visuais sem medida.
* Evitar relacionamento bidirecional sem justificativa.
* Diferenciar relacionamento fato-dimensão e fato-fato.
* Documentar campos que devem ser ocultados.
* Validar totais principais antes de publicar dashboard.

## Segurança e privacidade

* Proteger dados sensíveis.
* Não expor prompts privados de agente.
* Não publicar dados privados sem autorização.
* Usar `.gitignore` para arquivos que não devem ser versionados.
* Remover ou mascarar identificadores quando não forem necessários.
* Registrar decisões de privacidade.

## Versionamento e reprodutibilidade

* Versionar scripts e relatórios.
* Manter scripts pequenos o suficiente para auditoria.
* Evitar alterações manuais não rastreadas em dados derivados.
* Validar antes de commitar.
* Conferir `git status` antes de finalizar.
* Separar mudanças de código, dados e documentação quando possível.

## Separação de responsabilidades

* Python gera evidências.
* IA interpreta hipóteses e organiza documentação.
* Humano valida decisões.
* A inspeção não deve tratar dados.
* A validação não deve alterar dados.
* A definição de KPIs não deve criar dashboard.
* A especificação BI não deve criar arquivo `.pbix`.

## Rastreabilidade

* Cada etapa deve declarar entradas e saídas.
* Cada relatório deve indicar limitações.
* Cada transformação deve ser reproduzível.
* Cada decisão relevante deve ter registro humano.
* Cada KPI deve apontar tabelas e campos de origem.

## Reconhecimento de limitações

* Correlação não implica causalidade.
* Dados completos não garantem regra de negócio correta.
* Métricas podem ser tecnicamente corretas e ainda assim mal interpretadas.
* Dashboards não substituem análise crítica.
* IA pode apoiar, mas não deve decidir sozinha.

## Resumo

As boas práticas do ADA existem para manter o projeto confiável, auditável e útil. Elas não eliminam a necessidade de julgamento humano; elas criam condições para que esse julgamento seja melhor informado.
