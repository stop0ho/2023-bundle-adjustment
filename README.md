## **Bundle Adjustment**

**2019103025 컴퓨터공학과 정지호**

---

### **연구배경**

최근 SNS가 활발해지면서 SNS 사용자들의 자기표현 욕구가 점차 높아졌다. 이에 따라 자기표현과 가장 밀접한 인물 사진을 더 아름답게 만들어주는 이미지 보정 어플의 수요가 높아지고 있다. 이미지 보정 어플은 카메라에 기본적으로 탑재되어있는 명암, 대비 등을 조정할 수 있도록 해줄 뿐만 아니라 완벽한 이미지를 만들기 위한 눈, 코, 입술의 크기 조정, 머리 스타일 변경, 피부의 결점 제거까지 가능하다. 심지어 사진의 뒷 배경화면에도 원하는 이미지를 넣을 수 있다. ULIKE, SNOW, SODA, B612, makeup plus 등 수많은 보정 어플은 사진 각각을 아름답게 만들어주지만, 사진마다 보정 해주는 값의 정도에 차이가 있어 동일 인물임에도 사진마다 다른 사람인 것처럼 보정되는 단점이 있다.

또한 봄철 벚꽃 축제나 여름철 바닷가의 경우 사람이 아주 많다. 아래의 사진은 당장 올해 봄 학교의 벚꽃을 구경하기 위해 다녀왔을 때의 사진이다.

![화면 캡처 2023-06-10 003629](https://github.com/stop0ho/2023-bundle-adjustment/assets/68852637/e37b2d4e-409d-4822-b02a-03566473d378)

최대한 사람이 없는 쪽에서 사진을 찍어보려고 해도, 인파가 너무 몰려서 주변에 있는 사람들의 얼굴이 찍히기에 임의로 사람들의 얼굴을 찾아서 모자이크 했다. 굉장히 불편하고 번거로운 일임이 분명하다.

### **연구 목표**

실제 모습은 얼굴에서 눈, 코, 입의 비율이 항상 동일하다. 하지만 사진은 순간을 포착하는 것이므로 사진을 찍을 때의 각도에 따라 눈, 코, 입의 비율이 달라지면서 사진마다 얼굴에 차이가 생길 수 있다. 이렇게 차이가 생긴 사진에 보정 어플을 사용하면서 더 다르게 나오는데, 이를 해결하기 위해 사용자가 지정한 일정 값으로 얼굴 대비 이목구비의 비율을 사진마다 동일하게 맞춰주며 사진을 보정하는 서비스를 개발하고자 하였다.

또한 시중에 있는 서비스 중에서는 사진 당사자를 제외한 주변 인물들의 얼굴을 자동으로 모자이크 해주는 기능이 없다. 따라서 모자이크 기능 또한 개발해보고자 했다.

---

### **연구 방법**

\- OpenCV의 Cascade Classifier를 사용하여 얼굴과 눈을 검출했다. (참고 : [https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html](https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html) )

이 방법에는 명확한 한계점이 존재했다. Open CV에서 제공하는 훈련 데이터는 정면에서 본 얼굴에 대한 이미지들로만 만들어졌기 때문에 정면 사진에 대해서는 얼굴과 눈 인식이 가능하지만, 얼굴 측면을 비추는 사진에 대해서는 인식이 불가능하다는 한계점이 있다. 따라서 일단은 정면 사진을 대상으로 연구를 진행하였다.

![화면 캡처 2023-06-10 004137](https://github.com/stop0ho/2023-bundle-adjustment/assets/68852637/a4bb5990-5b02-4378-9077-9cba99ba7bbb)

⬆ 정면 사진에 대한 결과

![화면 캡처 2023-06-10 004152](https://github.com/stop0ho/2023-bundle-adjustment/assets/68852637/af4c5794-6d97-41a1-91a7-b4164e3cd14e)

⬆ 측면 사진에 대한 결과

또한 사진에 따라서 눈이 아닌 다른 부위를 눈으로 판단하는 경우도 있다. 이 경우는 정면 사진에서 눈이 위치하는 곳이 얼굴의 위쪽임을 이용하여 개선할 수 있었다.

![화면 캡처 2023-06-10 004422](https://github.com/stop0ho/2023-bundle-adjustment/assets/68852637/f29d93ab-bc8b-4994-9c65-ff7ff272d460)

⬆ 눈이 아닌 부위를 눈으로 검출하는 경우

![화면 캡처 2023-06-10 004434](https://github.com/stop0ho/2023-bundle-adjustment/assets/68852637/9983fe56-0528-4706-bc43-a9bfc9e0f8ea)

⬆ 눈만 검출하도록 코드를 수정한 경우

\- 사진 보정을 위해 눈만 segmentation 하기 위해 사용한 각종 알고리즘은 다음과 같다.

1\. grabcut

![grabcut](https://github.com/stop0ho/2023-bundle-adjustment/assets/68852637/b0d6de19-f5d1-4eb1-94de-b128f2969937)

2\. image binarization

![이진화](https://github.com/stop0ho/2023-bundle-adjustment/assets/68852637/9b2a2974-90f6-4587-99f3-c216700a6691)

3\. k-means

![k-means](https://github.com/stop0ho/2023-bundle-adjustment/assets/68852637/2f054099-a5fd-4c79-85c0-cc93fa0e86b3)

4\. Watershed

![watershed](https://github.com/stop0ho/2023-bundle-adjustment/assets/68852637/43d67954-9c33-461f-9f11-30bdc182b595)

\- 모자이크는 Face Detection을 진행하고, 결과로 나온 Face ROI에 cv2.GaussianBlur를 적용해주었다.

![mosaic](https://github.com/stop0ho/2023-bundle-adjustment/assets/68852637/16f6532e-64c7-46c6-ac07-9048b68abc6e)

---

### **한계 및 추후방향**

현재는 정면 사진에 대한 얼굴 인식, 눈 인식, 얼굴 인식에 따른 모자이크만 가능한 상태다.

따라서 추후에는 다음과 같은 기능을 넣어보려고 한다.

- Eye segmentation 후 크기 조정 기능
- 사용자가 선택한 얼굴 이외의 얼굴에 모자이크를 적용시키는 기능
- 사용자가 모자이크의 강도를 선택할 수 있는 기능
