# Requisitos — usuários, organizações e permissões

## Hierarquia
### Superusuário global
Administra organizações, contas, perfis, permissões e auditoria global. Deve ser criado por bootstrap seguro, sem senha fixa no código.

### Administrador de oficina
Administra somente a própria organização e seus membros conforme permissões. Não pode criar superusuário nem acessar outras oficinas.

### Funcionários e técnicos
Acessam somente módulos e ações autorizados.

## Autorização
Adotar RBAC com permissões granulares e exceções individuais quando necessário. Negar por padrão e validar cada operação no backend.

Permissões iniciais sugeridas:
- dashboard.view
- customers.view/create/edit/delete
- vehicles.view/create/edit/delete
- ecu.view/manage
- diagnostics.view/create/edit
- remap.view/execute
- files.upload/download/delete
- reports.view/generate/export
- users.view/create/edit/block
- permissions.view/manage
- audit.view
- settings.view/manage

## Isolamento multiempresa
Toda entidade de oficina deve estar vinculada à organização. Consultas, downloads, relatórios e sincronizações devem verificar o vínculo do usuário. Avaliar Row-Level Security do PostgreSQL como defesa adicional.

## Matriz inicial
| Perfil | Clientes | Veículos | Diagnóstico | Remap | Usuários |
|---|---|---|---|---|---|
| Recepção | Criar/editar | Criar/editar | Não | Não | Não |
| Técnico | Consultar | Consultar/editar | Executar | Conforme autorização | Não |
| Especialista | Consultar | Consultar | Consultar | Conforme autorização | Não |
| Admin oficina | Gerenciar oficina | Gerenciar oficina | Gerenciar oficina | Conforme autorização | Gerenciar equipe |
| Superusuário | Global | Global | Global | Global | Global |

A matriz é um exemplo configurável, não uma regra fixa.

## Testes de aceite
- Acesso sem permissão é negado pela API.
- Oficina A não acessa dados da Oficina B.
- Admin de oficina não cria superusuário.
- Revogação de acesso é aplicada no backend.
- Mudanças administrativas são auditadas.