# compare-screenshots

[![HitCount](http://hits.dwyl.io/ameyanatu/compare-screenshots.svg)](http://hits.dwyl.io/ameyanatu/compare-screenshots) [![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)

This is a Robot Framework library which contains one single keyword "compare screenshots" with three arguments.

{base_image_path, compare_image_path, diff_image_path}

(Note: Please consider image or images as a screenshot or screenshots) :blush:

base_image_path: This folder path should contain manually validated screenshots which act like baseline for your project.

compare_image_path: This folder path should contain new build screenshots, which you want to compare with baseline images.

diff_image_path: This folder path should contain difference found images which later you can move it to base_image_path folder if difference is valid. If difference is not valid then you can log a defect.

How to use this library:

1. Download and install all the necessary libraries from Requirements.txt
2. Then download compare-screenshots.py file to your framework's  library folder.
3. Then simply use this  library in your Robot file and use "compare screenshots" keyword.

For more information please read following linkedin article :





