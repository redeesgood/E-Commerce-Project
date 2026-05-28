# SauceDemo E2E Test Automation Framework

Полноценный тестовый фреймворк для автоматизации E-commerce платформы (SauceDemo). Проект демонстрирует выстроенную архитектуру, интеграцию с базой данных, работу с API и покрытие UI-слоя сквозными (E2E) тестами.

## Технологический стек
* **Язык:** Python 3.11
* **Тестовый фреймворк:** Pytest
* **UI Автоматизация:** Playwright (Page Object Model)
* **API Автоматизация:** Requests
* **База данных:** SQLite
* **Генерация данных:** Faker
* **Статический анализ:** Mypy, Ruff
* **Отчетность:** Allure Report
* **CI/CD:** GitHub Actions

## Ключевые особенности (Features)
* **Надежный UI-слой:** Использование паттерна Page Object Model (POM) и Web-First Assertions (Playwright `expect`).
* **Финансовая точность:** Проверки корзины и расчета налогов (Tax) с использованием библиотеки `Decimal` для предотвращения багов с плавающей точкой (float).
* **Управление сессиями:** Проверка истечения времени сессии (Session Expiration) путем принудительной манипуляции с cookies браузера.
* **Генерация тестовых данных:** Динамическое создание уникальных данных пользователя для оформления заказа (Faker).
* **Автоматизированный CI/CD:** Пайплайн настроен на запуск тестов и линтеров при каждом push/pull_request в ветку `master` с безопасным пробросом секретов окружения (API Keys).

## Структура проекта
├── .github/workflows/   # CI/CD пайплайны GitHub Actions
├── pages/               # Классы Page Object для UI (Inventory, Cart, Checkout и др.)
├── tests/               # Директория с автотестами (UI и API)
├── .env                 # Переменные окружения и секреты (не коммитится)
├── pytest.ini           # Конфигурация запуска Pytest
├── requirements.txt     # Зависимости проекта
└── README.md            # Документация проекта

## Установка и локальный запуск
1. Склонируйте репозиторий:
```bash
git clone [https://github.com/](https://github.com/)[ТВОЙ_GITHUB_USERNAME]/[НАЗВАНИЕ_РЕПОЗИТОРИЯ].git
cd [НАЗВАНИЕ_РЕПОЗИТОРИЯ]
```

2. Создайте и активируйте вирутальное окружение:
```bash
python -m venv venv
venv\Scripts\activate
```

3. Установите зависимости проекта:
```bash
pip install -r requirments.txt
```

4. Установите браузеры для Playwright:
```bash
playwright install chromium
```

5. Запустите автотесты:
```bash
pytest tests/ -v -alluredir=allure-results
```

6. Если захотите посмотреть отчётность, то выполните:
```bash
allure serve allure-results
```