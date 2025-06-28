from setuptools import setup, find_packages
from pathlib import Path

# Чтение README.md
readme_path = Path(__file__).parent / "README.md"
long_description = readme_path.read_text(encoding="utf-8")

setup(
    name="image_editor",
    version="1.0.0",
    author="Иванов Даниил",
    author_email="Legonn2006@gmail.com",
    description="Графический редактор изображений с поддержкой веб-камеры",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/danvar24/Practic_work_1st_term",
    packages=find_packages(),  # Изменено - ищем пакеты в корне
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Multimedia :: Graphics :: Editors"
    ],
    python_requires=">=3.7",
    install_requires=[
        "opencv-python>=4.5,<5.0",
        "Pillow>=9.0,<10.0",
        "numpy>=1.20,<2.0"
    ],
    entry_points={
        "console_scripts": [
            "image-editor=image_editor.main:main",  # Соответствует вашей структуре
        ],
    },
    include_package_data=True,
    package_data={
        "image_editor": ["*.txt", "*.md", "*.png", "*.ico"],
    },
    options={
        "bdist_wheel": {
            "universal": True
        }
    },
)