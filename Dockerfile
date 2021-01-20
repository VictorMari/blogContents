FROM python:3.8-rc-slim
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "crawler.py"]