# wDindin

Sistema de gerenciamento financeiro pessoal para treinamento

## Stack utilizada

**Front-end:** Vue3, Vuetify3, TailwindCSS

**Back-end:** Python, Django, Django Rest Framework, Pytest

## Variáveis de Ambiente

Para rodar esse projeto, você vai precisar adicionar as seguintes variáveis de ambiente no seu .env da pasta `api`

- SECRET_KEY
  - Rode no terminal `python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`
- DEBUG
  - `True`
- ALLOWED_HOSTS
  - `*`
- EXPIRATION*DELTA: \_Dias de validade do token JWT*
  - `10`
- CRYPTOGRAPHY_KEY
  - Rode no terminal `python -c 'from cryptography.fernet import Fernet; key = Fernet.generate_key(); print(key.decode())'`
- DATABASE_URL
  - `postgres://{USER}:{PASS}@{HOST}:{PORT}/{DB}`
  - Se não ajustar o docker-compose.yml ficara `postgres://wdindin:wdindin@postgres:5432/wdindin`

Para rodar esse projeto, você vai precisar adicionar as seguintes variáveis de ambiente no seu .env da pasta `web`

## Instalação

## Rodando local

> Dependencias

- Python 3.12
- Node 20
- Postgres 16

### API

```bash
pip install pipenv
export PIPENV_VENV_IN_PROJECT=1

git clone git@github.com:wgalleti/wDindin.git
cd wDindin/api

echo 'SECRET_KEY=GENERATE_YOUR_SECRET
DEBUG=True
ALLOWED_HOSTS=*
EXPIRATION_DELTA=10
CRYPTOGRAPHY_KEY=GENERATE_YOUR_CRYPTKEY
DATABASE_URL=postgres://wdindin:wdindin@postgres:5432/wdindin' > .env

# DJANGO SECRET KEY
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
# CHANGE YOUR SECRET_KEY .env

# CRIPTO KEY
python -c 'from cryptography.fernet import Fernet; key = Fernet.generate_key(); print(key.decode())'
# CHANGE YOUR CRYPTOGRAPHY_KEY .env

pipenv sync -d
pipenv run python manage.py migrate
pipenv run python manage.py createsuperuser
pipenv run python manage.py runserver
```

### Frontend

```bash
cd wDindin/web
npm i
echo 'VITE_APP_BASE_URL=http://localhost:8000/' > .env
npm run dev
```

## Docker

> Dependencias

- Python 3.12
- Docker
- Docker compose

```bash
pip install django fernet

git clone git@github.com:wgalleti/wDindin.git
cd wDindin

echo 'SECRET_KEY=GENERATE_YOUR_SECRET
DEBUG=True
ALLOWED_HOSTS=*
EXPIRATION_DELTA=10
CRYPTOGRAPHY_KEY=GENERATE_YOUR_CRYPTKEY
DATABASE_URL=postgres://wdindin:wdindin@postgres:5432/wdindin' > api/.env

# DJANGO SECRET KEY
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
# CHANGE YOUR SECRET_KEY api/.env

# CRIPTO KEY
python -c 'from cryptography.fernet import Fernet; key = Fernet.generate_key(); print(key.decode())'
# CHANGE YOUR CRYPTOGRAPHY_KEY api/.env

echo 'VITE_APP_BASE_URL=http://api.wdindin.io' > web/.env

docker compose up -d
docker compose exec api python manage.py createsuperuser
```

Para acessar a aplicação que será servida pelo nginx, criar um fake dns no `/etc/hosts` no linux/mac ou `C:\windows\system\drivers\etc\hosts` no windows:

```
127.0.0.1 api.wdindin.io
127.0.0.1 www.wdindin.io
```
