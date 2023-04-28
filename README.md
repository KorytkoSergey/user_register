<h1>Аутентификация пользователя с использованием FastAPI, MongoDB, Docker Compose</h1>
<h2>Конвертер из csv в json и из json в csv</h2> 

<b>Как установить</b> 

Сначала вам нужно git клонировать файлы, введя в свой терминал:

<code>
$ git clone 
</code>

Запустить приложение

<code>
$ docker-compose up -d
</code>

Приведенная выше команда создаст образы и запустит контейнеры (2 образа и 2 контейнера — один для приложения FastAPI и один для базы данных MongoDB).

Для визуализации приложения откройте браузер и введите: http://127.0.0.1/docs

В каталоге приложения в <code>main.py</code> файле делаем импорт всех зависимостей и маршрутизаторов из одноименных файлов, расположенных в <code>src</code>каталоге.

<code>src</code>Каталог — это тот, который содержит все необходимые модели <code>pydantic</code> (<code>models.py</code>), базу данных и переменные аутентификации (<code>settings.py</code>).

Аутентификация производится по <code>bearer</code> схеме с <code>token</code> созданием и использованием.

<code>dependecies.py</code>- это файл, содержащий функции аутентификации (я также создал промежуточное программное обеспечение аутентификации, расположенное в <code>main.py</code> файле в корневом каталоге, используя <code>basic</code> схему, эта функция служит только в качестве примера).

<b>Ковектер файлов</b>

Простой скрипт, который загружает, обрабатывает и выгружает файл в нужном формате.

<code>conv</code> содержит <code>csv_or_json.py</code>, который является самим скриптом.
<code>load_xml</code> скрипт загрузки файла формата xml. В дальйшем данный скрипт перейдет в <code>csv_or_json.py</code>
<code>iris.csv</code>, <code>iris.json</code> и <code>exp.xml</code> файлы для тестов
