# Site de Cadastro de Consumidores
Site de cadastro ligado ao banco de dados.


## Como usar
### Usando Docker

Primero crie uma conta no site do [ngrok] e edite o ngrok.yml com seu código de autenticação depois execute
```
docker compose up -d
```
Vá na url do seu navegador e coloque
```
0.0.0.0:4040/status
```
Copie a URL que estiver lá e coloque em outra aba

### Sem Docker
Instale as dependências do projeto
```
pip install -r requirements.txt
```
crie o SQLite
```
python manage.py migrate
```
Execute o seguinte comando
```
python manage.py runserver
```
Depois vai no seu navegador e coloque
```
localhost:8000
```
OBS: recomendo instalar em ambientes virtuais isolados
# Configurações diferentes
## PostgreSQL
Em BASH/ZSH (Linux)
```
export DJANGO_SETTINGS_MODULE=config.custom_settings.settings-postgres
```
em Powershell (Windows)
```
set DJANGO_SETTINGS_MODULE=config.custom_settings.settings-postgres
```
### Postgres no Docker
Descomente a variavel *ENV* do dockerfile e o *RUN* e comente a outra, depois vá no docker-compose.yml e descomente o serviço postgres e edite como conforme desejar.
Descomente o postgres-gui se quiser usar o pgAdmin4 para configurar/ver as tabelas via interface gráfica

[ngrok]: https://ngrok.com
