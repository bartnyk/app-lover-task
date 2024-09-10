FROM python:3.9

RUN apt-get update && apt-get install -y netcat-openbsd
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
ENV PYTHONUNBUFFERED 1

CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000
