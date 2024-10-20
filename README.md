# Асинхронный парсер PEP на Scrapy
Этот проект представляет собой асинхронный парсер PEP (Python Enhancement Proposals), разработанный с использованием фреймворка Scrapy. Основная задача парсера — извлечение информации о PEP с официального сайта peps.python.org и сохранение данных в формате CSV.

Парсер выполняет следующие функции:

Извлекает список всех PEP, включая номер, название и статус, и сохраняет их в файл pep_ДатаВремя.csv.
Создаёт сводный файл status_summary_ДатаВремя.csv, который содержит информацию о количестве PEP в каждом статусе.

## Использованные технологии
**Scrapy:** мощный фреймворк для асинхронного веб-парсинга.

**Python:** основной язык программирования проекта.

**pytest:** библиотека для тестирования, используемая для написания и выполнения тестов.

**CSV:** формат файлов, в который сохраняется собранная информация о PEP.

## Установка
Клонируйте репозиторий на свой компьютер:

```bash
git clone https://github.com/<ваш_пользователь>/scrapy_parser_pep.git
cd scrapy_parser_pep
```
Создайте новое виртуальное окружение:

```bash
python -m venv venv
```
Активируйте виртуальное окружение:

На Windows:
```bash
venv\Scripts\activate
```

На MacOS/Linux:

```bash
source venv/bin/activate
```
Установите зависимости из файла requirements.txt:

```bash
pip install -r requirements.txt
```
## Запуск проекта
Для запуска парсера выполните команду:

```bash
scrapy crawl pep
```