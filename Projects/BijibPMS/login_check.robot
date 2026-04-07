*** Settings ***
Library    SeleniumLibrary

Resource    ../../Shared/variables/common.resource
Resource    ./resources/common_keywords.resource

*** Test Cases ***
Go To Bijib PMS
    Login and Goto Bijib PMS    testuser3    correct_password    TEST HOSPITAL
