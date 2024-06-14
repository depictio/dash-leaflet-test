import dash
from dash import html
import dash_leaflet as dl

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the map
map_center = [48.5734, 7.7521]  # Latitude and Longitude for Strasbourg
zoom_level = 12  # Adjusted to show a close-up of the city

app.layout = html.Div([
    dl.Map(center=map_center, zoom=zoom_level, style={'width': '100%', 'height': '90vh'}, children=[
        dl.TileLayer()  # This will use the default OpenStreetMap tiles
    ])
], style={'height': '100vh'})  # Adjust height to fit the viewport

if __name__ == '__main__':
    app.run_server(debug=True)
