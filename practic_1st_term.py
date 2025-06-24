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

