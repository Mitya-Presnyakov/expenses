Содержание выполненного задания можно посмотреть в файле `Задание.pdf`.

**Запуск приложения:**
1. Перейдите в папку проекта:

    ```cd путь/к/папке/проекта```

2. Запустите приложение с помощью Docker Compose:

    ```docker-compose up```

3. Создайте и примените миграции:

   - Подключитесь к контейнеру веб-приложения:

        ```docker exec -it expenses-web bash```

   - Внутри контейнера создайте и примените миграции:

        ```python manage.py makemigrations```

        ```python manage.py makemigrations app```

        ```python manage.py migrate```

\
**Создание пользователей:**
1. Подключитесь к контейнеру веб-приложения

    ```docker exec -it expenses-web bash```

2. Создайте администратора:

    ```python manage.py createsuperuser```

3. Перейдите в [Django Admin](localhost:8000/admin/), введите логин и пароль администратора и добавьте пользователей в таблицу Users

\
**Авторизация**

*Получение токенов*

Запрос:
    
    POST /api/token/
    Content-Type: application/json

    {
        "username": "имя_пользователя", 
        "password": "пароль"
    }

Ответ:
    
    {
        "refresh": "refresh_token",
        "access": "access_token"
    }

\
*Обновление access-токена:*

Запрос:

    POST /api/token/
    Content-Type: application/json

    {
        "refresh": "refresh_token"
}

Ответ:

    {
        "refresh": "refresh_token",
        "access": "access_token"
    }