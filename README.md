# Site de Cadastro de Consumidores
Site de cadastro ligado ao banco de dados.


## Como usar
### Usando Docker

Primero edite o ngrok.yml com seu código de autenticação depois execute
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
Execute o seguinte comando
```
python manage.py runserver
```
Depois vai no seu navegador e coloque
```
localhost:8000
```
# Configurações diferentes
## PostgreSQL
em BASH/ZSH (Linux)
```
export DJANGO_SETTINGS_MODULE=projeto_cad_usu.custom_settings.settings-postgres
```
em Powershell (Windows)
```
set DJANGO_SETTINGS_MODULE=projeto_cad_usu.custom_settings.settings-postgres
```
