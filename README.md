## Тестовое задание от UpTrader
##  Для установки:

* Клонировать репозиторий на локальный компьютер
```commandline
git clone https://github.com/Kvezac/special-UpTrader
```
* Установить зависимости
```commandline
pip install -r requirements.txt
```
* Создать миграции на основе моделей
```commandline
python manage.py makemigrations
```
* Выполнить миграции
```commandline
python manage.py migrate
```
* Создать супер пользователя
```commandline
python manage.py createsuperuser
```
* После команды задать имя пользователя, почта(необязательно), пароль
* Запустить локальный хост
```commandline
python manage.py runserver
```
* Перейти по ссылки в терминале