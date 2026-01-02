FROM python:3.11

WORKDIR /app
COPY . .

RUN pip install pandas scikit-learn dash plotly sqlite3

CMD ["python", "app.py"]
