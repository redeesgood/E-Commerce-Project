# 🛒 SauceDemo E2E Test Automation Framework

Тестовый фреймворк для автоматизации E-commerce платформы (SauceDemo). Проект демонстрирует выстроенную архитектуру, работу с API, покрытие UI-слоя надежными сквозными (E2E) тестами и полную контейнеризацию

## 🛠 Технологический стек
* **Язык:** Python 3.12
* **Тестовый фреймворк:** Pytest
* **UI Автоматизация:** Playwright (Page Object Model)
* **API Автоматизация:** Requests
* **База данных:** SQLite
* **Генерация данных:** Faker
* **Статический анализ:** Mypy, Ruff
* **Отчетность:** Allure Report
* **CI/CD & Инфраструктура:** GitHub Actions, Docker, Docker Compose

## 🚀 Ключевые особенности (Features)
* **Надежный UI-слой:** Использование паттерна Page Object Model (POM) и Web-First Assertions (Playwright `expect`).
* **Финансовая точность:** Жесткие проверки корзины и расчета налогов (Tax) с использованием встроенной библиотеки `Decimal` для предотвращения багов с плавающей точкой (float).
* **Управление сессиями:** Проверка истечения времени сессии (Session Expiration) и безопасности логаута путем манипуляции с cookies браузера.
* **Генерация тестовых данных:** Динамическое создание уникальных данных пользователя для оформления заказа (Faker).
* **Автоматизированный CI/CD:** Пайплайн настроен на запуск тестов и линтеров при каждом push/pull_request в ветку `master` с безопасным пробросом секретов окружения (API Keys).
* **Контейнеризация (Docker):** Проект полностью упакован в Docker-контейнер для независимого запуска на любой операционной системе без локальной настройки окружения.

## 📁 Структура проекта
```text
├── .github/workflows/   # CI/CD пайплайны GitHub Actions
├── pages/               # Классы Page Object для UI (Inventory, Cart, Checkout и др.)
├── tests/               # Директория с автотестами (UI и API)
├── Dockerfile           # Инструкция по сборке образа
├── docker-compose.yml   # Конфигурация для быстрого запуска контейнера
├── .env                 # Переменные окружения и секреты (не коммитится)
├── pytest.ini           # Конфигурация запуска Pytest
├── requirements.txt     # Зависимости проекта
└── README.md            # Документация проекта
```

# Быстрый запуск через Docker 

Если вы не хотите устанавливать Python, зависимости и браузеры на свой компьютер, вы можете запустить тесты в изолированном контейнере, нужен только установленный Docker Desktop.

1. Склонируйте репозиторий и перейдите в папку:
```bash
git clone https://github.com/redeesgood/E-Commerce-Project.git
cd E-Commerce-Project
```

2. Запустите сборку и прогон тестов:
```bash 
docker compose up --build
```

3. После завершения сгенерируйте Allure-отчёт
```bash
allure serve allure-results
```

# Локальная установка

1. Склонируйте репозиторий и перейдите в папку:
```bash
git clone https://github.com/redeesgood/E-Commerce-Project.git
cd E-Commerce-Project
```

2. Создайте виртуальное окружение
```bash
python -m venv venv
```

3. Активируйте виртуальное окружение
```bash
# Для Windows (PowerShell):
.\venv\Scripts\activate

# Для Windows (Git Bash):
source venv/Scripts/activate
```
4. Установите зависимости проекта
```bash
pip install -r requirements.txt
```

5. Установите зависимости браузеров для Playwright:
```bash
playwright install chromium
```
6. Запустите автотесты
```bash
pytest tests/ -v --alluredir=allure-results
```

7. После завершения сгенерируйте Allure-отчёт
```bash
allure serve allure-results
```

