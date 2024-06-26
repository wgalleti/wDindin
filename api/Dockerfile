FROM python:3.12.4-alpine
LABEL authors="William Galleti <william.galleti@gmail.com>"

RUN \
  apk update && \
  apk add postgresql-dev gcc python3-dev musl-dev zlib-dev jpeg-dev gettext build-base libffi-dev

WORKDIR /api

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PIPENV_VENV_IN_PROJECT 1

COPY Pipfile Pipfile.lock ./

RUN pip install gunicorn
RUN pip install -U pipenv
RUN pipenv install -d --system --deploy --ignore-pipfile

COPY . .

CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]