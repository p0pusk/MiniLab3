FROM python:3.10-slim

WORKDIR /mini_lab_3
COPY ./requirements.txt .
COPY . .
RUN pip install -r ./requirements.txt

ENV PORT=6969

CMD [ "python", "backend/main.py" ]
