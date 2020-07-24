*** Settings ***
Suite Setup       Open Browser    about:blank    browser=Chrome
Suite Teardown    Close Browser
Library           SeleniumLibrary    plugins=SeleniumMouseExtensions

*** Test Cases ***
Test Kleki
    Go To    http://kleki.com
    Sleep    5s
    mouse down with offset    //canvas    300    300
    mouse move by offset    100    100
    mouse up
    mouse down with offset    //canvas    300    400
    mouse move by offset    100    -100
    mouse up
    Capture Page Screenshot
    Sleep    5s

*** Keywords ***
