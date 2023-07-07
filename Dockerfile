FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN python3 -m venv ./venv

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "python3", "manage.py", "runserver" ]
