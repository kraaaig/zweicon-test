FROM python:2-alpine

WORKDIR /usr/src/app

RUN pip install --no-cache-dir flask

COPY . .

EXPOSE 5000

CMD [ "python", "./service.py" ]