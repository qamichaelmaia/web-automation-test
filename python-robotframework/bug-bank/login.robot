*** Settings ***
Library         SeleniumLibrary

*** Variables ***
${URL}          https://bugbank.netlify.app
${EMAIL}        qamichael@test.com
${PASSWORD}     test@testqa

*** Test Cases ***
Login com credenciais válidas
    Open Browser    ${URL}    chrome
    Input Text      id:email     ${EMAIL}
    Input Text      id:password  ${PASSWORD}
    Click Button    Acessar
    Page Should Contain    Sair

    Close Browser
