*** Settings ***
Library    SeleniumLibrary

*** Variables ***


*** Keywords ***


*** Test Cases ***
My First Test
    Open Browser    https://pl.wikipedia.org/    chrome    #executable_path=C:/chromedriver/chromedriver.exe
    Sleep    1
    Click Element    id:pt-login-2

    Input Text    id:wpName1    RobotTests
    Sleep    1
    Close Browser