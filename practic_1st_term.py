import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageDraw
import cv2


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
            self.display_image()

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


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEditorApp(root)
    root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEditorApp(root)
    root.mainloop()