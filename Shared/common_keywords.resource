*** Settings ***
Library    SeleniumLibrary

Resource    ./browser_keywords.resource
Resource    ./login_keyword.resource

*** Variables ***


*** Keywords ***
Open Browser and Login Application
    [Arguments]    ${username}    ${password}

    Open Browser To Application
    Login To Application    ${username}    ${password}