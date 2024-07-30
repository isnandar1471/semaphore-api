FROM python:3.10.8
WORKDIR /app
#RUN apt install python3-pymysql -y
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8888
ENTRYPOINT python main.py
