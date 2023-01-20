import plotly.graph_objects as go
import pandas as pd
from dash import dcc, html

class Histogram(html.Div):
    def __init__(self, name, feature_x, feature_y, type, df):
        
        self.html_id = name.lower().replace(" ", "-")
        self.df = df
        self.feature_x = feature_x
        self.feature_y = feature_y
        self.type = type
        
        super().__init__(
            className="graph_card",
            children=[
                html.H6(name),
                dcc.Graph(id=self.html_id, figure=self.update())
            ],
        )
    
    def update(self):
        self.fig = go.Figure()
        
        x_values = self.df[self.feature_x]
        y_values = self.df[self.feature_y]    
        
        y_values_int = y_values    
        
        self.fig.add_trace(go.Histogram2d (x = x_values, y = y_values, texttemplate= "%{z}", textfont_size=15))
        self.fig.update_layout(
            xaxis_title=self.feature_x.lower().replace("_", " "),
            yaxis_title=self.feature_y.lower().replace("_", " ")
        )
        return self.fig
        