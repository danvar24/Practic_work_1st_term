from setuptools import setup, find_packages
from pathlib import Path

def get_version():
    version_file = Path(__file__).parent / "image_editor" / "__init__.py"
    with version_file.open(encoding="utf-8") as f:
        for line in f:
            if line.startswith("__version__"):
                return line.split("=")[1].strip().strip('"\'')
    return "1.0.0"

# Чтение README
readme_path = Path(__file__).parent / "README.md"
long_description = (
    readme_path.read_text(encoding="utf-8")
    if readme_path.exists()
    else "Графический редактор изображений с поддержкой веб-камеры"
)

setup(
    name="image-editor-danvar24",
    version=get_version(),
    author="Иванов Даниил",
    author_email="Legonn2006@gmail.com",
    description="Графический редактор изображений с поддержкой веб-камеры",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/danvar24/Practic_work_1st_term",
    project_urls={
        "Bug Tracker": "https://github.com/danvar24/Practic_work_1st_term/issues",
    },
    packages=find_packages(exclude=["tests*"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Multimedia :: Graphics :: Editors",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "opencv-python>=4.5,<5.0",
        "Pillow>=9.0,<10.0",
        "numpy>=1.20,<2.0"
    ],
    entry_points={
        "console_scripts": [
            "image-editor=image_editor.main:main",
            "ie-danvar=image_editor.main:main",
        ],
    },
    include_package_data=True,
    package_data={
        "image_editor": ["*.txt", "*.md", "*.png", "*.ico", "*.ui"],
    },
    options={
        "bdist_wheel": {
            "universal": False
        }
    },
    zip_safe=False,
)