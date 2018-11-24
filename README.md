# compare-screenshots

[![HitCount](http://hits.dwyl.io/ameyanatu/compare-screenshots.svg)](http://hits.dwyl.io/ameyanatu/compare-screenshots)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/ameyanatu/compare-screenshots/blob/master/compare-screenshots.py/graphs/commit-activity)
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](http://perso.crans.org/besson/LICENSE.html)
----------------------------------------------------------------------------------------------------------------------------------------
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
----------------------------------------------------------------------------------------------------------------------------------------

#### This is a Robot Framework library. Using this library we can do screenshots comparison which is an essential part of visual testing using Robot Framework.

| Keyword      | Description                    |
| ------------- | ------------------------------ |
| `compare screenshots`| This is the main keyword which actually does a comparison, this keyword takes three arguments path_to_baseline_screenshots, path_to_compare_screenshots and path_to_save_differencefound_screenshots|
| `create report`| This keyword creates a text file report of the comparison, like how many screenshots have differences, this keyword takes three arguments path_to_baseline_screenshots, path_to_compare_screenshots, and path_to_save_differencefound_screenshots|
| `move all difference found screenshots`| This keyword will move all the difference found screenshots from path_to_compare_screenshots To path_to_baseline_screenshots

#### How to use this library:

1. Download 'compare-screenshots.py' from this repository.
2. Download 'Requirements.txt' and install all the necessary packages before using this library.
3. Copy 'compare-screenshots.py' file to your Robot Framework project.
4. Then simply use it in your Robot file and use keywords in your test cases or tasks. 

##### (Note: This library tested on windows platform, however, I am sure it will work on the Linux platform as well. If you found any issue then please let me know.)

#### For more information regarding this library please read my article on LinkedIn: 

#### Credits:

1. RobotFramework (http://robotframework.org/)
2. OpenCV (https://opencv.org/)


##### If you have any questions / suggestions / comments on the library, please feel free to reach me on ameyanatu@yahoo.com


[![saythanks](https://img.shields.io/badge/say-thanks-ff69b4.svg)](https://saythanks.io/to/ameyanatu)
[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://GitHub.com/ameyanatu/)
