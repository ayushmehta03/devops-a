FROM ubuntu:latest

WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install -y python3 python3-pip

ENV NAME World

# Run a command to start the application
CMD ["python3", "app.py"]