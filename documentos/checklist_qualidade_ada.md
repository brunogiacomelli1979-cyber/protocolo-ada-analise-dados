# Checklist de Qualidade do Protocolo ADA

## Antes de iniciar o projeto

* [ ] Objetivo inicial registrado.
* [ ] Escopo do projeto definido.
* [ ] Fonte dos dados identificada.
* [ ] Permissão de uso dos dados confirmada.
* [ ] Estrutura de pastas criada.
* [ ] Critérios mínimos de privacidade definidos.
* [ ] Responsável humano pela validação identificado.
* [ ] Repositório Git preparado.
* [ ] `.gitignore` revisado.

## Inspeção de dados

* [ ] Dados brutos preservados.
* [ ] Arquivos listados.
* [ ] Linhas e colunas registradas.
* [ ] Tipos de dados inspecionados.
* [ ] Amostras revisadas com cuidado.
* [ ] Campos sensíveis identificados.
* [ ] Chaves candidatas mapeadas.
* [ ] Nulos iniciais registrados.
* [ ] Duplicidades iniciais avaliadas.
* [ ] Limitações iniciais documentadas.

## Tratamento e padronização

* [ ] Plano de tratamento aprovado antes da execução.
* [ ] Dados brutos não alterados.
* [ ] Arquivos tratados criados em pasta separada.
* [ ] Nomes de colunas padronizados.
* [ ] Datas tratadas de forma consistente.
* [ ] Campos sensíveis removidos ou mascarados.
* [ ] Nulos não imputados sem regra de negócio.
* [ ] Outliers não removidos automaticamente.
* [ ] Transformações documentadas.
* [ ] Script reprodutível versionado.

## Validação de dados tratados

* [ ] Todos os arquivos tratados existem.
* [ ] Todos os arquivos tratados são legíveis.
* [ ] Contagem de linhas comparada com origem.
* [ ] Colunas esperadas validadas.
* [ ] Chaves principais verificadas.
* [ ] Duplicidades relevantes avaliadas.
* [ ] Nulos operacionais registrados.
* [ ] Relacionamentos candidatos testados.
* [ ] Campos sensíveis auditados.
* [ ] Relatório gerado com decisão humana preservável.

## Criação dos dados finais

* [ ] Dados finais criados apenas a partir de dados tratados aprovados.
* [ ] Tabelas fato definidas.
* [ ] Dimensões definidas.
* [ ] Dimensão calendário criada quando necessária.
* [ ] Campos sensíveis excluídos ou mantidos mascarados conforme decisão.
* [ ] Granularidade documentada.
* [ ] Colunas selecionadas com justificativa.
* [ ] Nenhum KPI complexo criado nesta etapa.
* [ ] Nenhum dashboard criado.

## Validação dos dados finais

* [ ] Todos os arquivos finais esperados existem.
* [ ] Todos os arquivos finais são legíveis.
* [ ] Linhas e colunas registradas.
* [ ] Chaves das dimensões são únicas.
* [ ] Chaves das fatos foram avaliadas.
* [ ] Relacionamentos esperados validados.
* [ ] Dimensão calendário validada.
* [ ] Campos sensíveis confirmados.
* [ ] Nulos operacionais registrados.
* [ ] Campos não aditivos sinalizados.
* [ ] Status OK/Atenção/Crítico consolidado.

## Definição de perguntas e KPIs

* [ ] Perguntas derivadas dos dados disponíveis.
* [ ] Métricas diferenciadas de KPIs.
* [ ] Dimensões de análise identificadas.
* [ ] Fórmulas conceituais documentadas.
* [ ] Granularidade registrada.
* [ ] Regras de agregação definidas.
* [ ] Campos não aditivos tratados com cuidado.
* [ ] KPIs sem base suficiente deixados fora do escopo.
* [ ] Risco de correlação versus causalidade registrado.
* [ ] Validação humana prevista.

## Especificação Power BI

* [ ] Tabelas a importar listadas.
* [ ] Modelo estrela ou estrela adaptado definido.
* [ ] Relacionamentos dimensão-fato especificados.
* [ ] Relacionamentos fato-fato tratados com cautela.
* [ ] Direção de filtro simples priorizada.
* [ ] Tabela calendário especificada.
* [ ] Medidas DAX candidatas documentadas.
* [ ] Formatos recomendados definidos.
* [ ] Campos técnicos e sensíveis sinalizados.
* [ ] Páginas do dashboard especificadas.

## Segurança e privacidade

* [ ] Dados sensíveis identificados.
* [ ] Campos sensíveis removidos ou mascarados.
* [ ] Dados privados não expostos em relatórios públicos.
* [ ] Prompts privados de agente não documentados.
* [ ] Arquivos sensíveis protegidos por `.gitignore`.
* [ ] Acesso aos dados restrito quando necessário.
* [ ] Decisões de privacidade registradas.

## Documentação e Git

* [ ] Scripts versionados.
* [ ] Relatórios versionados.
* [ ] Dados brutos protegidos quando necessário.
* [ ] Commits revisados antes de envio.
* [ ] Mudanças não relacionadas evitadas.
* [ ] Relatórios preservam validação humana ao serem regenerados.
* [ ] README ou documentação principal atualizada quando necessário.

## Validação humana

* [ ] Decisões humanas registradas.
* [ ] Aprovação, aprovação com ressalvas ou reprovação indicada.
* [ ] Ressalvas documentadas.
* [ ] Limitações aceitas explicitamente.
* [ ] IA não apresentada como decisora.
* [ ] Próximos passos aprovados pelo responsável.

## Finalização do projeto

* [ ] Entregas finais listadas.
* [ ] Limitações finais registradas.
* [ ] Reprodutibilidade verificada.
* [ ] Artefatos sensíveis revisados.
* [ ] Métricas e dashboards validados por humano.
* [ ] Recomendações finais documentadas.
* [ ] Possíveis evoluções registradas.
