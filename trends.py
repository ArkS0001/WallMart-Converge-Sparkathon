
Hugging Face's logo Hugging Face

Models
Datasets
Spaces
Posts
Docs
Pricing

    Log In
    Sign Up

Spaces:
alexander-lazarin
/
fashion-trends
App
Files
Community
fashion-trends
/ app.py
alexander-lazarin's picture
alexander-lazarin
Change layout to vertical
8c05129
2 months ago
raw
history
blame
contribute
delete
No virus
3.49 kB
import gradio as gr
import pandas as pd
import pmdarima as pm
from pmdarima import auto_arima
import plotly.graph_objs as go

def forecast_time_series(file):
    # Load data
    data = pd.read_csv(file.name, skiprows=2)
    period_type = data.columns[0]
    data[period_type] = pd.to_datetime(data[period_type])
    data.set_index(period_type, inplace=True)

    # Fit the SARIMAX model automatically
    model = auto_arima(data)
    
    # Forecasting
    n_periods = 24  # Number of periods to forecast
    forecast, conf_int = model.predict(n_periods=n_periods, return_conf_int=True)
    
    # Create a DataFrame with the forecast and confidence intervals
    forecast_index = pd.date_range(start=data.index[-1], periods=n_periods + 1, freq=data.index.inferred_freq)[1:]
    forecast_df = pd.DataFrame(forecast, index=forecast_index, columns=['Forecast'])
    conf_int_df = pd.DataFrame(conf_int, index=forecast_index, columns=['Lower CI', 'Upper CI'])
    forecast_df = pd.concat([forecast_df, conf_int_df], axis=1)

    # Calculate the YoY change
    sum_last_12_original = data.iloc[-12:, 0].sum()
    sum_first_12_forecast = forecast_df['Forecast'].iloc[:12].sum()
    yoy_change = (sum_first_12_forecast - sum_last_12_original) / sum_last_12_original

    # Create an interactive plot with Plotly
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data.index, y=data.iloc[:, 0], mode='lines', name='Original Series'))
    fig.add_trace(go.Scatter(x=forecast_df.index, y=forecast_df['Forecast'], mode='lines', name='Forecast', line=dict(color='red')))
    fig.add_trace(go.Scatter(
        x=forecast_df.index,
        y=forecast_df['Lower CI'],
        fill=None,
        mode='lines',
        line=dict(color='pink'),
        showlegend=False
    ))
    fig.add_trace(go.Scatter(
        x=forecast_df.index,
        y=forecast_df['Upper CI'],
        fill='tonexty',
        mode='lines',
        line=dict(color='pink'),
        name='Confidence Interval'
    ))
    fig.update_layout(
        title='Original Time Series and Forecast with Confidence Intervals',
        xaxis_title='Date',
        yaxis_title='Values',
        legend=dict(
            orientation='h',
            yanchor='bottom',
            y=1.02,
            xanchor='right',
            x=1
        ),
        hovermode='x unified'
    )
    
    # Combine original data and forecast data into one DataFrame for export
    combined_df = pd.concat([data, forecast_df], axis=0)
    combined_file = 'combined_data.csv'
    combined_df.to_csv(combined_file)

    # Return plot file path and YoY change
    return fig, f'Year-over-Year Change in Sum of Values: {yoy_change:.2%}', combined_file

# Create Gradio interface using Blocks
with gr.Blocks(theme=gr.themes.Monochrome()) as interface:
    gr.Markdown("# Time Series Forecasting")
    gr.Markdown("Upload a CSV file with a time series to forecast the next 24 periods and see the YoY % change. Download the combined original and forecast data.")
    
    with gr.Row():
        file_input = gr.File(label="Upload Time Series CSV")
    
    with gr.Row():
        plot_output = gr.Plot(label="Time Series + Forecast Chart")
    
    with gr.Row():
        yoy_output = gr.Text(label="YoY % Change")
    
    with gr.Row():
        csv_output = gr.File(label="Download Combined Data CSV")
    
    file_input.change(forecast_time_series, inputs=file_input, outputs=[plot_output, yoy_output, csv_output])

# Launch the interface
interface.launch()

