*** Settings ***
Library           SeleniumLibrary
Resource          pages/home_page.robot
Resource          pages/login_page.robot
Resource          pages/cadastro_page.robot
Resource          pages/produtos_page.robot

Suite Teardown    Fechar Navegador

*** Variables ***
${NOME}           João
${EMAIL}          joao.teste${random}@mail.com
${SENHA}          Senha123
${PRODUTO}        Blue Top

*** Test Cases ***
Cadastro, Login e Busca de Produto
    #${random}=    Generate Random String    4    [LOWER]
    Abrir Homepage
    Cadastrar Novo Usuário    ${NOME}    ${EMAIL}    ${SENHA}
    Verificar Conta Criada
    Logout
    Fazer Login    ${EMAIL}    ${SENHA}
    Verificar Login Sucesso
    Buscar Produto    ${PRODUTO}
    Verificar Produto Encontrado    ${PRODUTO}
