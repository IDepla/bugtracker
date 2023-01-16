FROM postgres:14.3-alpine


COPY ./setup-master.sh /docker-entrypoint-initdb.d/setup-master.sh
COPY ./sql/schema.sql /docker-entrypoint-initdb.d/db.sql
RUN chmod 0666 /docker-entrypoint-initdb.d/setup-master.sh
