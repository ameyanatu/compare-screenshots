from skimage.measure import compare_ssim
import cv2
import imutils
import os


def __compare_image(path_one, path_two, diff_save_location):
    """
    Compares to images and saves a diff image, if there
    is a difference
    @param: path_one: The path to the base image
    @param: path_two: The path to the compare image
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

    if cnts:
        for c in cnts:
            # compute the bounding box of the contour and then draw the
            # bounding box on both input images to represent where the two
            # images differ
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.imwrite(diff_save_location + "diff_" + os.path.basename(path_two), imageB)
    else:
        print("No Difference found between " + path_one + " & " + path_two)


def compare_screenshots(base_images_path, compare_images_path, diff_images_path):
    base_images = []
    for file in os.listdir(base_images_path):
        base_images.append(os.path.join(base_images_path,file))

    compare_images = []
    for file in os.listdir(compare_images_path):
        compare_images.append(os.path.join(compare_images_path, file))

    for (fileA, fileB) in zip(base_images, compare_images):
        __compare_image(fileA, fileB, diff_images_path)


# if __name__ == '__main__':
#     compare_screenshots('E:/RobotFrameworkProjects/compare-screenshots/compare-screenshots/Test/base-images/', 'E:/RobotFrameworkProjects/compare-screenshots/compare-screenshots/Test/compare-images/',
#                     'E:/RobotFrameworkProjects/compare-screenshots/compare-screenshots/Test/diff-images/')



