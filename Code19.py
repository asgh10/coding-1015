# 사진은 실존하지 않으며 임의로 둔 이미지 파일이름이다 ( 실행도 당연히 안된다 ) 

from PIL import Image
from PIL import ImageFilter # 필터 기능을 쓰기위해 불러온 모듈

img = Image.open("my_image.jpg")
# 컴퓨터에 있는 이미지 파일을 파이썬으로 불러와 조작할 수 있는상태로 만든다

#-----------------------------------------------------------------------

print(f"원래 이미지 크기: {img.size}")

resized_img = img.resize((300, 300)) # 크기를 조정하는 코드
resized_img.save("resized_image.jpg") # 이미지를 저장하는 코드이며 이름을 정할 수 있다

#-----------------------------------------------------------------------

rotated_img = img.rotate(90) # 각도를 조정 하는 코드
rotated_img.save("rotated_image.jpg")
# expand=True 옵션중 이런 기능이 있는데 모서리가 잘리지 않도록 해주는 코드이다 ( 전체코드 -  img.rotate(90, expand=True))

#-----------------------------------------------------------------------

box = (100, 100, 400, 400) # 이미지를 자르는 코드 순서대로 왼쪽, 위쪽, 오른쪽, 아래쪽 이며 (100, 100) 좌표부터 (400, 400) 까지 자르라는 코드이다 
cropped_img = img.crop(box)

cropped_img.save("cropped_image.jpg")

#-----------------------------------------------------------------------

gray_img = img.convert("L") # 컬러를 변환하는 코드
gray_img.save("gray_image.jpg")

#-----------------------------------------------------------------------

blur_img = img.filter(ImageFilter.BLUR) # 뿌옇게 만드는 코드
blur_img.save("blur_image.jpg")

contour_img = img.filter(ImageFilter.CONTOUR) # 윤곽선만 남기는 코드
contour_img.save("contour_image.jpg")

#-----------------------------------------------------------------------

print("이미지 편집과 저장 완료!")