FROM python:3.8-slim-buster

ARG USERNAME=django
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN apt-get update && apt-get -y install libgdal-dev gettext

COPY requirements.txt /app/

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME 

RUN python3 -m pip install --no-cache-dir pip --upgrade \
    && python3 -m pip install --no-cache-dir -r /app/requirements.txt 

USER $USERNAME


COPY . /app/

WORKDIR /app