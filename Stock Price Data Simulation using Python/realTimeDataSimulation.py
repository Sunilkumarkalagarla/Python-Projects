import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import numpy as np

# Simulate some time-series data: a simple stock price dataset
np.random.seed(42)
dates = pd.date_range(start='2020-01-01', periods=100)
prices = np.random.randn(100).cumsum() + 100  # Simulating stock prices

# Create a DataFrame
df = pd.DataFrame({'Date': dates, 'Price': prices})

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.H1("Time-Series Data Visualization"),
    dcc.Graph(id='time-series-chart'),
    html.Label("Select Date Range:"),
    dcc.RangeSlider(
        id='date-range-slider',
        min=0,
        max=len(df),
        step=1,
        value=[0, len(df)],
        marks={i: str(date.date()) for i, date in enumerate(df['Date'])},
        tooltip={"placement": "bottom", "always_visible": True}
    ),
    html.Label("Adjust Y-Axis Range:"),
    dcc.RangeSlider(
        id='price-range-slider',
        min=df['Price'].min(),
        max=df['Price'].max(),
        step=0.5,
        value=[df['Price'].min(), df['Price'].max()],
        marks={i: f'{i:.0f}' for i in np.linspace(df['Price'].min(), df['Price'].max(), 10)},
        tooltip={"placement": "bottom", "always_visible": True}
    ),
    dcc.Interval(
        id='interval-component',
        interval=1*1000,  # in milliseconds
        n_intervals=0
    )
])

# Callback for updating the graph based on the slider inputs and interval
@app.callback(
    Output('time-series-chart', 'figure'),
    [Input('date-range-slider', 'value'),
     Input('price-range-slider', 'value'),
     Input('interval-component', 'n_intervals')]
)
def update_chart(date_range, price_range, n):
    global df
    if n > 0:  # Avoid updating on the initial load
        new_date = df['Date'].iloc[-1] + pd.Timedelta(days=1)
        new_price = df['Price'].iloc[-1] + np.random.randn()  # Simulate price change
        new_row = pd.DataFrame({'Date': [new_date], 'Price': [new_price]})
        df = pd.concat([df, new_row]).reset_index(drop=True)

    # Ensure the slider range does not exceed the data frame length
    max_index = len(df) - 1
    start_index = max(0, min(date_range[0], max_index))
    end_index = max(start_index, min(date_range[1], max_index))

    filtered_df = df.iloc[start_index:end_index]
    fig = px.line(filtered_df, x='Date', y='Price', title='Stock Price Over Time')
    fig.update_yaxes(range=price_range)
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
