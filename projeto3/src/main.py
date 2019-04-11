import cv2
import os

IMAGES_FOLDER = os.path.join(os.path.abspath(
    os.path.dirname(__file__)), "../images/")

RED = (0, 0, 255)


def main():
    img = cv2.imread(IMAGES_FOLDER + 'dados.jpg')
    showImg("Original", img)
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 250, 255, cv2.THRESH_BINARY_INV)
    thresh = cv2.medianBlur(thresh, 21)
    showImg('Thresh', thresh)
    contours, hierarchy = cv2.findContours(
        thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img, contours, -1, RED, 2)

    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        roi = img[y:y+h, x:x+w]
        # cv2.imwrite('dado_recortado.jpg', roi)
        # dado = cv2.imread('dado_recortado.jpg', cv2.IMREAD_GRAYSCALE)
        detector = cv2.SimpleBlobDetector_create()
        points = detector.detect(roi)

        if len(points) > 0:
            cv2.putText(img, str(len(points)), (x+w, y+h),
                        cv2.FONT_HERSHEY_SIMPLEX, .5, RED, 2)

    showImg('Dices', img)
    # os.remove('dado_recortado.jpg')


def showImg(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
