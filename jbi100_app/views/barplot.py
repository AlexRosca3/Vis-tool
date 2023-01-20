import plotly.graph_objects as go
import pandas as pd
from dash import dcc, html

class Barplot(html.Div):
    def __init__(self, name, feature_x, feature_y, df):
        self.html_id = name.lower().replace(" ", "-")
        self.df = df
        self.feature_x = feature_x
        self.feature_y = feature_y
        self.listing_type = 'Entire home/apt'  # set a default listing type
        self.color = 'green'

        super().__init__(
            className="graph_card",
            children=[
                html.H6(name),
                dcc.Graph(id=self.html_id, figure=self.update())
            ],
        )
    
    def update(self, listing_type=None, color=None):
        if listing_type is None:
            listing_type = self.listing_type
        if color is not None:
            self.color = color
        title = listing_type + " Average Price by Neighbourhood Group"

        self.fig = go.Figure()

        df_avg = self.df[self.df['room_type'] == listing_type].groupby(self.feature_x).mean(numeric_only=True)

        if self.feature_y == 'price':
            self.fig.add_trace(go.Bar(x=df_avg.index, y=df_avg[self.feature_y], name='Average Price', marker=dict(color=self.color), 
            text=["{} €{:,.2f}".format(x, y) for x, y in zip(df_avg.index, df_avg[self.feature_y])], 
            hoverinfo='text', textfont=dict(size=15), hoverlabel=dict(font=dict(size=20))))
            
            self.fig.update_layout(
            height = 600,
            xaxis_title=self.feature_x.lower().replace("_", " "),
            yaxis_title=listing_type.lower().replace("_", " ") + " " + "average price",
            title = title
            )
        else:
            self.fig.add_trace(go.Bar(x=df_avg.index, y=df_avg[self.feature_y], name='Average Price', marker=dict(color=self.color), 
            text=["{} {:,.2f}".format(x, y) for x, y in zip(df_avg.index, df_avg[self.feature_y])], 
            hoverinfo='text', textfont=dict(size=15), hoverlabel=dict(font=dict(size=20))))
            
            self.fig.update_layout(
            yaxis=dict(range=[0, 5]),
            height = 600,
            xaxis_title=self.feature_x.lower().replace("_", " "),
            yaxis_title=listing_type.lower().replace("_", " ") + " " + "average price",
            title = title
            )

        return self.fig

