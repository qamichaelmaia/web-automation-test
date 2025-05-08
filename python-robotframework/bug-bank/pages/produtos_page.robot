*** Keywords ***
Buscar Produto
    [Arguments]    ${produto}
    Click Link    Products
    Page Should Contain    All Products
    Input Text    id=search_product    ${produto}
    Click Button    id=submit_search

Verificar Produto Encontrado
    [Arguments]    ${produto}
    Page Should Contain    Searched Products
    Page Should Contain    ${produto}
