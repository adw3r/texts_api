FROM python:3.10

WORKDIR /myapp

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["sh", "-c", "uvicorn main:app --host=$HOST --port=$PORT"]