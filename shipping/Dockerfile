FROM python:3.11-slim
WORKDIR /shipping
COPY req.txt .
RUN pip install --upgrade pip
RUN pip install -r req.txt
COPY . .
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]