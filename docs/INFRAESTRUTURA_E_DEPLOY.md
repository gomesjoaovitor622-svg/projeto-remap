# Infraestrutura, hospedagem e implantação

## Hospedagem ainda não decidida

### Servidor Ubuntu próprio
Pode aproveitar hardware existente, mas exige avaliar energia, internet, IP público/CGNAT, disponibilidade, segurança física, manutenção e redundância.

### VPS
Facilita conectividade e disponibilidade, mas gera custo recorrente e dependência do provedor.

### Híbrida
Pode hospedar API e PostgreSQL em VPS e manter cópias/arquivos no servidor próprio. Exige sincronização e backup seguros.

A decisão deverá considerar volume de arquivos, usuários simultâneos, disponibilidade e orçamento.

## Componentes previstos
FastAPI, PostgreSQL, Nginx, Flutter Web, armazenamento persistente, backups, logs e monitoramento.

## Segurança
HTTPS obrigatório em produção, firewall restritivo, PostgreSQL sem exposição pública direta, usuário de banco com privilégio mínimo, segredos fora do Git e backups externos criptografados.

## Docker
A configuração definitiva deverá incluir health checks, volumes persistentes, rede interna, limites de recursos e política de reinicialização. Não usar credenciais de exemplo em produção.

## Backup
Definir frequência, retenção, local secundário, criptografia, responsável, procedimento de restauração e testes periódicos. Banco e arquivos precisam de estratégia coordenada.

## Android
Gerar APK para testes e AAB para distribuição. Proteger a chave de assinatura fora do repositório. Validar requisitos vigentes da Play Store antes da publicação.

## Critérios de produção
Não declarar produção pronta até validar domínio, HTTPS, autenticação, isolamento multiempresa, persistência, backup/restauração, monitoramento, rollback e testes proporcionais ao uso.