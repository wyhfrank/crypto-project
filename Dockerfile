# https://qiita.com/sebastianrettig/items/a52f6a5c36288db7b823
# https://www.codementor.io/@adammertz/basic-tutorial-using-docker-and-python-1gxmzm43k2

FROM python:3.8-slim-buster AS base

# https://medium.com/rahasak/configure-docker-timezone-in-linux-71893fe51499
ENV TZ Asia/Tokyo

WORKDIR /work

# RUN apk add --no-cache gcc musl-dev linux-headers

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

# Development Stage
FROM base AS dev
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    git \
    && rm -rf /var/lib/apt/lists/*
COPY requirements.dev.txt .
RUN pip install --no-cache-dir -r requirements.dev.txt
# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1


# Production Stage
FROM base AS prod
COPY . .
# COPY requirements.prod.txt .
RUN pip install --no-cache-dir -r requirements.prod.txt
CMD ["gunicorn", "--reload", "--bind", "0.0.0.0:5000", "flasky:app"]
