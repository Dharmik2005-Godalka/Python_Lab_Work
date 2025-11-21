import pandas as pd
import plotly.express as px

data = {
    'Product': ['A', 'B', 'C', 'D', 'E'],
    'Sales': [100, 200, 150, 300, 250],
    'Profit': [30, 70, 50, 120, 90]
}

df = pd.DataFrame(data)

fig = px.bar(df, x='Product', y='Sales', title='Sales by Product')
fig.show(renderer="browser")
