from a.image_handler import ImageHandler
from a.image_processor import ImageProcessor

def main():
    try:
        filename = input("Введите название изображения с форматом (например, image.jpg): ")
        image_handler = ImageHandler(filename)
        image_processor = ImageProcessor(image_handler.img)
    except Exception as e:
        print(f"Ошибка: {e}")
        return

    while True:
        try:
            print("\nМеню:")
            print("1 - Уменьшить изображение до 200x200 пикселей")
            print("2 - Сохранить уменьшенное изображение")
            print("3 - Применить фильтр контуров")
            print("4 - Добавить текст 'Вариант 3' в центр изображения")
            print("5 - Сохранить изображение")
            print("0 - Выход")

            choice = int(input("Выберите опцию: "))

            if choice == 1:
                image_handler.resize_thumbnail()

            elif choice == 2:
                image_handler.save_thumbnail()

            elif choice == 3:
                image_processor.apply_contour_filter()

            elif choice == 4:
                image_processor.add_text()

            elif choice == 5:
                image_handler.save()

            elif choice == 0:
                print("Выход из программы.")
                break

            else:
                print("Некорректный ввод. Попробуйте снова.")

        except Exception as e:
            print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()
