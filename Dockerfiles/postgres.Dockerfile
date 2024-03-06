FROM postgres:latest

COPY ../docker-entrypoint-initdb.d/postgres-db.sql /docker-entrypoint-initdb.d 
