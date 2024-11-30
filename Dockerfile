FROM python:3.12-bullseye
ENV PYTHONUNBUFFERED=1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
# Ensure correct line endings and executable permissions
RUN chmod 755 /code/start-django.sh
EXPOSE 8000
ENTRYPOINT [ "/code/start-django.sh" ]
