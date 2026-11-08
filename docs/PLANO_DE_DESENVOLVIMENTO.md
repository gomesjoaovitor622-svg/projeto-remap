# Plano de desenvolvimento — REMAP

## Estado inicial
O repositório está sendo inicializado. Não há aplicação funcional confirmada neste momento.

## Requisitos aprovados
- Escopo: gestão, diagnóstico e ferramentas de remapeamento.
- ECUs: objetivo de suportar gestão, comunicação e leitura/gravação real em etapas.
- Hospedagem: comparar servidor Ubuntu próprio, VPS e arquitetura híbrida antes de decidir.
- Multiusuário e multiempresa.
- Superusuário global que cria usuários e configura permissões granulares.
- Offline em Android e computador, com sincronização posterior.
- Interface moderna e tecnológica.

## Arquitetura proposta
- Flutter/Dart para Android, Web e desktop conforme viabilidade.
- FastAPI para API REST e regras de negócio.
- PostgreSQL para banco central.
- SQLAlchemy e Alembic para persistência e migrations.
- Persistência local para uso offline, tecnologia a selecionar após validar requisitos.
- Docker Compose, Nginx e GitHub Actions.

O Flutter não acessará PostgreSQL diretamente.

## Fases de execução
1. Descoberta: auditar sistema de referência e fechar requisitos.
2. Arquitetura: diagramas, modelo de dados, UX, segurança e sincronização.
3. Fundação: backend, banco, migrations, logs e testes.
4. Identidade: bootstrap do superusuário, organizações, usuários e permissões.
5. Aplicação: dashboard, clientes, veículos e ECUs.
6. Operação: arquivos, diagnósticos, histórico e relatórios.
7. Offline: banco local, fila, idempotência e resolução de conflitos.
8. Integrações: equipamentos reais e protocolos documentados.
9. Infraestrutura: hospedagem, HTTPS, backups e monitoramento.
10. Entrega: APK, AAB, Web, documentação e validação.

## Critérios de aceite
- Testes de autorização e isolamento multiempresa.
- Migrations reproduzíveis.
- Backup e restauração testados.
- Dados simulados claramente identificados.
- Integrações ECU comprovadas com equipamento real.
- Builds executados e artefatos verificados.
- Documentação coerente com a implementação.

## Decisões pendentes
Hospedagem definitiva, equipamentos disponíveis, marcas/protocolos prioritários, tecnologia offline, política de retenção, planos comerciais e licença do repositório.

## Relatório por fase
Registrar objetivo, arquivos modificados, decisões, comandos, testes e resultados reais, riscos, pendências e commit correspondente.