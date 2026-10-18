"""Interactive SpaceX launch dashboard.

Run with: python plotly_dash.py
Then open http://127.0.0.1:8050 in a browser.
"""
import pandas as pd
import dash
from dash import dcc, html, Input, Output
import plotly.express as px

DATA_URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv"
df = pd.read_csv(DATA_URL)
required = {"Launch Site", "Payload Mass (kg)", "class", "Booster Version Category"}
missing = required - set(df.columns)
if missing:
    raise ValueError(f"Dataset is missing required columns: {sorted(missing)}")

df["class"] = pd.to_numeric(df["class"], errors="coerce").fillna(0).astype(int)
df["Payload Mass (kg)"] = pd.to_numeric(df["Payload Mass (kg)"], errors="coerce")
max_payload = float(df["Payload Mass (kg)"].max())
min_payload = float(df["Payload Mass (kg)"].min())
sites = sorted(df["Launch Site"].dropna().unique().tolist())
options = [{"label": "All Sites", "value": "ALL"}] + [{"label": s, "value": s} for s in sites]

app = dash.Dash(__name__)
app.title = "SpaceX Launch Records Dashboard"
app.layout = html.Div([
    html.H1("SpaceX Launch Records Dashboard", style={"textAlign": "center"}),
    html.P("Explore landing success by launch site and payload mass.", style={"textAlign": "center"}),
    html.Label("Launch site"),
    dcc.Dropdown(id="site-dropdown", options=options, value="ALL", clearable=False),
    dcc.Graph(id="success-pie-chart"),
    html.Label("Payload range (kg)"),
    dcc.RangeSlider(
        id="payload-slider", min=0, max=max(10000, int(max_payload)), step=500,
        marks={0: "0", int(max_payload/2): str(int(max_payload/2)), int(max_payload): str(int(max_payload))},
        value=[max(0, min_payload), max_payload], tooltip={"placement": "bottom", "always_visible": False}
    ),
    dcc.Graph(id="success-payload-scatter-chart")
], style={"maxWidth": "1200px", "margin": "0 auto", "padding": "24px", "fontFamily": "Arial"})

@app.callback(Output("success-pie-chart", "figure"), Input("site-dropdown", "value"))
def update_pie(selected_site):
    filtered = df if selected_site == "ALL" else df[df["Launch Site"] == selected_site]
    counts = filtered["class"].map({1: "Successful landing", 0: "Unsuccessful / not recorded"}).value_counts().rename_axis("Landing outcome").reset_index(name="Launches")
    title = "Landing outcomes across all sites" if selected_site == "ALL" else f"Landing outcomes — {selected_site}"
    return px.pie(counts, names="Landing outcome", values="Launches", title=title, hole=0.35)

@app.callback(Output("success-payload-scatter-chart", "figure"), Input("site-dropdown", "value"), Input("payload-slider", "value"))
def update_scatter(selected_site, payload_range):
    low, high = payload_range
    filtered = df[df["Payload Mass (kg)"].between(low, high)]
    if selected_site != "ALL":
        filtered = filtered[filtered["Launch Site"] == selected_site]
    title = "Payload mass vs landing outcome"
    if selected_site != "ALL":
        title += f" — {selected_site}"
    fig = px.scatter(filtered, x="Payload Mass (kg)", y="class", color="Booster Version Category",
                     hover_data=["Launch Site"], labels={"class": "Landing class (1=success, 0=not successful)"}, title=title)
    fig.update_yaxes(tickmode="array", tickvals=[0, 1])
    return fig

if __name__ == "__main__":
    app.run(debug=False, port=8050)
