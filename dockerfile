FROM python:latest

WORKDIR .

copy requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python" , "hello.py"] 
