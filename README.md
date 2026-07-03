# SampaTransit - Análise em Tempo Real

Pipeline de dados e dashboard interativo para monitoramento da frota de ônibus de São Paulo (SPTrans).

## Arquitetura
* **Orquestração/ETL:** Mage.ai
* **Banco de Dados:** PostgreSQL
* **Processamento:** Pandas, PyArrow (camada Gold em Parquet)
* **Visualização:** Streamlit
* **Infraestrutura:** Docker & Docker Compose

## Como Executar

1. Clone o repositório e acesse a pasta:
   git clone <URL-DO-SEU-REPOSITORIO>
   cd sampa-transit-analysis

2. Suba os contêineres:
   docker-compose up -d --build

3. Acesse os serviços:
* **Dashboard (Streamlit):** http://localhost:8501
* **Orquestrador (Mage.ai):** http://localhost:6789
* **Banco (PostgreSQL):** localhost:5432

## Funcionalidades
* Ingestão contínua da API da SPTrans.
* Dashboard em tempo real com mapa, filtro por linha, cálculo de velocidade média e veículos ativos.
* Fuso horário ajustado automaticamente (America/Sao_Paulo).