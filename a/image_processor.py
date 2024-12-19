from PIL import ImageDraw, ImageFont, ImageFilter
class ImageProcessor:
    def __init__(self, img):
        self.img = img
    def apply_contour_filter(self):
        # Применяем фильтр контуров (CONTOUR)
        self.img = self.img.filter(ImageFilter.CONTOUR)
        print("Применён фильтр контуров")

    def add_text(self):
        # Используем ImageDraw для рисования текста
        draw = ImageDraw.Draw(self.img)
        text = "Вариант 3"
        # Получаем размеры изображения
        width, height = self.img.size
        # Загрузка шрифта Arial в обычном стиле
        try:
            font = ImageFont.truetype("arial.ttf", 36)  #Путь к шрифту Arial
        except IOError:
            font = ImageFont.load_default()  #если Arial не найден
        # Получаем размеры текста с помощью textbbox
        text_bbox = draw.textbbox((0, 0), text, font=font)  # Получаем границы текста
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        # Располагаем текст по центру изображения
        position = ((width - text_width) // 2, (height - text_height) // 2)
        # Рисуем текст
        draw.text(position, text, font=font, fill="white")
        print("Текст 'Вариант 3' добавлен в центр изображения")
        return self.img
