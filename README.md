# Pipeline ETL — Barbearia

Pipeline de análise de dados de uma barbearia, desenvolvido em Python.
Projeto acadêmico para prática de Python, Pandas, SQL e Git.

## Tecnologias utilizadas
- Python 3.13
- Pandas
- SQLite3
- Git / GitHub

## O que o projeto faz
1. Extrai dados de atendimentos de um arquivo CSV
2. Limpa e padroniza os dados (remoção de nulos, padronização de texto, conversão de datas)
3. Analisa os dados: total por serviço, por forma de pagamento e ranking de clientes
4. Carrega os dados num banco de dados SQLite
5. Consulta o banco com queries SQL
6. Exporta um relatório final em CSV

## Como executar
1. Instale as dependências: pip install pandas
2. Execute: python pipeline_barbearia.py

## Estrutura do projeto
- atendimentos.csv — dados brutos de entrada
- pipeline_barbearia.py — pipeline completo
- relatorio_final.csv — relatório gerado automaticamente