# Status do Projeto REMAP

## Estado atual verificado
- Repositório: https://github.com/gomesjoaovitor622-svg/projeto-remap
- PR #1: https://github.com/gomesjoaovitor622-svg/projeto-remap/pull/1 (branch de trabalho; não integrado à main).
- CI da branch está sendo executado após as alterações mais recentes. Consulte os resultados em Actions antes de considerar a etapa aprovada.

## Implementado na branch feat/database-auth-foundation
- API FastAPI e health checks.
- PostgreSQL 16 via Docker Compose, sem publicar a porta do banco na internet.
- Alembic e migration inicial de organizações, usuários, papéis, permissões e associações RBAC.
- Autenticação inicial por e-mail/senha, hash Argon2 e JWT de acesso.
- Login de empresa exige identificador (slug); login global sem empresa fica reservado ao superusuário global.
- Verificação do vínculo empresa presente no token contra o usuário carregado no banco; empresa inativa bloqueia acesso.
- Comando local interativo para criar o primeiro superusuário, sem senha padrão.
- Proteção da chave JWT padrão em ambiente production.
- App Flutter inicial com tela de login, campo de empresa, token no armazenamento seguro e tela inicial autenticada.
- CI separado para backend/PostgreSQL/migration e Flutter analyze/test.

## Limitações e pendências importantes
- CI completo da versão mais recente ainda precisa terminar e passar.
- Migration precisa ser verificada em execução real no PostgreSQL pelo job de CI.
- Autenticação ainda não tem refresh token, revogação de sessão, recuperação de senha, MFA ou limitação de tentativas.
- O endpoint de autorização global é apenas uma verificação inicial; faltam CRUDs administrativos, criação de empresas/usuários e matriz RBAC aplicada a cada rota.
- O isolamento multiempresa foi iniciado na autenticação/token, mas precisa ser aplicado e testado em todos os recursos de negócio antes de armazenar dados reais.
- O app Flutter é um esqueleto de login; ainda não tem módulos de veículos, ECU, leitura/gravação, sincronização offline, armazenamento local de dados nem build APK/AAB validado.
- Nenhuma integração ECU/OBD/CAN/K-Line/J2534 foi testada em hardware real.
- Não há implantação pública, domínio, TLS, backup restaurável ou monitoramento de produção.

## Próximas etapas
1. Corrigir eventuais falhas do CI e validar migration PostgreSQL.
2. Testar login e autorização com PostgreSQL real e usuários de duas empresas.
3. Implementar administração de empresas, usuários, papéis e permissões.
4. Aplicar isolamento multiempresa a clientes, veículos, ECUs, arquivos e operações.
5. Completar Flutter, sessões, navegação, testes e builds Android.
6. Projetar offline-first e sincronização com resolução de conflitos.
7. Implementar módulos automotivos apenas com protocolos, adaptadores e equipamentos compatíveis e testados.
8. Planejar deploy, TLS, backups e observabilidade antes de uso público.
