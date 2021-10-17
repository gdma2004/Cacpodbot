FROM python:3.8-slim-buster

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT [ "sh" ]

CMD [ "loop.sh" ]