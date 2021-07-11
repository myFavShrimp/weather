FROM python:3.9-buster

WORKDIR /app

COPY . .

EXPOSE 5000

RUN pip3 install -r requirements.txt

CMD [ "python3", "run.py"]
