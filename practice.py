from PIL import Image
from PIL import ImageFilter

img = Image.open("my_image.png")

rotated_image = img.rotate(65, expand=True)

blur_image = rotated_image.filter(ImageFilter.BLUR)

blur_image.save("final_image.png")

print("저장완료")

# rollback 같은 기능은 없고 다시 내가 이걸 했던것처럼 반대로 해서 복구하는 방법이있다