# Тестовое задание группы компаний "МЕГАПОЛИС"

#### Зависимости
- python 3.7
- PostgreSQL 11
- node 12


**Бэкенд** Django 2.2
**Фронтэнд** Vue.js 2.6
**Аутентификация** JWT

Проект тестовый, все приватные ключи открыты: 'megapolis/.env'
Дамп базы данных PostgreSQL также присутствует: 'megapolis.dump'
С целью экономии времени, рефакторинг не делал, Vue на компоненты не разбивал.

### Локальная установка

    git clone https://github.com/dmitrytk/megapolis.git
    cd megapolis
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    cd client
    npm install

Создание базы данных

    psql -U <user>
    create database megapolis;
    \q

Загрузка данных в базу

    pg_restore -C -d megapolis megapolis.dump

Ввод данных пользователя бд

    nano megapolis/.env
    POSTGRES_USER=<user>
    POSTGRES_PASSWORD=<password>

Запуск проекта

    source venv/bin/activate
    python manage.py runserver 127.0.0.1:8000

    cd client
    npm run serve

Сайт доступен по адресу **127.0.0.1:8001**

Данные тестового пользователя с должностью 'EXECUTIVE' вбиты в форму логина.

### Сборка проекта

    cd client
    npm run build
    cd ..
    python manage.py collectstatic --noinput
    python manage.py runserver 127.0.0.1:8000

Сайт доступен по адресу **127.0.0.1:8000**

## API Routes
**GET**

    /api/contracts
    /api/contracts/:contract_id
    /api/contracts/:contract_id/employees
    /api/organization/:organization_id/employees
    /api/auth/user


**POST**

    /api/contracts/:contract_id/employees
    /api/auth/login

**DELETE**

    /api/contracts/:contract_id/employees/:employee_id

## Frontend Routes
    /
    /login
    /profile
    /contracts
    /contracts/:contract_id


#### Лицензия
[MIT](LICENSE.md)
