*** Settings ***
Library    SeleniumLibrary


*** Variables ***
${username_path}    //input[@placeholder="Enter Username"]
${password_path}    //input[@placeholder="Enter Password"]
${login_button_path}    //button[normalize-space()="Login"]
${alert_message_path}    //p[contains(@class,"alert")]
${login_success_locator}    User Management System

*** Keywords ***
Enter Username
    [Arguments]    ${username}
    Wait Until Element Is Visible    ${username_path}    ${TIMEOUT}
    Input Text      ${username_path}    ${username}

Enter Password
    [Arguments]    ${password}
    Wait Until Element Is Visible    ${password_path}    ${TIMEOUT}
    Input Text      ${password_path}    ${password}

Click Login Button
    Wait Until Element Is Visible    ${login_button_path}    ${TIMEOUT}
    Click Button    ${login_button_path}

Clear Form
    Input Text      ${username_path}    ${EMPTY}
    Input Text      ${password_path}    ${EMPTY}

Check Alert Message
    [Arguments]    ${expected_message}
    Wait Until Element Is Visible    ${alert_message_path}    ${TIMEOUT}
    ${alert_message}=    Get Text    ${alert_message_path}
    Should Be Equal    ${expected_message}    ${alert_message}

Check Login Success
    Wait Until Page Contains    ${login_success_locator}    timeout=10s
    Page Should Contain    ${login_success_locator}
