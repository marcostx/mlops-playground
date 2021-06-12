FROM python:3.6.4

RUN apt-get update -y \
    && apt-get install -y python3-dev python3-pip build-essential \
    && apt-get install gcc -y \
    && apt-get clean

# Install requirements
COPY requirements.txt /requirements.txt

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

RUN mkdir -p /app
RUN mkdir -p /app/ml_app

WORKDIR /app/ml_app

COPY ml_app/src /app/ml_app/src
COPY ml_app/data /app/ml_app/data
COPY ml_app/models /app/ml_app/models
ENV PYTHONPATH /app/ml_app/

CMD ["bash"]