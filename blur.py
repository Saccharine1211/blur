import os

## python3 -m pip install --upgrade pip
## python3 -m pip install --upgrade Pillow
from PIL import Image, ImageFilter

# 이미지가 저장된 폴더 경로
image_folder_path = 'images'

# 블러처리된 이미지를 저장할 폴더 경로
blurred_image_folder_path = 'blurred_images'

# 이미지 폴더 내의 모든 파일명을 가져옵니다.
image_filenames = os.listdir(image_folder_path)

# 이미지 폴더 내의 모든 이미지를 순차적으로 블러처리합니다.
for image_filename in image_filenames:
    # 이미지를 열고 블러처리합니다.
    image = Image.open(os.path.join(image_folder_path, image_filename))
    blurred_image = image.filter(ImageFilter.BLUR)
    
    # 블러처리된 이미지를 저장합니다.
    blurred_image_filename = f'{os.path.splitext(image_filename)[0]}_blurred{os.path.splitext(image_filename)[1]}'
    blurred_image.save(os.path.join(blurred_image_folder_path, blurred_image_filename))

