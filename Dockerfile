FROM python:3.10.6

WORKDIR /usr/app/src

COPY /src ./
COPY install.sh ./
COPY Pipfile ./
COPY arquivo.json /usr/app/

RUN chmod +x ./install.sh

RUN ./install.sh

CMD ["pipenv", "run", "python", "./main.py"]