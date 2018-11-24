from skimage.measure import compare_ssim
import cv2
import imutils
import os
import shutil
import time
import datetime

ROBOT_CONTINUE_ON_FAILURE = True

"""
This is a private method which will take two input images and compare it and save it in a location
"""


def __compare_image(path_one, path_two, diff_save_location):
    """
    Compares two images and saves a diff image, if there
    is a difference
    path_one: The path to the base image
    path_two: The path to the compare image
    diff_save_location: Path where we want to save diff image
    """
    imageA = cv2.imread(path_one)
    imageB = cv2.imread(path_two)

    grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
    (score, diff) = compare_ssim(grayA, grayB, full=True)
    diff = (diff * 255).astype("uint8")
    thresh = cv2.threshold(diff, 0, 255,
                           cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]

    # Checking whether there is a difference in image or not
    if cnts:
        for c in cnts:
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.imwrite(diff_save_location + os.path.basename(path_two), imageB)
    else:
        # If difference is not found then logging which image do not have differences
        print("No Difference found between " + " Image A: " + path_one + " & " + " Image B: " + path_two)

    """
    This is a keyword method.
    This keyword will compare screenshots from folders and find out differences and save it in image file in another folder.
    compare screenshots base_images_path, compare_images_path, diff_images_path   
    """


def compare_screenshots(base_images_path, compare_images_path, diff_images_path):
    if os.path.exists(base_images_path) and os.path.exists(compare_images_path) and os.path.exists(diff_images_path):
        base_images = []
        for file in os.listdir(base_images_path):
            base_images.append(os.path.join(base_images_path,file))
        compare_images = []
        for file in os.listdir(compare_images_path):
            compare_images.append(os.path.join(compare_images_path, file))

        for (fileA, fileB) in zip(base_images, compare_images):
            __compare_image(fileA, fileB, diff_images_path)
    else:

        print("Folders path provided in keyword, does not exist!!")

    """
    This is a keyword method
    This keyword will create txt file report in folder called compare-screenshots-result
    create report :  base_images_path, compare_images_path, diff_images_path
    """


def create_report(base_images_path, compare_images_path, diff_images_path):
    if os.path.exists(base_images_path) and os.path.exists(compare_images_path) and os.path.exists(diff_images_path):
        base_screenshots = os.listdir(base_images_path)
        compare_screenshots_list = os.listdir(compare_images_path)
        diff_screenshots = os.listdir(diff_images_path)

        if os.path.isdir(os.getcwd() + "\\" + "compare-screenshots-result"):
            shutil.rmtree(os.getcwd() + "\\" + "compare-screenshots-result")
            os.mkdir(os.getcwd() + "\\" + "compare-screenshots-result")
        else:
            os.mkdir(os.getcwd() + "\\" + "compare-screenshots-result"+"\\output.txt")

        with open(os.getcwd() + "\\" + "compare-screenshots-result"+"\\output.txt", "w") as file:
            file.write(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') + " Compare Screenshots Output: \n")
            file.write("\nBase Screenshots: ")
            for filename in base_screenshots:
                file.write('\t' + filename)

            file.write("\nCompare Screenshots: ")
            for filename in compare_screenshots_list:
                file.write('\t' + filename)

            file.write("\nDifference found in (" + str(len(diff_screenshots)) + ") Screenshots: ")
            for filename in diff_screenshots:
                file.write('\t' + filename)
    else:

        print("Folders path provided in keyword, does not exist!!")
    """
    This is a keyword method
    This keyword will move and replace screenshots from compare_screenshots to base_screenshots
    move all difference found screenshots : compare_screenshots_path, base_screenshots_path  
    """


def move_all_difference_found_screenshots(compare_screenshots_path, base_screenshots_path):
    if os.path.exists(compare_screenshots_path) and os.path.exists(base_screenshots_path):
        files = os.listdir(compare_screenshots_path)
        for f in files:
            shutil.copy2(compare_screenshots_path + f, base_screenshots_path + f)
