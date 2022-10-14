FROM python:3.8-slim-buster

COPY my_flask_app /app

WORKDIR /app 

RUN pip3 install -r requirements.txt
CMD ["python3", "main.py"]
