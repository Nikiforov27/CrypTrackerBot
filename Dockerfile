FROM python:3.10 AS builder
COPY . /bot
WORKDIR /bot
RUN pip3 install -r requirements.txt
CMD ["python3", "main.py"]
