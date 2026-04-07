*** Variables ***
${BROWSER}    chrome
${WEB_TITLE}    Bijib
${SELENIUM_SPEED}    0s
${TIMEOUT}    10s
${TIMEOUT_LONG}    30s
${ENV}    test

*** Settings ***
Resource    ${ENV}.resource

*** Variables ***
${DASHBOARD_URL}    ${BASE_URL}/#/layout/dashboard