FROM postgres:latest

COPY ./postgres-db.sql /docker-entrypoint-initdb.d 
