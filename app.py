import sqlite3
import pandas as pd
from sklearn.linear_model import LinearRegression
from dash import Dash, dcc, html
import plotly.express as px
from datetime import datetime, timedelta
# Optional: OpenAI for GenAI prediction
# from openai import OpenAI

# -------------------------------
# Step 1: Load Sales Data
# -------------------------------
conn = sqlite3.connect('data/sales.db')
df = pd.read_sql_query("SELECT * FROM sales", conn)
conn.close()

# Step 2: Subset data (e.g., North region)
subset = df[df['region']=='North']

# Step 3: Handle missing data
subset['units_sold'] = subset['units_sold'].fillna(subset['units_sold'].mean())
subset['revenue'] = subset['revenue'].fillna(subset['revenue'].mean())

# -------------------------------
# Step 4: Future Prediction (Simple Regression)
# -------------------------------
subset['date_ordinal'] = pd.to_datetime(subset['date']).map(pd.Timestamp.toordinal)
X = subset[['date_ordinal']]
y = subset['units_sold']

model = LinearRegression()
model.fit(X, y)

future_dates = pd.date_range(start=subset['date'].max() + timedelta(days=1), periods=7)
future_X = future_dates.map(pd.Timestamp.toordinal).values.reshape(-1,1)
predictions = model.predict(future_X)

forecast = pd.DataFrame({'date': future_dates, 'predicted_units_sold': predictions})

# -------------------------------
# Step 4.5: GenAI Prediction (Simulated)
# -------------------------------
# If using OpenAI:
# client = OpenAI(api_key="YOUR_API_KEY")
# prompt = f"Predict next 7 days units sold: {subset[['date','units_sold']].to_dict(orient='records')}"
# response = client.chat.completions.create(model="gpt-4o-mini", messages=[{"role":"user","content":prompt}])
# genai_predictions = [int(x) for x in response.choices[0].message.content.split(',')]

# For demo, simulate GenAI predictions
genai_predictions = [int(p+2) for p in predictions]  # small modification for AI effect
forecast_genai = pd.DataFrame({'date': future_dates, 'predicted_units_sold': genai_predictions})

# -------------------------------
# Step 5: Dashboard with Dash
# -------------------------------
app = Dash(__name__)

fig_actual = px.line(subset, x='date', y='units_sold', title='Actual Sales')
fig_forecast = px.line(forecast, x='date', y='predicted_units_sold', title='Regression Forecast')
fig_genai = px.line(forecast_genai, x='date', y='predicted_units_sold', title='GenAI Forecast')

app.layout = html.Div([
    html.H1("Sales Dashboard with GenAI Forecast"),
    dcc.Graph(figure=fig_actual),
    dcc.Graph(figure=fig_forecast),
    dcc.Graph(figure=fig_genai)
])

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=5000)
