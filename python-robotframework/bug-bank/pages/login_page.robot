*** Keywords ***
Fazer Login
    [Arguments]    ${email}    ${senha}
    Click Link    Signup / Login
    Input Text    css=input[data-qa="login-email"]    ${email}
    Input Text    css=input[placeholder="Password"]    ${senha}
    Click Button    Login

Verificar Login Sucesso
    Page Should Contain Element    css=a[href="/logout"]
    Page Should Contain    Logged in as
