from fastapi import FastAPI
from pyspark.sql import SparkSession
import pandas as pd
import sqlite3
from sklearn.linear_model import LinearRegression
from datetime import datetime, timedelta

app = FastAPI(title="Sales Forecast API")

# -------------------------------
# Initialize Spark Session
# -------------------------------
spark = SparkSession.builder \
    .appName("SalesAnalysis") \
    .master("local[*]") \
    .getOrCreate()

# -------------------------------
# Load Data from SQLite using Spark
# -------------------------------
def load_sales_data():
    conn = sqlite3.connect('data/sales.db')
    pdf = pd.read_sql_query("SELECT * FROM sales", conn)
    conn.close()
    return spark.createDataFrame(pdf)

# -------------------------------
# Endpoint: Get Raw Sales Data
# -------------------------------
@app.get("/sales")
def get_sales():
    df = load_sales_data()
    return df.toPandas().to_dict(orient='records')

# -------------------------------
# Endpoint: Predict Future Sales
# -------------------------------
@app.get("/predict")
def predict_sales(region: str = "North"):
    df = load_sales_data().toPandas()
    subset = df[df['region']==region]
    subset['date_ordinal'] = pd.to_datetime(subset['date']).map(pd.Timestamp.toordinal)
    
    X = subset[['date_ordinal']]
    y = subset['units_sold']
    model = LinearRegression()
    model.fit(X, y)

    future_dates = pd.date_range(start=subset['date'].max() + timedelta(days=1), periods=7)
    future_X = future_dates.map(pd.Timestamp.toordinal).values.reshape(-1,1)
    predictions = model.predict(future_X)

    # Simulate GenAI
    genai_predictions = [int(p+2) for p in predictions]

    forecast_genai = pd.DataFrame({
        'date': future_dates,
        'predicted_units_sold': genai_predictions
    })
    return forecast_genai.to_dict(orient='records')

# -------------------------------
# Run with Uvicorn (development)
# -------------------------------
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)
