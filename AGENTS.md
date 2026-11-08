# Instruções para agentes de desenvolvimento — REMAP

## Antes de alterar
- Leia README.md e todos os documentos em docs/.
- Confirme o estado da branch e os arquivos existentes.
- Não presuma que requisitos planejados já estão implementados.
- Não sobrescreva ou apague dados, migrations, arquivos ou configurações sem backup e autorização.

## Requisitos obrigatórios
- Flutter/Dart para clientes.
- FastAPI para API, salvo decisão arquitetural documentada.
- PostgreSQL como banco central.
- Multiempresa com isolamento testado.
- Superusuário global criado por bootstrap seguro.
- Permissões granulares validadas no backend.
- Offline e sincronização com idempotência e tratamento explícito de conflitos.
- Arquivos originais de calibração preservados e identificados por hash.
- Integrações automotivas reais somente com equipamentos e protocolos documentados.

## Qualidade
- Faça alterações pequenas e reversíveis.
- Adicione ou atualize testes.
- Execute formatadores, análise estática e testes aplicáveis.
- Atualize documentação e changelog.
- Informe comandos executados e resultados reais.
- Nunca declare build, teste, publicação ou integração concluída sem evidência.

## Segurança
- Nunca commitar segredos, tokens, chaves ou .env real.
- Não colocar credenciais padrão no código.
- Não expor PostgreSQL diretamente à internet.
- Validar autorização no servidor.
- Não simular leitura/gravação real de ECU.

## Git
- Trabalhe em branch específica para mudanças relevantes.
- Use commits descritivos.
- Não force push.
- Não altere branch principal de forma destrutiva.
- Abra PR quando apropriado e descreva testes, riscos e limitações.