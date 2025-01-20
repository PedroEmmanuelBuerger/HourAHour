# HourAHour
HourAHour é um projeto desenvolvido visando fazer o registro das condições climaticas de hora a hora, podendo setar uma região, estado e pais.

## Funcionalidades
O projeto inclui as seguintes funcionalidades:
- Obtém informações climáticas em tempo real para Blumenau, SC, utilizando o serviço wttr.in.
- Cria e atualiza um arquivo de texto com o clima, a hora da execução e o local.
- Faz commits automáticos para um repositório Git a cada uma hora e diariamente às 08:00.
- Registra logs detalhados de cada operação em um arquivo commit_diario.log.
Lida com erros durante a execução, registrando mensagens no arquivo de log para análise posterior.

## O projeto foi desenvolvido utilizando as seguintes tecnologias:
- Python: Linguagem principal para desenvolvimento do projeto.
- wttr.in: API de clima para obter informações meteorológicas de Blumenau.
- schedule: Biblioteca para agendamento de tarefas recorrentes.
- subprocess: Utilizada para integração com comandos do Git.
- requests: Biblioteca para realizar chamadas HTTP para a API de clima.

## Principais Aprendizados
Os principais aprendizados incluem:
- Automatizar o envio de contribuições para um repositório Git, reduzindo a necessidade de ações manuais.
- Utilizar APIs públicas para obter informações externas (como clima) e integrá-las ao fluxo de trabalho.
- Configurar e gerenciar tarefas recorrentes com a biblioteca schedule.
Registrar eventos e mensagens de erro em logs persistentes para facilitar a análise e depuração.
- Aplicar boas práticas de codificação em Python, incluindo manuseio de encoding para evitar problemas com caracteres Unicode.

## Conclusão
Commit Diário Automático é uma ferramenta prática para automatizar a criação de commits em um repositório Git, registrando informações de clima em tempo real. O projeto destaca conceitos importantes de automação, integração com APIs, gerenciamento de logs e agendamento de tarefas, proporcionando uma solução eficiente e confiável para manter um histórico atualizado no Git.
