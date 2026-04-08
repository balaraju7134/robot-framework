*** Settings ***
Library    SeleniumLibrary
Library    UIAutomationLib

Resource    ../../Shared/variables/common.resource
Resource    ./resources/common_keywords.resource

*** Test Cases ***
Go To Bijib PMS
    Login and Goto Bijib PMS    testuser3    E7q_35&ZR]5D*iRZ    TEST HOSPITAL
    Enter Textfield By Label    
