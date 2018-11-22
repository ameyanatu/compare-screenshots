# compare-screenshots

[![HitCount](http://hits.dwyl.io/ameyanatu/compare-screenshots.svg)](http://hits.dwyl.io/ameyanatu/compare-screenshots)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/ameyanatu/compare-screenshots/blob/master/compare-screenshots.py/graphs/commit-activity)
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)

#### This is a Robot Framework library which has one single keyword "compare screenshots" with three arguments. Using this library we can perform visual testing using Robot Framework.

| Argument      | Description                    |
| ------------- | ------------------------------ |
| `base_screenshots_path`      | This folder path should contain manually validated screenshots which act like baseline for your project.|
| `compare_screenshots_path`   | This folder path should contain new build screenshots, which you want to compare with baseline screenshots.|
| `diff_screenshots_path`   | This folder path should contain difference found screenshots which later you can move it to base_screenshots_path folder if difference is valid.|

#### How to use this library:

1. Download 'compare-screenshots.py' from this repository
2. Copy 'compare-screenshots.py' file to your Robot Framework project.
3. Then simply use it in your Robot file and use 'compare screenshots' keyword.

#### Credits:

1. RobotFramework (http://robotframework.org/)
2. OpenCV (https://opencv.org/)


##### If you have any questions / suggestions / comments on the library, please feel free to reach me on ameyanatu@yahoo.com

