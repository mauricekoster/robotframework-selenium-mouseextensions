# robotframework-selenium-mouseextensions

## Description

The standard SeleniumLibrary has some limited support for mouse actions. Mouse Down and Mouse Up are available 
and clicking on a specific position, but moving the mouse pointer while holding the mouse button is not supported.

This plugin will extend the SeleniumLibrary with extra mouse actions.

## Install

```bash
pip install robotframework-selenium-mouseextensions [--upgrade]
```

## Usage

Add plugin information to the library import of SeleniumLibrary:

```robotframework
*** Settings ***
Library           SeleniumLibrary    plugins=SeleniumMouseExtensions 
```

### Example

```robotframework
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
```