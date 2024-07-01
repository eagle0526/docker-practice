FROM python:3.9-slim

WORKDIR /srv

# COPY index.html /srv/
# COPY project-one/* /srv/
# COPY project-two/* .
COPY projectTwo .
# ENV POETRY_VIRTUALENVS_CREATE=0
RUN pip install -U poetry \
    && poetry install --only main \
    && rm -rf ~/.cache/pypoetry \
    && apt-get update \
    && apt-get install -y nano

