# mainslab

## Задание
client_org.xlsx

Состоит из двух листов client и organization.
В листе client поле name уникально.
В листе organization список компаний клиента (client_name + name уникально).

bills.xlsx

Это список счетов организации клиента. Уникальность по полям client_org и №.
Необходимо реализовать загрузку этих файлов через api и заполнить БД (SQLite или PostgreSQL) находящимися записями.
Условие уникальности записей должно сохраняться и в БД.

Это должно быть api с использованием Django REST framework:
Перед созданием апи потребуются модули: 
- Детектор мошенничества
На вход принимает str, на выходе float рандомно в диапазоне от 0 до 1. При загрузке файла bills.xlsx колонку service пропускать через “Детектор мошенничества” и сохранять это значение в бд под названием fraud_score.

- Классификатор услуг
На вход принимает str, на выходе dict вида {service_class: int, ‘service_name’: str}
Возвращаемый dict формировать путём рандомного выбора пары ключ-значение из этого словаря {1: ‘консультация’, 2: ‘лечение’, 3: ‘стационар’, 4: ‘диагностика’, 5: ‘лаборатория’}, где ключ это service_class, а значение это ‘service_name’.
При загрузке файла bills.xlsx колонку service пропускать через “Классификатор услуг” и сохранять service_class, service_name в бд.

API
1. эндпоинт загрузки файлов bills.xlsx и client_org.xlsx  (может быть по одному на файл, как посчитаете правильным)

2. эндпоинт со списком клиентов
Данные, которые нужно отдавать для каждого элемента списка:
 - Название клиента
 - Кол-во организаций
 - Приход (сумма по счетам всех организаций клиента)

3. эндпоинт со списком счетов с возможностью фильтровать по организации, клиенту.

Дополнительная обработка данных
1. В файле client_org.xlsx есть колонка address. При загрузке строк этого файла обрабатывать колонку следующим образом:
Если не пусто(любой пробельный символ или знак -), то добавлять в начало “Адрес:”.
К примеру: в ячейке этой колонки есть строка “117519, г Москва, ул Кировоградская, д 22Б”, на выходе должны получить “Адрес: 117519, г Москва, ул Кировоградская, д 22Б”

2. Для организации добавить аттрибут fraud_weight. Каждая строка счетов организации где fraud_score >= 0.9 увеличивает это значение на 1.


## Решение
- Клонировать репозиторий 'git clone ...'
- Установить зависимости 'pip install requirements.txt'
- Создать миграции 'python mange.py migrate'
- Создать суперюзера для работы через админку 'python mange.py createsuperuser'
- Загрузить файл client_org перейдя по адресу/api/uploade/
- Загрузить файл bills перейдя по адресу /api/uploade/
- Эндпоинт со списком клиентов /api/clients/
- Эндпоинт со списком счетов /api/check/