FROM python:latest

# ENV DJANGO_SETTINGS_MODULE=projeto_cad_usu.custom_settings.settings-postgres

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt --break-system-packages && \
    python manage.py migrate

# RUN pip install -r requirements.txt --break-system-packages \
#  && python manage.py migrate


CMD ["gunicorn", "projeto_cad_usu.wsgi:application"]
