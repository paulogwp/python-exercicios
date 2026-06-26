# language: pt
Funcionalidade: Gerenciamento de Projetos

  Cenário: Remover um projeto cadastrado com sucesso
    Dado que o usuário está logado no sistema e acessa a tela de projetos
    E possui um projeto ativo chamado "Projeto Terralab"
    Quando o usuário clicar no botão "Remove Project" desse projeto
    Então o projeto "Projeto Terralab" deve sumir da listagem de projetos