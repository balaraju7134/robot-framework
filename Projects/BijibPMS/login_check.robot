*** Settings ***
Library    SeleniumLibrary

Resource    ../../Shared/variables/common.resource
Resource    ../../Shared/common_keywords.resource

*** Test Cases ***
Login Check
    Open Browser and Login Application    testuser3    correct_password