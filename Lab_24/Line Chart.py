import pandas as pd
import plotly.express as px

data = {
    'Product': ['A', 'B', 'C', 'D', 'E'],
    'Sales': [100, 200, 150, 300, 250],
    'Profit': [30, 70, 50, 120, 90]
}

df = pd.DataFrame(data)

fig = px.line(df, x='Product', y='Profit', title='Profit by Product')
fig.show(renderer="browser") 
