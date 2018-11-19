**** Settings ***
Library  compare-screenshots.py

*** Test Cases ***

comparing screenshots
    compare screenshots  E:/RobotFrameworkProjects/compare-screenshots/Test/base-images/  E:/RobotFrameworkProjects/compare-screenshots/Test/compare-images/  E:/RobotFrameworkProjects/compare-screenshots/Test/diff-images/
