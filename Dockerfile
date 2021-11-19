FROM ubuntu:latest

RUN apt-get update -y && apt-get install -y python3-pip python3-dev build-essential

COPY my_flask_app /app

WORKDIR /app 

RUN pip3 install -r requirements.txt
CMD ["python3", "main.py"]
