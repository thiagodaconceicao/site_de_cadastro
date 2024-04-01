FROM python:latest

#ENV DJANGO_SETTINGS_MODULE=projeto_cad_usu.custom_settings.settings-postgres

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt --break-system-packages

CMD [ "python", "manage.py", "runserver" ]
