Проект представляет собой простой тренировочный веб-сервис для заметок.
Поддерживает:
    - Авторизацию (почта+пароль)
    - Создание заметки
    - Редактирование заметки
    - Удаление заметки
    - Восстановление заметки из корзины
    - Форматирование текста 
    - Пункты
    - Различные темы
    - Рисование 
    - Создание таблиц
    - Подключение других сервисов через API
    - Подключение AI-моделей 

Стек:
    - Python 3.12
    - FastAPI
    - PostgreSQL
    - SQLAlchemy 2.0
    - React


Цель проекта - обучение вышеперечисленному стеку 

Архитектура:
    - База данных (пока синхронная):
        - Формируется через SQLAlchemy
        - Модели:
            User:
                - id
                - email
                - password_hash
                - created_at

            Note:
                - id
                - user_id
                - title
                - content
                - content_type
                - is_deleted
                - deleted_at
                - created_at
                - updated_at

            UserSettings:
                - id
                - user_id
                - theme
                - editor_settings
                - ai_enabled

    - Эндпоинты:
        POST   /auth/register
        POST   /auth/login
        GET    /users/me

        GET    /notes
        GET    /notes/{note_id}
        POST   /notes
        PATCH  /notes/{note_id}
        DELETE /notes/{note_id}

        GET    /notes/deleted
        GET    /notes/deleted/{note_id}
        PATCH  /notes/{note_id}/restore

        GET    /settings
        PATCH  /settings

    - Валидация:
        - Пользователь 
        - Заметка

    - Сервисы - в планах (AI...)

    - Фронтенд:
        - React + Tailwind + CSS


Пример действия (алгоритм):
    1. Пользователь открывает React-приложение
    2. Если JWT нет — показываем страницу входа
    3. Пользователь вводит email и пароль
    4. Frontend отправляет POST /auth/login
    5. Backend проверяет пароль
    6. Backend возвращает access_token
    7. Frontend сохраняет JWT
    8. Все следующие запросы идут с заголовком:

    Authorization: Bearer <token>
    

Главная идея архитектуры:
    Frontend отвечает за интерфейс.
    FastAPI отвечает за API и бизнес-логику.
    SQLAlchemy отвечает за работу с БД.
    PostgreSQL хранит данные.
    JWT отвечает за авторизацию.
    Services отвечают за действия.
    Repositories отвечают за запросы в БД.

Структура проекта:
            backend/
        ├── app/
        │   ├── main.py
        │   ├── core/
        │   │   ├── config.py
        │   │   ├── security.py
        │   │   └── database.py
        │   │
        │   ├── models/
        │   │   ├── user.py
        │   │   ├── note.py
        │   │   └── settings.py
        │   │
        │   ├── schemas/
        │   │   ├── user.py
        │   │   ├── note.py
        │   │   └── settings.py
        │   │
        │   ├── repositories/
        │   │   ├── user_repository.py
        │   │   └── note_repository.py
        │   │
        │   ├── services/
        │   │   ├── auth_service.py
        │   │   ├── note_service.py
        │   │   └── ai_service.py
        │   │
        │   ├── api/
        │   │   ├── auth.py
        │   │   ├── notes.py
        │   │   ├── users.py
        │   │   └── settings.py
        │   │
        │   └── dependencies/
        │       └── auth.py