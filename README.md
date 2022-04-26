# simple-chat
API простого чата, реализованный на фреймворке FastAPI с помощью асинхронных библиотек

Структура проекта.

.

- migrations\
- sql-app\
  - __init__.py
  - crud.py
  - database.py
  - main.py
  - models.py
  - schemas.py
  - test_main.py
- .env
- .gitignore
- alembic.ini
- main.py
- README.md
- requirements.txt

## Если хочется проверить на своём устройстве

В файле .env хранится переменная SQLALCHEMY_DATABASE_URL.

Для миграций использовался alembic. После выполнения

	alembic init -t async migrations 

необходимо отредактировать файлы alembic.ini и migrations\env.py.

При разработке использовал uvicorn. При выполнении

	uvicorn sql_app.main:app --reload

запросы доступны по адресу http://localhost:8000/docs