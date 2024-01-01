FROM python:3.10-alpine3.16
WORKDIR /fin_proj
EXPOSE 8000
COPY requirements.txt /temp/requirements.txt
RUN apk add postgresql-client build-base postgresql-dev
RUN pip install -r /temp/requirements.txt
RUN adduser --disabled-password s-user
USER s-user
COPY fin_proj /fin_proj