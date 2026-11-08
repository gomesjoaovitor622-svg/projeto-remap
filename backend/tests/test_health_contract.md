# Contrato inicial dos health checks

Este documento registra os testes de aceite para a primeira execução local da API.

1. GET /health/live deve retornar HTTP 200 e {"status":"alive"} sem depender do PostgreSQL.
2. GET /health/ready deve retornar HTTP 200 quando SELECT 1 funcionar no PostgreSQL.
3. GET /health/ready deve retornar HTTP 503 quando o banco estiver indisponível.
4. A porta da API no Compose está vinculada a 127.0.0.1 para evitar exposição pública acidental durante desenvolvimento.

Os testes automatizados executáveis serão adicionados junto com a configuração de pytest na próxima etapa. Este contrato ainda não representa testes executados.
