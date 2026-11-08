# Prompt mestre — auditoria, melhoria e evolução contínua do REMAP

Leia AGENTS.md, README.md e toda a documentação antes de iniciar. Examine o repositório real e não assuma que funcionalidades planejadas já existem.

## Missão
Auditar, corrigir, refatorar e melhorar a implementação existente sem reescrever tudo do zero e sem remover funcionalidades que funcionam.

## Auditoria
- Mapear estrutura, dependências, versões e fluxos.
- Identificar código duplicado, erros, vulnerabilidades, consultas lentas, falhas de validação e componentes incompletos.
- Executar testes existentes antes de alterar.
- Registrar achados por severidade, evidência, impacto e recomendação.

## Melhorias obrigatórias
1. UX moderna, responsiva, acessível, com tema claro/escuro e feedback de carregamento, sucesso e erro.
2. Dashboard com dados reais e filtros.
3. Superusuário global, gestão de usuários/oficinas e permissões granulares.
4. Autorização em todos os endpoints e isolamento multiempresa.
5. PostgreSQL: migrations, constraints, índices, transações, integridade e backup/restauração.
6. API: validação, paginação, erros padronizados, logs, limites de upload e versionamento.
7. Flutter: arquitetura modular, rotas, estado, tratamento de erros e testes.
8. Offline: persistência local, fila idempotente, sincronização retomável e resolução explícita de conflitos.
9. Remapeamento: arquivos originais imutáveis, SHA-256, metadados, versões, permissões e auditoria.
10. Diagnóstico: diferenciar dados manuais, demonstração e dados reais.
11. Equipamentos: adaptadores documentados e testes com hardware real.
12. Segurança: MFA administrativo, sessões revogáveis, segredos fora do Git, rate limiting e proteção de arquivos.
13. Infraestrutura: Docker, HTTPS, logs, monitoramento, backups e rollback.
14. CI: análise estática, testes backend/Flutter, migrations e builds.
15. Documentação: atualizar manuais para refletir o comportamento real.

## Regras de segurança
Não simular operações de ECU. Não inventar compatibilidades ou resultados. Não gravar em ECU sem equipamento, protocolo validado, confirmação e plano de recuperação. Não expor dados de uma oficina para outra. Não commitar credenciais.

## Processo
1. Fazer backup e registrar branch/commit inicial.
2. Rodar testes e capturar estado inicial.
3. Criar plano priorizado.
4. Corrigir primeiro problemas críticos.
5. Implementar melhorias pequenas e reversíveis.
6. Executar testes de regressão após cada etapa.
7. Atualizar documentação e changelog.
8. Commitar em branch própria e abrir PR quando apropriado.

## Relatório
Listar achados, severidade, correções, arquivos alterados, testes e resultados reais, riscos remanescentes e próximos passos. Nunca afirmar que tudo está perfeito sem evidência.