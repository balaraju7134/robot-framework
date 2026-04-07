*** Settings ***
Library    SeleniumLibrary

*** Variables ***

*** Keywords ***

Go To Service
    [Arguments]    ${service_name}    ${page_title}    ${hospital_name}=${EMPTY}
    
    ${service_locator}=    Set Variable    //li[@title="${service_name}"]
    Wait Until Element Is Visible    ${service_locator}    ${TIMEOUT}
    Click Element    ${service_locator}
    
    # Only select hospital if menu exists and hospital_name provided
    Run Keyword If    '${hospital_name}' != ''    Select Service Hospital    ${hospital_name}
    
    Wait Until Keyword Succeeds    ${TIMEOUT}    1s    Title Should Be    ${page_title}


Select Service Hospital
    [Arguments]    ${hospital_name}
    
    ${hospital_menu_locator}=    Set Variable    //div[contains(@class,"submenu dsktp-vw-dsply")]
    ${menu_present}=    Run Keyword And Return Status    Wait Until Element Is Visible    ${hospital_menu_locator}    ${TIMEOUT}    fail_on_timeout=False
    
    IF    ${menu_present}
        ${hospital_locator}=    Set Variable    //div[contains(@class,"submenu dsktp-vw-dsply")]//li[normalize-space(.)="${hospital_name}"]
        ${is_present}=    Run Keyword And Return Status    Page Should Contain Element    ${hospital_locator}
        Run Keyword If    ${is_present}    Click Element    ${hospital_locator}
        Run Keyword If    not ${is_present}    Log    Hospital "${hospital_name}" not found in menu    WARN
    END

