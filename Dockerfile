FROM docker.io/python:3.10-buster

# Install Python
RUN apt-get update && apt-get install -y python3 python3-pip




WORKDIR /app
ADD ./ /app
COPY ./requirements.txt requirements.txt
RUN apt-get -yq update && pip3 install --no-cache-dir -r requirements.txt

COPY . .

WORKDIR /app

RUN pip3 install requests

ENTRYPOINT ["python3", "src/app.py"]
