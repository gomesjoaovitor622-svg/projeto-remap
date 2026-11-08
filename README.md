# REMAP — Gestão, diagnóstico e remapeamento automotivo

Plataforma em planejamento para oficinas e profissionais automotivos.

> **Estado atual:** este repositório está sendo inicializado. As funcionalidades descritas são requisitos planejados, não recursos já implementados ou testados.

## Objetivos
- Flutter para Android, Web e computador compatível.
- Backend FastAPI e API REST.
- PostgreSQL como banco central.
- Superusuário global e permissões granulares.
- Multiusuário e multiempresa com isolamento de dados.
- Operação offline e sincronização posterior.
- Gestão de clientes, veículos, ECUs, diagnósticos e arquivos de calibração.
- Integrações automotivas desenvolvidas progressivamente e validadas com equipamentos reais.

## Documentação
- [Plano de desenvolvimento](docs/PLANO_DE_DESENVOLVIMENTO.md)
- [Manual do usuário](docs/MANUAL_USUARIO.md)
- [Manual do administrador](docs/MANUAL_ADMINISTRADOR.md)
- [Requisitos e permissões](docs/REQUISITOS_E_PERMISSOES.md)
- [Segurança automotiva](docs/SEGURANCA_E_OPERACAO_AUTOMOTIVA.md)
- [Infraestrutura e deploy](docs/INFRAESTRUTURA_E_DEPLOY.md)

## Regras
1. Não declarar como funcional algo que não foi implementado e testado.
2. Não simular comunicação real com ECU, OBD-II, CAN, K-Line ou J2534.
3. Preservar arquivos originais e registrar alterações.
4. Validar permissões no backend.
5. Isolar os dados de cada oficina.
6. Não versionar segredos, tokens ou credenciais.
7. Fazer backup antes de operações destrutivas e testar restauração.

## Tecnologias propostas
Flutter/Dart, FastAPI, PostgreSQL, SQLAlchemy, Alembic, Docker, Nginx e GitHub Actions. A arquitetura será confirmada na fase de planejamento.

## Licença
A licença ainda precisa ser definida pelo proprietário. Não presuma autorização de redistribuição enquanto não houver uma licença escolhida.