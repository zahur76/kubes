FROM python:3.9-slim-buster

# Do not cache Python packages
ENV PIP_NO_CACHE_DIR=yes

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

# set PYTHONPATH
ENV PYTHONPATH "${PYTHONPATH}:/code/"

# Initializing new working directory
WORKDIR /code

# Transferring the code and essential data
COPY config ./config
COPY kubes ./kubes
COPY Pipfile ./Pipfile
COPY Pipfile.lock ./Pipfile.lock
COPY app.py ./app.py

RUN pip install pipenv
RUN pipenv install --ignore-pipfile --system