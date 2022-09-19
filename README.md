REST API сервис для отзывов пользователей на кино, фильмы и музыку.
=====

Описание проекта
----------
Проект YaMDb собирает отзывы пользователей на произведения (книги, фильмы и
музыка). Произведению может быть присвоен жанр из списка предустановленных.
Новые жанры может создавать только администратор.
Пользователи могут оставить к произведениям текстовые отзывы и ставят
произведению оценку. На основании оценок рассчитывается общий рейтинг
произведения.
На одно произведение пользователь может оставить только один отзыв.

Реализован REST API CRUD для моделей проекта, для аутентификации примненяется
JWT-токен.
В проекте реализованы пермишены, фильтрации, сортировки и поиск по запросам
клиентов, а так же пагинация ответов от API.


Системные требования
----------

* Python 3.6+
* Works on Linux, Windows, macOS

Стек технологий
----------

* Python 3.7+
* Django 2.1
* Django Rest Framework
* Simple-JWT
* SQLite3

Установка проекта из репозитория (Linux и macOS)
----------

1. Клонировать репозиторий и перейти в него в командной строке:

```bash
git clone git@github.com:vladdiev/api_yamdb.git

cd api_yamdb
```

2. Cоздать и активировать виртуальное окружение:

```bash
python3 -m venv venv

source env/bin/activate
```

3. Установить зависимости из файла ```requirements.txt```:

```bash
python3 -m pip install --upgrade pip

pip install -r requirements.txt
```

4. Выполнить миграции:

```bash
cd api_yamdb

python3 manage.py migrate
```

5. Запустить проект (в режиме сервера Django):

```bash
python3 manage.py runserver
```

Документация к проекту
----------
Документация для API после установки доступна по адресу

```http://127.0.0.1/redoc/```

# REST API

Примеры запросов приведены ниже.

## Получение списка всех произведений.

### Request

`GET http://127.0.0.1:8000/api/v1/titles/`

### Response

```json
[
  {
    "count": 0,
    "next": "string",
    "previous": "string",
    "results": [
      {
        "id": 0,
        "name": "string",
        "year": 0,
        "rating": 0,
        "description": "string",
        "genre": [
          {
            "name": "string",
            "slug": "string"
          }
        ],
        "category": {
          "name": "string",
          "slug": "string"
        }
      }
    ]
  }
]
```

## Получение списка всех отзывов.

### Request

`GET http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/`

### Response

```json
[
  {
    "count": 0,
    "next": "string",
    "previous": "string",
    "results": [
      {
        "id": 0,
        "text": "string",
        "author": "string",
        "score": 1,
        "pub_date": "2019-08-24T14:15:22Z"
      }
    ]
  }
]
```
# Авторы

* [Vladimir Ananin](https://github.com/vladdiev) 
* [Chernykh Maria](https://github.com/chernyh-mv)
* [Shandalii Dmitrii](https://github.com/FinkTim)