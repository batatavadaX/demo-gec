FROM python:3-slim

WORKDIR /usr/src/app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 6996

CMD ["bash", "Creatus-est" ]
