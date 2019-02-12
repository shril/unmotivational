FROM python:3

RUN apt-get update -y

RUN apt-get install python3-pip -y
RUN pip install --upgrade pip
RUN pip3 install flask
RUN pip3 install waitress
RUN pip3 install requests

RUN mkdir app

COPY . /app

WORKDIR /app

EXPOSE 5000

CMD ["python", "app.py"]