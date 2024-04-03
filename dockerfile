FROM python:latest

# ENV DJANGO_SETTINGS_MODULE=projeto_cad_usu.custom_settings.settings-postgres

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt --break-system-packages

# RUN pip install -r requirements.txt --break-system-packages \
#  && python manage.py migrate


CMD [ "python", "manage.py", "runserver" ]
