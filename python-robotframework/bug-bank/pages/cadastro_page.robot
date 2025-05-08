*** Keywords ***
Cadastrar Novo Usuário
    [Arguments]    ${nome}    ${email}    ${senha}
    Click Link    Signup / Login
    Input Text    css=input[data-qa="signup-name"]    ${nome}
    Input Text    css=input[data-qa="signup-email"]    ${email}
    Click Button    Signup

    Click Element    id=id_gender1
    Input Text    id=password    ${senha}
    Select From List By Value    id=days    10
    Select From List By Value    id=months    6
    Select From List By Value    id=years    1990
    Click Element    id=newsletter
    Click Element    id=optin
    Input Text    id=first_name    ${nome}
    Input Text    id=last_name    Silva
    Input Text    id=company    TestCompany
    Input Text    id=address1    Rua Principal 123
    Input Text    id=address2    Apt 4
    Select From List By Label    id=country    Brazil
    Input Text    id=state    SP
    Input Text    id=city    São Paulo
    Input Text    id=zipcode    12345
    Input Text    id=mobile_number    11999999999
    Click Button    Create Account

Verificar Conta Criada
    Page Should Contain    ACCOUNT CREATED!
    Click Link    Continue
    Page Should Contain    Logged in as

Logout
    Click Link    Logout
