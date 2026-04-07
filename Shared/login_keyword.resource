*** Settings ***
Library    SeleniumLibrary
Resource    ../Projects/Login/pages/login_with_password_page.robot

*** Variables ***


*** Keywords ***
Login To Application
    [Arguments]    ${username}    ${password}

    Enter Username    ${username}
    Enter Password    ${password}
    Click Login Button
    Check Login Success