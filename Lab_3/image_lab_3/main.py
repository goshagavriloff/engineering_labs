from PIL import Image, ImageFilter


def quest_1(image_path):
    try:
        with Image.open(image_path) as img:
            print(f"Формат изображения: {img.format}")
            print(f"Размеры (Ширина x Высота): {img.size[0]} x {img.size[1]} пикселей")
            save_and_show_img(img,'base_image.jpg')

            new_size = (img.size[0] // 2, img.size[1] // 2)
            resized_img = img.resize(new_size, Image.Resampling.LANCZOS)
            print(f"Новые размеры после уменьшения: {resized_img.size[0]} x {resized_img.size[1]} пикселей")
            save_and_show_img(resized_img,'resize_image.jpg')

            blurred_img = resized_img.filter(ImageFilter.GaussianBlur(radius=2))
            blurred_img.save('result_image.jpg')
            save_and_show_img(blurred_img,'result_image.jpg')

            

    except FileNotFoundError:
        print(f"Ошибка: Файл '{image_path}' не найден. Пожалуйста, проверьте путь.")

def save_and_show_img(img,name):
    img.save(name)
    print(f"Обработанное изображение успешно сохранено как '{name}'")
    img.show()
    
