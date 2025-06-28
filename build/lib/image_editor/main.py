import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageDraw
import cv2


class ImageEditorApp:
    """Основной класс приложения для редактирования изображений."""

    def __init__(self, root):
        """Инициализация приложения.

        Args:
            root (tk.Tk): Главное окно приложения.
        """
        self.root = root
        self.root.title("Редактор изображений")

        # Переменные
        self.image = None
        self.tk_image = None
        self.filename = None
        self.camera_on = False
        self.cap = None
        self.original_image = None  # Для хранения оригинала
        # при показе каналов

        # Интерфейс
        self.create_widgets()

    def create_widgets(self):
        """Создает элементы интерфейса приложения."""
        # Фрейм для кнопок
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        # Кнопка загрузки изображения
        self.load_button = tk.Button(
            button_frame,
            text="Загрузить изображение",
            command=self.load_image
        )
        self.load_button.grid(row=0, column=0, padx=5)

        # Кнопка веб-камеры
        self.webcam_button = tk.Button(
            button_frame,
            text="Снять с веб-камеры",
            command=self.toggle_webcam
        )
        self.webcam_button.grid(row=0, column=1, padx=5)

        # Выбор канала
        channel_label = tk.Label(button_frame, text="Канал:")
        channel_label.grid(row=0, column=2, padx=5)

        self.channel_var = tk.StringVar(value="red")
        self.channel_menu = tk.OptionMenu(
            button_frame,
            self.channel_var,
            "red",
            "green",
            "blue",
            command=self.show_channel
        )
        self.channel_menu.grid(row=0, column=3, padx=5)

        # Кнопка сброса каналов
        self.reset_button = tk.Button(
            button_frame,
            text="Сбросить каналы",
            command=self.restore_original
        )
        self.reset_button.grid(row=0, column=4, padx=5)

        # Изменение размера
        resize_button = tk.Button(
            button_frame,
            text="Изменить размер",
            command=self.resize_image
        )
        resize_button.grid(row=0, column=5, padx=5)

        # Яркость
        brightness_button = tk.Button(
            button_frame,
            text="Изменить яркость",
            command=self.adjust_brightness
        )
        brightness_button.grid(row=0, column=6, padx=5)

        # Прямоугольник
        rect_button = tk.Button(
            button_frame,
            text="Нарисовать прямоугольник",
            command=self.draw_rectangle
        )
        rect_button.grid(row=0, column=7, padx=5)

        # Отображение изображения
        self.image_label = tk.Label(self.root)
        self.image_label.pack()

    def load_image(self):
        """Загружает изображение из файла."""
        filetypes = [("Изображения", "*.jpg *.jpeg *.png")]
        self.filename = filedialog.askopenfilename(filetypes=filetypes)

        if self.filename:
            self.stop_webcam()
            self.image = Image.open(self.filename)
            self.original_image = None
            self.display_image()

    def restore_original(self):
        """Восстанавливает оригинальное изображение."""
        if self.image:
            self.display_image()

    def toggle_webcam(self):
        """Включает/выключает веб-камеру."""
        if not self.camera_on:
            self.start_webcam()
        else:
            self.stop_webcam()

    def start_webcam(self):
        """Запускает веб-камеру."""
        self.camera_on = True
        self.cap = cv2.VideoCapture(0)
        self.webcam_button.config(text="Остановить камеру")
        self.update_webcam()

    def stop_webcam(self):
        """Останавливает веб-камеру."""
        self.camera_on = False
        if self.cap:
            self.cap.release()
        self.webcam_button.config(text="Снять с веб-камеры")

    def update_webcam(self):
        """Обновляет изображение с веб-камеры."""
        if self.camera_on:
            ret, frame = self.cap.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                self.image = Image.fromarray(frame)
                self.display_image()
            self.root.after(10, self.update_webcam)

    def display_image(self):
        """Отображает изображение в интерфейсе."""
        if self.image:
            width, height = self.image.size
            max_size = 800
            if width > max_size or height > max_size:
                ratio = min(max_size / width, max_size / height)
                new_size = (int(width * ratio), int(height * ratio))
                display_image = self.image.resize(new_size,
                                                  Image.LANCZOS)
            else:
                display_image = self.image

            self.tk_image = ImageTk.PhotoImage(display_image)
            self.image_label.config(image=self.tk_image)

    def show_channel(self, channel):
        """Отображает выбранный цветовой канал.

        Args:
            channel (str): Название канала ('red', 'green' или 'blue')
        """
        if not self.image:
            return

        try:
            if (not hasattr(self, 'original_image') or
                    self.original_image is None):
                self.original_image = self.image.copy()

            channel_image = self.original_image.copy()

            if channel_image.mode != 'RGB':
                channel_image = channel_image.convert('RGB')

            r, g, b = channel_image.split()

            if channel == "red":
                g = g.point(lambda _: 0)
                b = b.point(lambda _: 0)
                result = Image.merge("RGB", (r, g, b))
            elif channel == "green":
                r = r.point(lambda _: 0)
                b = b.point(lambda _: 0)
                result = Image.merge("RGB", (r, g, b))
            elif channel == "blue":
                r = r.point(lambda _: 0)
                g = g.point(lambda _: 0)
                result = Image.merge("RGB", (r, g, b))

            self.image = result
            self.display_image()

        except Exception as e:
            messagebox.showerror("Ошибка", f"Не "
                                        f"удалось обработать каналы: "
                                           f"{str(e)}")

    def restore_original(self):
        """Восстанавливает оригинальное изображение."""
        if self.original_image is not None:
            self.image = self.original_image.copy()
            self.original_image = None
            self.display_image()

    def resize_image(self):
        """Изменяет размер изображения."""
        if not self.image:
            return

        resize_dialog = tk.Toplevel(self.root)
        resize_dialog.title("Изменить размер")

        tk.Label(resize_dialog, text="Ширина:").grid(row=0, column=0)
        width_entry = tk.Entry(resize_dialog)
        width_entry.grid(row=0, column=1)

        tk.Label(resize_dialog, text="Высота:").grid(row=1, column=0)
        height_entry = tk.Entry(resize_dialog)
        height_entry.grid(row=1, column=1)

        def apply_resize():
            try:
                new_width = int(width_entry.get())
                new_height = int(height_entry.get())

                if new_width <= 0 or new_height <= 0:
                    raise ValueError

                self.image = self.image.resize(
                    (new_width, new_height),
                    Image.LANCZOS
                )
                self.display_image()
                resize_dialog.destroy()
            except ValueError:
                messagebox.showerror(
                    "Ошибка",
                    "Введите корректные размеры"
                    " (целые числа больше 0)"
                )

        tk.Button(
            resize_dialog,
            text="Применить",
            command=apply_resize
        ).grid(row=2, columnspan=2)

    def adjust_brightness(self):
        """Регулирует яркость изображения."""
        if not self.image:
            return

        brightness_dialog = tk.Toplevel(self.root)
        brightness_dialog.title("Уменьшить яркость")

        tk.Label(brightness_dialog, text="Уменьшение"
                                         " яркости (0-100):").grid(
            row=0, column=0
        )
        brightness_entry = tk.Entry(brightness_dialog)
        brightness_entry.insert(0, "0")
        brightness_entry.grid(row=0, column=1)

        def apply_brightness():
            try:
                value = int(brightness_entry.get())

                if value < 0 or value > 100:
                    raise ValueError

                img = self.image.convert('RGB')
                darkened = Image.eval(
                    img,
                    lambda x: max(0, int(x * (1 - value / 100)))
                )

                self.image = darkened
                self.display_image()
                brightness_dialog.destroy()
            except ValueError:
                messagebox.showerror("Ошибка",
                                     "Введите число от 0 до 100")

        tk.Button(
            brightness_dialog,
            text="Применить",
            command=apply_brightness
        ).grid(row=1, columnspan=2)

    def draw_rectangle(self):
        """Рисует прямоугольник на изображении."""
        if not self.image:
            return

        rect_dialog = tk.Toplevel(self.root)
        rect_dialog.title("Нарисовать прямоугольник")

        tk.Label(rect_dialog, text="X1:").grid(row=0, column=0)
        x1_entry = tk.Entry(rect_dialog)
        x1_entry.grid(row=0, column=1)

        tk.Label(rect_dialog, text="Y1:").grid(row=1, column=0)
        y1_entry = tk.Entry(rect_dialog)
        y1_entry.grid(row=1, column=1)

        tk.Label(rect_dialog, text="X2:").grid(row=2, column=0)
        x2_entry = tk.Entry(rect_dialog)
        x2_entry.grid(row=2, column=1)

        tk.Label(rect_dialog, text="Y2:").grid(row=3, column=0)
        y2_entry = tk.Entry(rect_dialog)
        y2_entry.grid(row=3, column=1)

        def apply_rectangle():
            try:
                x1 = int(x1_entry.get())
                y1 = int(y1_entry.get())
                x2 = int(x2_entry.get())
                y2 = int(y2_entry.get())

                draw_image = self.image.copy()
                draw = ImageDraw.Draw(draw_image)
                draw.rectangle([x1, y1, x2, y2], outline="blue", width=2)

                self.image = draw_image
                self.display_image()
                rect_dialog.destroy()
            except ValueError:
                messagebox.showerror(
                    "Ошибка",
                    "Введите корректные координаты (целые числа)"
                )

        tk.Button(
            rect_dialog,
            text="Нарисовать",
            command=apply_rectangle
        ).grid(row=4, columnspan=2)

def main():
    """Точка входа для запуска приложения"""
    root = tk.Tk()
    app = ImageEditorApp(root)
    root.mainloop()