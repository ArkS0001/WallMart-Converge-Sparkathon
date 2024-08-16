import pandas as pd
import numpy as np

# Generate date range
date_range = pd.date_range(start='2022-01-01', end='2024-12-31', freq='D')

# Generate synthetic data
np.random.seed(42)  # For reproducibility
trend = np.linspace(10, 100, len(date_range))  # Linear trend
seasonality = 10 * np.sin(2 * np.pi * date_range.dayofyear / 365.25)  # Seasonal component
noise = np.random.normal(0, 5, len(date_range))  # Random noise
values = trend + seasonality + noise

# Create DataFrame
data = pd.DataFrame({
    'Date': date_range,
    'Value': values
})

# Save to CSV
data.to_csv('synthetic_time_series.csv', index=False)

print("Synthetic dataset created and saved as 'synthetic_time_series.csv'.")
