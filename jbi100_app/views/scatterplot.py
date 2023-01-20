import plotly.graph_objects as go
import pandas as pd
from dash import dcc, html

class Scatterplot(html.Div):
    def __init__(self, name, feature_x, feature_y, df):
        self.html_id = name.lower().replace(" ", "-")
        self.df = df
        self.feature_x = feature_x
        self.feature_y = feature_y
        self.neighbourhood = 'Bronx'  # set a default neighbourhood
        self.listing_type = 'Entire home/apt'  # set a default listing type
        self.color = 'blue'

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
        if color is None:
            color = self.color
        title = "Listing Price by " + listing_type + " in " + self.feature_x

        self.fig = go.Figure()

        df_listing = self.df[(self.df['room_type'] == listing_type) & (self.df[self.feature_x].notna())]

        self.fig.add_trace(go.Scatter(x=df_listing[self.feature_x], y=df_listing[self.feature_y], mode='markers', 
        marker=dict(color=self.color), name='Price'))

        self.fig.update_layout(
            height = 600,
            xaxis_title=self.feature_x.lower().replace("_", " "),
            yaxis_title="Price",
            title = title
        )
    
        return self.fig
        
    