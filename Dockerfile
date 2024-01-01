FROM python:3.10-alpine3.16

COPY requirements.txt /temp/requirements.txt
COPY fin_proj /fin_proj
WORKDIR /fin_proj
EXPOSE 8000
RUN pip install -r /temp/requirements.txt
RUN adduser --disabled-password s-user
USER s-user
