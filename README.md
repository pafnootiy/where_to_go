# Куда пойти — Москва глазами Артёма

Фронтенд для будущего сайта о самых интересных местах в Москве. Авторский проект Артёма.

 ![site](https://user-images.githubusercontent.com/66752812/215351770-4de024d2-4144-4995-adb5-005559324db3.png)




# where_to_go

Сайт-интерактивная карта с самыми интересными местами Москвы для посещения.
Представляет собой карту Москвы, на которой отмечены интересные места. При
щелчке на конкретное место открываются подробности и фотографии.

[Тестовая версия сайта](http://pafnootiy.pythonanywhere.com/)  

 
## Как запустить

Для запуска сайта вам понадобится Python 3.8+ версии. Скачайте код с GitHub.
Затем установите зависимости

```sh
pip install -r requirements.txt
```

Создайте .env файл по шаблону в папке .env.template и заполните вашими данными,без кавычек.
```sh
SECRET_KEY=fill-this-string-with-your-your-secret-key-!
localhost=127.0.0.1
DEBUG=True

```


Проведите миграции

```shell
python3 manage.py migrate
```

Запустите сервер

```sh
python3 manage.py runserver
```

Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Заполняем базу данных тестовыми данными

Добавьте через административную панель несколько локаций. Или воспользуйтесь
**менеджмент-командой**:

```sh
python manage.py load_place url
```

, где `url` - адрес json файла в формате  **http://адрес/файла.json**. Можно
указать несколько через пробел `url1 url2 ... url_n`.
[Примеры файлов](https://github.com/devmanorg/where-to-go-places/tree/master/places)

## Возможности админки

- добавлять локации (описание, координаты)
- добавлять и сортировать фотографии
- редактор текста WYSIWYG

### Разное

* [Leaflet](https://leafletjs.com/) — отрисовка карты
* [loglevel](https://www.npmjs.com/package/loglevel) для логгирования
* [Bootstrap](https://getbootstrap.com/) — CSS библиотека
* [Vue.js](https://ru.vuejs.org/) — реактивные шаблоны на фронтенде
* Код написан в учебных целях [Devman](https://dvmn.org/)
* Тестовые данные взяты с сайта [KudaGo](https://kudago.com/)



