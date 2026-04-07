*** Settings ***
Library    SeleniumLibrary

Resource    ../../../Shared/common_keywords.resource
Resource    ../../../Shared/service_keywords.resource

*** Variables ***


*** Keywords ***

Login and Goto Bijib PMS
    [Arguments]    ${username}    ${password}    ${hospital_name}=${EMPTY}

    Open Browser and Login Application    ${username}    ${password}
    Go To Service    Bijib PMS    PMS    ${hospital_name}
