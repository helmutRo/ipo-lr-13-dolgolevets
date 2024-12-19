from a.image_handler import ImageHandler  #Импорт класс ImageHandler
from a.image_processor import ImageProcessor  #Импорт класс ImageProcessor

def main():
    try:
        #название файла с изображением
        filename = input("Введите название изображения с форматом (например, image.jpg): ")
        # Создаем объект класса ImageHandler, передавая ему имя файла
        image_handler = ImageHandler(filename)
        # Создаем объект класса ImageProcessor, передавая ему изображение из image_handler
        image_processor = ImageProcessor(image_handler.img)
    except Exception as e:
        #В случае ошибки вывод ошибки
        print(f"Ошибка: {e}")
        return

    while True:
        try:
            #меню
            print("\nМеню:")
            print("1 - Уменьшить изображение до 200x200 пикселей") 
            print("2 - Сохранить уменьшенное изображение") 
            print("3 - Применить фильтр контуров") 
            print("4 - Добавить текст 'Вариант 3' в центр изображения")
            print("5 - Сохранить изображение") 
            print("0 - Выход")

            # Запрашиваем у пользователя выбор
            choice = int(input("Выберите опцию: "))

            # Обрабатываем выбор пользователя
            if choice == 1:
                # Уменьшаем изображение до размера 200x200 пикселей
                image_handler.resize_thumbnail()

            elif choice == 2:
                # Сохраняем уменьшенное изображение
                image_handler.save_thumbnail()

            elif choice == 3:
                #фильтр контур
                image_processor.apply_contour_filter()

            elif choice == 4:
                #текст 'Вариант 3' в центр изображения
                image_processor.add_text()

            elif choice == 5:
                #Сохр текущее состояние изображения
                image_handler.save()

            elif choice == 0:
                #выход из программы
                print("Выход из программы.")
                break

            else:
                #Если выбран неверный номер, вывод ошибки
                print("Некорректный ввод. Попробуйте снова.")

        except Exception as e:
            # Ловим исключения внутри цикла и вывод ошибки
            print(f"Ошибка: {e}")

#main() запусквется только в случае, если этот скрипт запускается напрямую
if __name__ == "__main__":
    main()
