import matplotlib.pyplot as plt
import imutils
import cv2
import os

'''이미지 확인 function'''


def plt_imshow(title='image', img=None, figsize=(5, 5)):
    """이미지 영역 확보"""
    plt.figure(figsize=figsize)

    if type(img) == list:
        if type(title) == list:
            titles = title
        else:
            titles = []

            for i in range(len(img)):
                titles.append(title)

        for i in range(len(img)):
            if len(img[i].shape) <= 2:
                rgbImg = cv2.cvtColor(img[i], cv2.COLOR_GRAY2RGB)
            else:
                rgbImg = cv2.cvtColor(img[i], cv2.COLOR_BGR2RGB)

            plt.subplot(1, len(img), i + 1), plt.imshow(rgbImg)
            plt.title(titles[i])
            plt.xticks([]), plt.yticks([])

        plt.show()
    else:
        if len(img.shape) < 3:
            rgbImg = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
        else:
            rgbImg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        plt.imshow(rgbImg)
        plt.title(title)
        plt.xticks([]), plt.yticks([])
        plt.show()


'''Load Haar cascades'''
cascades_path = 'resource'
detectorPaths = {
    "face": "haarcascade_frontalface_alt2.xml",
    "eyes": "haarcascade_eye_tree_eyeglasses.xml",
}

detectors = {}
for (name, path) in detectorPaths.items():
    path = os.path.sep.join([cascades_path, path])
    detectors[name] = cv2.CascadeClassifier(path)

'''Load Image'''
'''sample1, 4, 7, 8, 9에서만 됨'''
image_path = 'img/sample10.jpg'

image = cv2.imread(image_path)
image = imutils.resize(image, width=900)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

'''Face Detection'''
'''
cv2.CascadeClassifier.detectMultiScale(image, scaleFactor=None, minNeighbors=None, minSize=None, maxSize=None)
- image : 입력영상(cv2.CV_8U)
- scaleFactor : 영상 축소 비율. 기본값 1.1
- minNeighbors : 얼마나 많은 이웃 사각형이 검출 되어야 최종 검출 영역으로 설정할지 지정. 디폴트 3
- minSize : 최소 객체 크기
- maxSize : 최대 객체 크기
'''
faceRects = detectors["face"].detectMultiScale(gray, scaleFactor=1.07, minNeighbors=5, minSize=(30, 30),
                                               flags=cv2.CASCADE_SCALE_IMAGE)

for (fX, fY, fW, fH) in faceRects:
    # 얼굴 ROI 추출
    faceROI = gray[fY:fY + fH, fX:fX + fW]

    '''
    cv2.rectangle(img, pt1, pt2, color[, thickness[, lineType[, shift]]]) -> img
    - img : 이미지 파일
    - pt1 : 시작점 좌표 (x, y)
    - pt2 : 종료점 좌표 (x, y)
    - color : 색상 (blue, green, red) 0 ~ 255
    - thickness : 선 두께(default 1)
    - lineType : 선 종류
    - shift : fractional bit (default 0)
    '''
    mosaic_loc = image[fY:fY + fH, fX:fX + fW]
    mosaic_loc = cv2.GaussianBlur(mosaic_loc, (0, 0), 3)

    img_w_mosaic = image
    img_w_mosaic[fY:fY + fH, fX:fX + fW] = mosaic_loc


plt_imshow("Output", image, figsize=(16, 10))
