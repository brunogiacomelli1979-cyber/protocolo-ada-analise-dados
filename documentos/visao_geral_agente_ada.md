# Visão Geral do Agente ADA

O Agente ADA é um assistente de apoio para projetos de análise de dados. Ele faz parte do Protocolo ADA - Análise de Dados Assistida por IA - e tem como função ajudar na organização, documentação, revisão e condução segura de etapas analíticas.

Este documento é público e não revela prompts internos, regras privadas de decisão ou templates sensíveis do agente.

## Qual problema ele resolve

O Agente ADA ajuda a reduzir improvisos em projetos de dados, especialmente quando há risco de alteração indevida dos dados brutos, perda de rastreabilidade, criação de métricas sem validação ou exposição de informações sensíveis.

Ele também apoia a separação entre preparação técnica dos dados, análise, visualização e decisões humanas.

## Etapas que ele apoia

- planejamento analítico;
- avaliação de privacidade, LGPD e risco;
- inspeção inicial dos dados;
- documentação de problemas encontrados;
- proposta de tratamento e padronização;
- validação dos dados preparados;
- estruturação de métricas e KPIs, quando aprovados;
- preparação de relatórios e materiais de apoio;
- revisão e melhoria contínua do processo.

## Decisões que exigem validação humana

Exigem validação humana decisões que possam afetar dados, pessoas, negócio, conformidade ou interpretação dos resultados.

Isso inclui:

- excluir, alterar ou consolidar registros;
- tratar valores ausentes, duplicados ou inconsistentes;
- definir métricas, KPIs e regras de cálculo;
- alterar regras de negócio;
- usar dados pessoais ou sensíveis;
- publicar relatórios, dashboards ou conclusões;
- tomar decisões com impacto operacional, financeiro, legal ou reputacional.

## O que o agente não pode fazer sozinho

O agente não pode analisar dados reais, aplicar transformações críticas, criar KPIs, gerar conclusões, publicar resultados ou tomar decisões sensíveis sem validação humana.

Antes de uma alteração crítica, ele deve apresentar o problema, a proposta, o impacto esperado, um exemplo de antes/depois quando aplicável e solicitar aprovação explícita.

## Redução de risco de distorção dos dados

O Agente ADA ajuda a reduzir distorções ao reforçar que os dados brutos nunca devem ser alterados, que tratamentos devem ser documentados e que mudanças relevantes precisam de validação.

Ele também incentiva a separação entre dados brutos, dados tratados e dados finais, além do registro de decisões e riscos.

## Privacidade, LGPD e ambientes de IA

O agente considera privacidade e LGPD como parte do processo de análise. Isso inclui atenção a dados pessoais, dados sensíveis, minimização de dados, controle de acesso e risco de exposição em ferramentas de IA.

Informações confidenciais, bases reais e materiais sensíveis não devem ser enviados a ambientes de IA sem avaliação prévia, autorização adequada e medidas de proteção.

## Partes mantidas privadas

São mantidos privados:

- prompts internos;
- regras detalhadas de decisão;
- templates sensíveis;
- exemplos confidenciais;
- materiais de treinamento interno;
- dados brutos, tratados ou finais com informações sensíveis;
- documentos operacionais que possam expor critérios internos do agente.

Esses materiais devem permanecer na pasta `agente_privado/` ou em ambientes controlados, sem publicação em repositórios públicos.
