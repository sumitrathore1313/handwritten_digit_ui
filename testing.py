import cv2
import os
if os.path.exists('number.png'):
    img = cv2.imread('number.png', 0)
    img = cv2.resize(img, (28, 28))
    cv2.imshow("image", img)
    print img.shape
    cv2.waitKey(0)
    cv2.destroyAllWindows()