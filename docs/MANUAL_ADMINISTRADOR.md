# Manual inicial do administrador — REMAP

> Procedimentos previstos; atualizar após implementação e validação das telas reais.

## 1. Superusuário
A conta global deve ser criada por procedimento de bootstrap seguro, com segredo fornecido fora do código. Não utilizar senha padrão fixa nem permitir que usuários comuns promovam a si mesmos.

## 2. Criar oficina
Acesse Administração > Oficinas, crie a organização, informe os dados, associe o administrador responsável e confira o isolamento dos registros.

## 3. Criar usuário
Acesse Administração > Usuários, informe nome e e-mail, associe a oficina, atribua perfil inicial, revise permissões e envie convite ou instrução segura de ativação.

## 4. Configurar permissões
Abra o usuário ou perfil, habilite somente as ações necessárias, salve e teste com uma conta de teste. A API deve validar as permissões mesmo se a interface ocultar o módulo.

## 5. Bloquear acesso
Bloqueie a conta, revogue sessões e tokens, revise atividades recentes e preserve a auditoria.

## 6. Auditoria
Acompanhe criação de usuários, mudanças de permissões, exclusões, downloads e operações críticas.

## 7. Backup
Mantenha cópias criptografadas em local separado, defina frequência e retenção e teste restauração. Backup não é considerado válido sem restauração testada.

## 8. Atualizações
Leia o changelog, faça backup, teste migrations em homologação, atualize serviços, execute testes de saúde e mantenha plano de rollback.

## 9. Operações de ECU
Não autorize gravação real sem equipamento compatível, protocolo documentado, validação de integridade e procedimento de recuperação comprovado.