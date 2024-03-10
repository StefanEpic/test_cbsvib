FROM python:3.10-alpine

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR ./backend

COPY . .
COPY requirements.txt .

RUN python3 -m pip install --no-cache-dir -r requirements.txt
