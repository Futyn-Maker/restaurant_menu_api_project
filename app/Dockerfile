# pull the official docker image
FROM python:3.9

# set work directory
WORKDIR /app

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY ./requirements.txt /app
RUN pip3 install --upgrade pip -r requirements.txt

# copy project
COPY . /app
