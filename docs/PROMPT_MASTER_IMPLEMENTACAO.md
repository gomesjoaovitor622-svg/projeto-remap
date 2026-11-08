# Prompt mestre — implementação inicial do REMAP

Atue como equipe sênior de arquitetura, Flutter, backend, PostgreSQL, segurança, DevOps e tecnologia automotiva.

Repositório: https://github.com/gomesjoaovitor622-svg/projeto-remap

Leia primeiro README.md, AGENTS.md e toda a documentação em docs/. O repositório pode conter apenas planejamento; verifique antes de afirmar que há código.

## Objetivo
Construir uma plataforma profissional de gestão, diagnóstico e remapeamento automotivo, multiusuário e multiempresa, com superusuário global, permissões granulares, modo offline e sincronização.

## Requisitos
1. Flutter/Dart para Android, Web e desktop quando suportado.
2. FastAPI com API REST.
3. PostgreSQL central, migrations versionadas e backups.
4. Superusuário global criado por bootstrap seguro, sem senha padrão fixa.
5. Usuários vinculados a organizações/oficinas.
6. RBAC com permissões por recurso e ação, validado no backend.
7. Isolamento de dados entre oficinas, com testes negativos.
8. Clientes, veículos, catálogo ECU, diagnósticos, arquivos de calibração, versões e relatórios.
9. Persistência local e operação offline em Android e computador, com fila idempotente e conflitos explícitos.
10. Docker Compose, Nginx, HTTPS e CI.
11. APK de testes, APK release e AAB, sem publicar credenciais de assinatura.
12. Documentação atualizada conforme a implementação real.

## Segurança automotiva
Preservar arquivos originais, calcular SHA-256, registrar metadados e histórico. Separar dados manuais, dados de demonstração e dados recebidos de equipamentos reais. Não inventar compatibilidade, protocolo, checksum ou resultado. Implementar comunicação OBD-II/CAN/K-Line/J2534 por adaptadores independentes e somente com equipamentos/documentação disponíveis. Leitura e gravação real exigem validação técnica, autorização explícita e procedimento de recuperação comprovado.

## Método
Fase 1: auditoria do sistema de referência e levantamento de requisitos.
Fase 2: arquitetura, UX, modelo de dados e decisões técnicas.
Fase 3: backend, PostgreSQL e migrations.
Fase 4: autenticação, superusuário, RBAC e multiempresa.
Fase 5: Flutter e módulos de gestão.
Fase 6: arquivos, diagnósticos e remapeamento.
Fase 7: offline e sincronização.
Fase 8: integrações reais com equipamentos.
Fase 9: infraestrutura e hospedagem.
Fase 10: testes, builds, documentação e publicação.

## Hospedagem
Não escolher sem comparar servidor Ubuntu próprio, VPS e arquitetura híbrida em custo, disponibilidade, conectividade, segurança, manutenção e escalabilidade. Não contratar ou migrar sem autorização do proprietário.

## Critérios
Não criar telas estáticas como se fossem sistema pronto. Cada fluxo deve persistir dados, validar permissões, tratar erros e possuir testes. Não usar dados falsos em produção. Não destruir arquivos existentes. Fazer backup antes de mudanças destrutivas.

## Entrega
Ao final de cada fase, apresentar arquivos criados/modificados, decisões, comandos executados, testes e resultados, limitações e pendências. Atualizar README, docs e changelog. Fazer commits claros e abrir PR quando apropriado.