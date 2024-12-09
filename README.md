# Forms check

## Описание
Form check это Web-приложение для определения заполненных форм, сделанное на FastAPI. 
В ответе возвращается имя шаблона который соответствует полям который совпал с полями в присланной форме.<br> 

## Установка
Присутствует возможность запуска по одному из двух вариантов(Можно выбрать любой из вариантов,какой проще для вас):<br>
-Общее для двух вариантов необходимо установить docker и docker-compose, Git [Установка Docker](https://docs.docker.com/engine/install/)<br>
-[Установка Git](https://git-scm.com/downloads)<br>
-Скачать код с репозитория для этого зайти в терминал:<br>
-Пройти в директорию по вашему выбору<br>
Пример:<br>
```
cd Загрузки
```
-Выполнить команду:<br>
```
git clone https://github.com/JolyCougar/FastApi_form_check.git
```
-Перейти в созданную папку:<br>
```
cd FastApi_form_check
```
## Вариант 1(с использованием docker-compose):<br>
-Набираем в терминале следующую команду:<br>
```
docker-compose up --build
```
или следующую команду и тогда сразу можно вводить команду для запуска пробного запроса.<br>
```
docker-compose up --build -d
```
-Приложение запущенно!<br>
-(Вариант 1)Что бы использовать пробные запросы необходимо создать ещё вкладку в терминале и снова перейти в директорию куда вы скачали приложение и ввести команду:<br>
```
python app/tests/test_requests.py
```
-(Вариант 2)Что бы использовать пробные запросы необходимо создать ещё вкладку в терминале и ввести следующие команды:<br>
```
docker ps
```
Нам выведется список запущенных контейнеров, нам неодбходим контейнер с именем fastapi_form_check-app точнее его CONTAINER ID<br>
-Дальше вводим команду:<br>
```
docker exec -it CONTAINER_ID /bin/bash
```
Вместо CONTAINER_ID подставить ID, который вы увидели в прошлом пункте<br>
-Вводим команду:<br>
```
python app/tests/test_requests.py
```
-В ответе получим результат тестовых запросов.<br>

## Вариант 2 (Без использвания docker-compose):<br>
Здесь будет описываться вариант когда виртуальное окружение venv у вас уже активированно.<br>
-Устанавливаем зависимости :<br>
```
pip instal -r requirements.txt
```
-Открываем вторую вкладку терминала и вводим команду для запуска MongoDB в docker:<br>
```
docker run --name my-mongo -d -p 27017:27017 mongo
```
-Переходим в первую вкладку и выполняем команду:<br>
```
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload --log-level info

```
-Что бы использовать пробные запросы необходимо создать ещё вкладку(или перейти в созданную ранее 2-ю вкладку) в терминале,
снова перейти в директорию куда вы скачали приложение(если вы создали новую вкладку) и ввести команду:<br>
```
python app/tests/test_requests.py
```