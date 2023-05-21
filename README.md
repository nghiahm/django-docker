# Django Docker

## Setup project
### 1. Clone project
```bash
$ git clone https://github.com/nghiahm/django-docker.git
$ cd django-docker
```
### 2. Create Django environment file
```bash
$ cp app/.env.example app/.env
```

## Run project in Docker
### 1. Update `app/.env` file
```python
# postgres
POSTGRES_HOST=db
```
### 2. Run Django server
```bash
$ docker compose up -d
```
The server runs at: http://0.0.0.0:8000/ \
Login as superuser at: http://0.0.0.0:8000/admin/
- Username: admin
- Password: admin123

## Run project in Local
### 1. Create virtual environment
```bash
$ virtualenv -p python3 <venv_name>
```
### 2. Active virtual environment
```bash
$ source <venv_name>/bin/activate
# result
(venv_name)$ _
```
### 3. Install requirements
```bash
(venv_name)$ pip install -r app/requirements.txt
```
### 4. Update `app/.env` file
```python
# postgres
POSTGRES_HOST=localhost
```
### 5. Run Django server
```bash
(venv_name)$ cd app
(venv_name)$ python manage.py runserver
```
The server runs at: http://localhost:8000/
