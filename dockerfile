FROM python:latest

# ENV DJANGO_SETTINGS_MODULE=config.custom_settings.settings-postgres

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt --break-system-packages && \
    python manage.py migrate

# RUN pip install -r requirements.txt --break-system-packages \
#  && python manage.py migrate


CMD ["gunicorn", "config.wsgi:application", "--bind 0.0.0.0:8000"]
