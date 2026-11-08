# Segurança e operação automotiva

## Princípio
Distinguir gestão de arquivos, análise offline, diagnóstico real e comunicação física com módulos eletrônicos. Simulações nunca podem ser apresentadas como leituras ou gravações reais.

## Arquivos
- Preservar original.
- Calcular SHA-256 na importação.
- Registrar tamanho, formato, origem, autor e data.
- Manter histórico de versões.
- Restringir download por organização e permissão.
- Validar uploads e limitar tamanho.
- Nunca executar arquivos recebidos.

## Equipamentos
Integrações OBD-II, CAN, K-Line e J2534 devem usar adaptadores independentes e documentar equipamento, firmware, protocolo, veículo/ECU testados e limitações.

## Leitura e gravação
Antes de implementar gravação: confirmar compatibilidade, validar arquivo, preservar original quando suportado, exigir confirmação, registrar usuário/equipamento/ECU/arquivo/resultado e documentar recuperação apenas quando comprovada. Não emitir comandos destrutivos sem documentação e testes controlados.

## Segurança da aplicação
Menor privilégio, autorização no servidor, segredos fora do Git, HTTPS, hash seguro de senhas, expiração e revogação de tokens, MFA administrativo, rate limiting, validação de entradas e uploads, logs sem credenciais e isolamento multiempresa.

## Incidentes
Registrar ambiente, data, usuário afetado, ação, mensagem e impacto. Nunca anexar senhas, tokens ou chaves.