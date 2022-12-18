FROM library/python:3.7-slim

COPY requirements.txt /app/
COPY server.py /app/

WORKDIR /app

RUN pip3.7 install -r requirements.txt

EXPOSE 8080


CMD ["python3.7", "server.py"]

