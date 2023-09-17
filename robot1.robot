*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${login}     RobotTests
${good_password}    RobotFramework
${wrong_password}    wrong_pass
${error_message}    Podany login lub hasło są nieprawidłowe. Spróbuj jeszcze raz.

*** Keywords ***


*** Test Cases ***
#My First Test
#    Open Browser    https://pl.wikipedia.org/    chrome    #executable_path=C:/chromedriver/chromedriver.exe
#    Set Window Size    1200     800
#    Sleep    1
#    Click Element    id:pt-login-2
#    Input Text    id:wpName1    RobotTests
#    Input Password    id:wpPassword1    RobotFramework
#    Select Checkbox    id:wpRemember
#    Wait Until Element Is Visible    id:wpLoginAttempt   3
#    click button    id:wpLoginAttempt
#    Wait Until Element Is Visible    name:search    3
#    Input text      name:search   Teoria Wielkiego Podrywu
#    click button  //*[@id="searchform"]/div/button
#    Capture Page Screenshot
#    Close Browser

My Second Test
    Run Keyword And Ignore Error    Click Button    id:cookies
    Open Browser    https://pl.wikipedia.org/    chrome    #executable_path=C:/chromedriver/chromedriver.exe
    Set Window Size    1200     800
    Sleep    1
    Click Element    id:pt-login-2
    Input Text    id:wpName1    ${login}
    Input Password    id:wpPassword1   ${wrong_password}
    Checkbox Should Not Be Selected    id:wpRemember
    Select Checkbox    id:wpRemember
    Wait Until Element Is Visible    id:wpLoginAttempt   3
    click button    id:wpLoginAttempt
    Wait Until Element Is Visible    //*[@id="userloginForm"]/form/div[1]/div    5
    ${my_error_message}   Get Text    //*[@id="userloginForm"]/form/div[1]/div
    Log   ${my_error_message}
    Log To Console    ${my_error_message}
    Should Be Equal As Strings    ${my_error_message}    ${error_message}
    Capture Page Screenshot
    Close Browser