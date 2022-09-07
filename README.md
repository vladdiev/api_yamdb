REST API сервис для отзывов пользователей на кино, фильмы и музыку (Яндекс.Практикум)
=====

Описание проекта
----------
Проект в рамках учебного курса Яндекс.Практикум.

Проект YaMDb собирает отзывы пользователей на произведения (книги, фильмы и музыка). Произведению может быть присвоен жанр из списка предустановленных.
Новые жанры может создавать только администратор.
Пользователи оставляют к произведениям текстовые отзывы
и ставят произведению оценку в диапазоне от одного до десяти (целое число). На основании оценок рассчитывается общий рейтинг произведения.
На одно произведение пользователь может оставить только один отзыв.

Спецификация OpenAPI: http://127.0.0.1:8000/redoc

Запросы API начинаются с `/api/v1/`