# 🎛️ Image Editor - Графический редактор изображений

*Простой и удобный инструмент для обработки изображений*

## 🗒️ Описание
Image Editor - это кроссплатформенное приложение с графическим интерфейсом для базовой обработки изображений. Поддерживает работу с файлами и захват изображений с веб-камеры.

**🔧 Основные возможности:**
- 📥 Загрузка изображений (JPG, PNG, JPEG)
- 🌅 Захват фото с веб-камеры
- 🖌️ Выделение цветовых каналов (RGB)
- 📐 Изменение размера изображения
- 💡 Регулировка яркости
- 🟦 Рисование синего прямоугольника

## ⚡ Быстрый старт

### Установка
```bash
pip install image-editor
```

### Запуск
```bash
image-editor
```

## 🛠️ Установка из исходников

### Требования
- 🐍 Python 3.7+
- 📦 pip

### Шаги установки:
1. Клонирование репозитория
```
git clone https://github.com/danvar24/Practic_work_1st_term
cd Practic_work_1st_term
```

2. Создать виртуальное окружение (ОБЯЗАТЕЛЬНО на Linux/macOS)
```
# Windows
python -m venv venv
venv\Scripts\activate
```
```
# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```
3. Установка зависимостей
```
pip install -r requirements.txt
```
4. Установка пакета (опцианально)
```
pip install .
```

5. Запуск 
```
python -m image_editor

#или

python image_editor/app.py
```

## 🎨 Использование

### Основные функции
1. **📤 Загрузка изображения**  
   Используйте кнопку на панели инструментов

2. **📷 Захват с камеры**  
   Алгоритм работы:
   - Нажмите "Снять с веб-камеры" для запуска трансляции
   - Для сохранения фото нажмите "Остановить"

3. **🌈 Цветовые каналы**  
   Доступные режимы:
   - ❤️ Красный канал
   - 💚 Зеленый канал
   - 💙 Синий канал

4. **⚙️ Операции с изображением**  
   Доступные операции:
   - Изменение размеров (ширина × высота)
   - Коррекция яркости (диапазон 0-100)
   - Добавление синего прямоугольника

## 📦 Сборка проекта

### Создание пакета
```bash
python setup.py sdist bdist_wheel
```

### Создание исполняемого файла
```bash
pip install pyinstaller
pyinstaller --onefile --windowed --name ImageEditor image_editor/app.py
```

## 📁 Структура проекта
```
practices/
├── image_editor/     # Основной пакет
│   ├── __init__.py   # Инициализация
│   ├──main.py       # Главный модуль
│   └── __main__.py 
├── LICENSE           # Лицензия MIT
├── README.md         # Документация
├── requirements.txt  # Список зависимостей
└── setup.py          # Конфигурация сборки
```

## 📚 Зависимости 
Все зависимости указываются в requirements.txt:
- [OpenCV](https://opencv.org/) - работа с изображениями и камерой
- [Pillow](https://python-pillow.org/) - обработка графики
- [NumPy](https://numpy.org/) - математические операции

```text
opencv-python>=4.5
pillow>=9.0
numpy>=1.20
```

## ⚖️ Лицензия
Этот проект распространяется под лицензией MIT. Подробнее см. в файле LICENCE.txt.

