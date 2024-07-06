FROM python:3.8-alpine

RUN apk add --no-cache postgresql-dev gcc python-dev musl-dev

WORKDIR /app

COPY . /app 

WORKDIR /app 

RUN pip install -r requirements.txt

ENV PORT 5000

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
