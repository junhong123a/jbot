FROM python:3.8-slim

WORKDIR /app
COPY . .
RUN pip install --trusted-host pypi.python.org -r requirements.txt 

CMD python V4_1.py
EXPOSE 80
