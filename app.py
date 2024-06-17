import dash
from dash import html, dcc
import dash_leaflet as dl
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# List of beacons with external website links
beacons = [
    {"name": "Beacon 1", "lat": 48.5765, "lon": 7.7480, "url": "https://www.google.com"},
    {"name": "Beacon 2", "lat": 48.5805, "lon": 7.7500, "url": "https://www.amazon.com"}
]

def generate_marker(beacon):
    return dl.Marker(position=[beacon['lat'], beacon['lon']], children=[
        dl.Tooltip(beacon['name']),
        dl.Popup([
            html.A("Visit Site", href=beacon['url'], target="_blank")
        ])
    ])

app.layout = html.Div([
    dl.Map(center=[48.5734, 7.7521], zoom=12, style={'width': '100%', 'height': '90vh'}, children=[
        dl.TileLayer(),
        dl.LayerGroup([generate_marker(beacon) for beacon in beacons])
    ]),
    html.Div(id="media-content", style={"margin": "20px"})
])

if __name__ == '__main__':
    app.run_server(debug=True)
