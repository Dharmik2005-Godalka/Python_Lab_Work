import pandas as pd
import plotly.express as px

data = {
    'Product': ['A', 'B', 'C', 'D', 'E'],
    'Sales': [100, 200, 150, 300, 250],
    'Profit': [30, 70, 50, 120, 90]
}

df = pd.DataFrame(data)

fig = px.scatter(df, x='Sales', y='Profit', color='Product', title='Sales vs Profit')
fig.show(renderer="browser")
