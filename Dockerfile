
FROM python:3.7.6-buster AS base

WORKDIR /work

# RUN apk add --no-cache gcc musl-dev linux-headers

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_ENV="docker"
ENV FLASK_APP=app.py
EXPOSE 5000

# Development Stage
FROM base AS develop

# ENV FLASK_RUN_HOST=0.0.0.0

# RUN pip install debugpy
COPY requirements.dev.txt .
RUN pip install --no-cache-dir -r requirements.dev.txt
# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1
# CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

# Production Stage
FROM base AS production
COPY requirements.prod.txt .
RUN pip install --no-cache-dir -r requirements.prod.txt
# RUN pip install --no-cache-dir gunicorn
COPY . .
CMD ["gunicorn", "--reload", "--bind", "0.0.0.0:5000", "app:app"]