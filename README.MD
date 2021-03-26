# Для запуска миграций

```cmd

python manage.py makemigrations # Если хотите сгенерировать новые

python manage.py migrate
```

# Для админки 

Создаем пользователя

```cmd

python manage.py createsuperuser

```

Переходим на [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin) 

Тестим [http://127.0.0.1:8000/news](http://127.0.0.1:8000/news) 