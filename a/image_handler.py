from PIL import Image, ImageOps
import os

class ImageHandler:
    def __init__(self, filename):
        self.filename = filename
        # Предположим, что изображения могут находиться в основной директории проекта
        self.img = self.load(f"{os.getcwd()}/{self.filename}")  # Загружаем из текущей рабочей директории
        self.format = self.filename.split('.')[1]
        self.filename = self.filename.split('.')[0]

    def load(self, filename):
        try:
            with Image.open(filename) as img:
                img.load()
            print(f"Изображение {filename} открыто")
            return img
        except FileNotFoundError:
            raise Exception(f"Файл {filename} не найден. Проверьте путь и имя файла.")

    def save(self):
        self.img.save(f'a/new_{self.filename}.{self.format}')
        print(f"Изображение сохранено как new_{self.filename}.{self.format}")


    def save_with_data(self):
        from datetime import datetime
        date = datetime.now().strftime("%d-%m-%Y")
        self.img.save(f'a/new_{self.filename}-{date}.{self.format}')

    def resize_thumbnail(self):
        self.img.thumbnail((200, 200))
        print("Размер изображения уменьшен до 200x200 пикселей")

    def save_thumbnail(self):
        self.img.save(f'a/thumbnail_{self.filename}.{self.format}')
        print(f"Уменьшенное изображение сохранено как thumbnail_{self.filename}.{self.format}")
