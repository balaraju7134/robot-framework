*** Settings ***
Library    SeleniumLibrary

*** Variables ***


*** Keywords ***
Open Browser To Application
    Open Browser    ${BASE_URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed    ${SELENIUM_SPEED}

Close Browser Session
    Close Browser