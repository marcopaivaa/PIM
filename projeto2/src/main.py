import cv2
import numpy as np

def main():
    img = np.ones((10,10),np.uint8)
    shape = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
    print("\nOriginal:")
    print(img)
    output = cv2.erode(img, shape, iterations=1, borderValue=0)
    checkSquareArea(output)
    print("\nEroded:")
    print(output)
    showImg("Original", img)
    showImg("Eroded", output)
    cv2.waitKey()


def checkSquareArea(matrix):
    for i in range(1, len(matrix) - 1):
        for j in range(1, len(matrix[i]) - 1):
            hasOne = False
            sub_m = matrix[i-1:i+2,j-1:j+2]
            for i_s in range(0, len(sub_m)):
                for j_s in range(0, len(sub_m[i_s])):
                    if(sub_m[i_s][j_s] == 1):
                        if(not hasOne):
                            hasOne = True
                        else:
                            sub_m[i_s][j_s] = 0

    
def showImg(name, matrix):
    img = np.ones((10,10,3),np.uint8)
    matrix = matrix * 255
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            img[i,j] = img[i,j] * matrix[i][j]
    
    img = cv2.resize(img, (400,400), interpolation = cv2.INTER_NEAREST)
    img = cv2.bitwise_not(img)
    cv2.imshow(name,img)


if __name__ == "__main__":
    main()
