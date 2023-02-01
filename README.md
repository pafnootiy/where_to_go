# Куда пойти — Москва глазами Артёма

Фронтенд для будущего сайта о самых интересных местах в Москве. Авторский проект Артёма.

 ![site](https://user-images.githubusercontent.com/66752812/215351770-4de024d2-4144-4995-adb5-005559324db3.png)


 
# Общая информация
Проект доступен по ссылке: https://pafnootiy.pythonanywhere.com

Панель администратора: https://pafnootiy.pythonanywhere.com/admin


Это код первого урока в курсе по Python и веб-разработке на сайте Devman

Тестовые данные взяты с сайта KudaGo.

Инструкция по локальному запуску (для разработчика)
Перед запуском см. Переменные окружения

Скачать репозиторий:

git clone https://github.com/pafnootiy/where_to_go.git

Перейти в папку проекта:

cd where_to_go
Создать и активировать виртуальное окружение удобным для вас способом:
например, через virtualenv

python3 -m venv <your-venv-name>

source <your-venv-name>/bin/activate
Установить зависимости:

pip install -r requirements.txt
Запустить миграции:

   python manage.py migrate
Запустить сервер:

   python manage.py runserver
Сайт запущен на локалхосте по адресу http://127.0.0.1:8000. Теперь можно создать суперюзера...

   python manage.py createsuperuser
...и зайти в админку по адресу: http://127.0.0.1:8000/admin/

Пока на сайте нет локаций. Чтобы поместить локацию на карту, запустите скрипт cо ссылкой на файл локации:

   python manage.py load_place <link>
Ссылки можно взять тут.
Чтобы добавить сразу все локации из файла, запустите команду:

python manage.py load_place links.txt
Либо добавьте локации вручную через админ-панель.





