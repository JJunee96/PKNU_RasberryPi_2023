import cv2

# 01. 일반이미지
# img = cv2.imread('./Day07/test1.jpg')
# 02. 그레이이미지
# img = cv2.imread('./Day07/test1.jpg', cv2.IMREAD_GRAYSCALE)
# 03. 원본을 그대로두고 흑백을 추가

img = cv2.imread('./Day07/test1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 04. 이미지 축소
# img_small = cv2.resize(img, (200, 90))

# 05. 이미지 자르기
height, width, channel = img.shape
print(height, width, channel)

img_crop = img[:, :int(width / 2)] # height, width
gray_crop = gray[:, :int(width / 2)] # height, width

# 06. 이미지 블러
img_blur = cv2.blur(img_crop, (10, 10)) # 숫자가 클수록 더 많이 블러(흐릿하게)

# cv2.imshow('Original', img)
# cv2.imshow('Gray', gray)
cv2.imshow('Blur half', img_blur)
cv2.imshow('Gray half', gray_crop)

cv2.waitKey(0)
cv2.destroyAllWindows()