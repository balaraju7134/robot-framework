*** Settings ***
Library           SeleniumLibrary
Library           DataDriver    file=../testdata/login_data.csv    dialect=excel    encoding=UTF-8

Resource    ../../../Shared/browser_keywords.resource
Resource    ../variables/common.resource
Resource    ../pages/login_with_password_page.robot

Suite Setup    Open Browser To Application
Suite Teardown    Close Browser Session
Test Teardown    Run Keyword And Ignore Error    Clear Form
Test Template     Login Test

*** Variables ***


*** Test Cases ***
Login With TestData

*** Keywords ***
Login Test
    [Arguments]    ${username}    ${password}    ${expected}

    Enter Username    ${username}
    Enter Password    ${password}
    Click Login Button

    IF    '${expected}' == 'success'
        Check Login Success
    ELSE
        Check Alert Message    ${expected}
    END