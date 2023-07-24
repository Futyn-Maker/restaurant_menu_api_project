# API для меню ресторана

**Учебный проект, выполненный в рамках курса [Основы Python](https://university.ylab.io/python_basics) от Y_LAB**

## О чём это всё?

В данном репозитории находится мой пример реализации простейшего API для управления меню ресторана. Сервер написан с использованием Python, FastAPI и PostgreSQL (со SQLAlchemy в качестве ORM). Сейчас поддерживаются все операции с меню, подменю и блюдами, которые находятся в подменю (но не в меню напрямую). Меню, подменю и блюда можно создавать, просматривать, изменять и удалять с помощью простых HTTP-запросов.

## Как развернуть?

Очень просто!

1. [Установить Docker](https://docs.docker.com/engine/install/), если по какой-то удивительной причине ещё не.
2. Клонировать репозиторий проекта: `git clone https://github.com/Futyn-Maker/restaurant_menu_api_project.git`.
3. Перейти в директорию проекта: `cd restaurant_menu_api_project`.
4. Развернуть с использованием Docker: `docker compose up`. Если есть потребность запустить сервер в режиме демона, то: `docker compose up -d`.
5. При первом запуске подождать (возможно, долго), пока всё соберётся. Потом запуск будет быстрым.
6. Пользоваться сервером. Начальная точка входа в API будет здесь: `http://127.0.0.1:8000/api/v1/menus`.

При необходимости изменить имя пользователя или пароль БД или название БД меняем соответствующие переменные в `docker-compose.yml`.

Автоматически созданная документация по методам API, примеры запросов и ответов есть тут: http://127.0.0.1:8000/docs.

## Немного про код

* `main.py` - собственно маршруты, само FastAPI-приложение и основная логика;
* База данных:
  * `database.py` - инициализация БД, вспомогательные функции для управления БД из других модулей;
  * `db_models.py` - схема базы данных, описания всех таблиц и связей;
  * `crud.py` --- реализация всех CRUD-операций;
* `api_models.py` - схема запросов к API и ответов от него;
* `db2api.py` - функции, которые конвертируют модель БД в модель ответа от API;
* `depends.py` - вспомогательные функции, проверяющие существование элементов в БД и возвращающие подходящие ошибки в случае необходимости.
