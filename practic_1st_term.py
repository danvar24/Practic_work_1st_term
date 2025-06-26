import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import cv2


class ImageEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Редактор изображений")

        # Переменные состояния
        self.image = None
        self.tk_image = None
        self.filename = None
        self.camera_on = False
        self.cap = None
        self.original_image = None

        self.create_widgets()

    def create_widgets(self):
        # Основной фрейм для кнопок
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        # Кнопки управления
        self.load_button = tk.Button(
            button_frame,
            text="Загрузить",
            command=self.load_image
        )
        self.load_button.grid(row=0, column=0, padx=5)

        self.webcam_button = tk.Button(
            button_frame,
            text="Камера",
            command=self.toggle_webcam
        )
        self.webcam_button.grid(row=0, column=1, padx=5)

        # Элементы для работы с каналами
        tk.Label(button_frame, text="Канал:").grid(row=0, column=2, padx=5)

        self.channel_var = tk.StringVar(value="red")
        channels = ["red", "green", "blue"]
        self.channel_menu = tk.OptionMenu(
            button_frame,
            self.channel_var,
            *channels,
            command=self.show_channel
        )
        self.channel_menu.grid(row=0, column=3, padx=5)

        self.reset_button = tk.Button(
            button_frame,
            text="Сброс",
            command=self.restore_original
        )
        self.reset_button.grid(row=0, column=4, padx=5)

        # Область отображения изображения
        self.image_label = tk.Label(self.root)
        self.image_label.pack()

    def load_image(self):
        filetypes = [("Изображения", "*.jpg *.jpeg *.png")]
        self.filename = filedialog.askopenfilename(filetypes=filetypes)

        if self.filename:
            self.stop_webcam()
            self.image = Image.open(self.filename)
            self.original_image = None
            self.display_image()

    def toggle_webcam(self):
        if not self.camera_on:
            self.start_webcam()
        else:
            self.stop_webcam()

    def start_webcam(self):
        self.camera_on = True
        self.cap = cv2.VideoCapture(0)
        self.webcam_button.config(text="Стоп")
        self.update_webcam()

    def stop_webcam(self):
        self.camera_on = False
        if self.cap:
            self.cap.release()
        self.webcam_button.config(text="Камера")

    def update_webcam(self):
        if self.camera_on:
            ret, frame = self.cap.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                self.image = Image.fromarray(frame)
                self.display_image()
            self.root.after(10, self.update_webcam)

    def show_channel(self, channel):
        if not self.image:
            return

        try:
            if self.original_image is None:
                self.original_image = self.image.copy()

            img = self.original_image.copy()
            if img.mode != 'RGB':
                img = img.convert('RGB')

            r, g, b = img.split()

            if channel == "red":
                g = g.point(lambda _: 0)
                b = b.point(lambda _: 0)
            elif channel == "green":
                r = r.point(lambda _: 0)
                b = b.point(lambda _: 0)
            elif channel == "blue":
                r = r.point(lambda _: 0)
                g = g.point(lambda _: 0)

            self.image = Image.merge("RGB", (r, g, b))
            self.display_image()

        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка обработки: {str(e)}")

    def restore_original(self):
        if self.original_image is not None:
            self.image = self.original_image.copy()
            self.original_image = None
            self.display_image()

    def display_image(self):
        if self.image:
            # Масштабирование для отображения
            width, height = self.image.size
            max_size = 800

            if width > max_size or height > max_size:
                ratio = min(max_size / width, max_size / height)
                new_size = (int(width * ratio), int(height * ratio))
                display_img = self.image.resize(new_size, Image.LANCZOS)
            else:
                display_img = self.image

            self.tk_image = ImageTk.PhotoImage(display_img)
            self.image_label.config(image=self.tk_image)


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEditorApp(root)
    root.mainloop()