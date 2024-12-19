from PIL import Image, ImageOps  # Импортируем необходимые модули из библиотеки pillow
import os  #работы с путями файлов в операционной системе

class ImageHandler:
    def __init__(self, filename):
        #инициализирует объект с данным файлом изображения
        self.filename = filename
        #Загружаем изображение из текущей рабочей директории
        self.img = self.load(f"{os.getcwd()}/{self.filename}")
        # Определяем формат изоб
        self.format = self.filename.split('.')[1]
        #Убираем расширение из имени файла
        self.filename = self.filename.split('.')[0]

    def load(self, filename):
        # Метод для загрузки изображения
        try:
            # Открываем изображение с помощью PIL
            with Image.open(filename) as img:
                img.load()  # Загружаем изображение в память
            print(f"Изображение {filename} открыто")  # Выводим сообщение об успешной загрузке
            return img  # Возвращаем объект изображения
        except FileNotFoundError:
            # Если файл не найден, выбрасываем исключение
            raise Exception(f"Файл {filename} не найден. Проверьте путь и имя файла.")

    def save(self):
        #сохранения изображения в папку 'a'
        self.img.save(f'a/new_{self.filename}.{self.format}')
        print(f"Изображение сохранено как new_{self.filename}.{self.format}")

    def resize_thumbnail(self):
        #изменения размера изображения до 200x200 пикселей
        self.img.thumbnail((200, 200))
        print("Размер изображения уменьшен до 200x200 пикселей") 

    def save_thumbnail(self):
        #сохраненик уменьшенного изображения
        self.img.save(f'a/thumbnail_{self.filename}.{self.format}')
        print(f"Уменьшенное изображение сохранено как thumbnail_{self.filename}.{self.format}")
