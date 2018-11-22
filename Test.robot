**** Settings ***
Library  compare-screenshots.py

#Robot -d Robot-Result Test.Robot
**** Variables ***

${base-imagepath}  E:/RobotFrameworkProjects/compare-screenshots/compare-screenshots/Test/base-images/
${compare-imagepath}  E:/RobotFrameworkProjects/compare-screenshots/compare-screenshots/Test/compare-images/
${diff-imagepath}  E:/RobotFrameworkProjects/compare-screenshots/compare-screenshots/Test/diff-images/

*** Test Cases ***
comparing screenshots
    compare screenshots  ${base-imagepath}  ${compare-imagepath}  ${diff-imagepath}
