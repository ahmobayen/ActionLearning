
import finnhub
import pandas as pd

finnhub_client = finnhub.Client(api_key="cj0hub9r01qgc2gj2pu0cj0hub9r01qgc2gj2pug")

# Get the basic financials data for AAPL
data = finnhub_client.company_basic_financials('AAPL', 'all')

# Create a DataFrame using pandas
df = pd.DataFrame(data)

# Print the DataFrame
print(df)