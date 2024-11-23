FROM python:3.12-bullseye
ENV PYTHONUNBUFFERED=1

RUN mkdir /code

WORKDIR /code

RUN pip install poetry

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

ENTRYPOINT [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
