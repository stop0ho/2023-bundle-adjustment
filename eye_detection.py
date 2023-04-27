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
image_path = 'img/sample1.jpg'

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
    # 눈 ROI 추출
    eyeRects = detectors["eyes"].detectMultiScale(faceROI, scaleFactor=1.1, minNeighbors=10, minSize=(15, 15),
                                                  flags=cv2.CASCADE_SCALE_IMAGE)

    # 눈 bounding box
    for (eX, eY, eW, eH) in eyeRects:
        # draw the eye bounding box
        ptA = (fX + eX, fY + eY)
        ptB = (fX + eX + eW, fY + eY + eH)
        cv2.rectangle(image, ptA, ptB, (0, 0, 255), 2)

    # 얼굴 bounding box
    cv2.rectangle(image, (fX, fY), (fX + fW, fY + fH), (0, 255, 0), 2)

plt_imshow("Output", image, figsize=(16, 10))
