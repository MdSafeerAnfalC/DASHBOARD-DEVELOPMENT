import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd

# Load dataset
df = pd.read_csv("E:/ALL Folder/Downloads/archive/Covid - 19.csv")

# Initialize app
app = dash.Dash(__name__)

# Layout
app.layout = html.Div([
    html.H1("COVID-19 Dashboard", style={'textAlign': 'center'}),

    # Filters
    html.Div([
        html.Label("Select Country:"),
        dcc.Dropdown(
            id='country_filter',
            options=[{'label': c, 'value': c} for c in df['Country'].unique()],
            value=df['Country'].unique()[0],
            multi=False
        ),
        html.Label("Select WHO Region:"),
        dcc.Dropdown(
            id='region_filter',
            options=[{'label': r, 'value': r} for r in df['WHO Region'].unique()],
            value=df['WHO Region'].unique()[0],
            multi=False
        )
    ], style={'width': '25%', 'float': 'left'}),

    # KPIs
    html.Div([
        html.Div(id="kpi_cases", style={'padding': '20px', 'fontSize': '18px'}),
        html.Div(id="kpi_deaths", style={'padding': '20px', 'fontSize': '18px'}),
        html.Div(id="kpi_recovery", style={'padding': '20px', 'fontSize': '18px'}),
        html.Div(id="kpi_active", style={'padding': '20px', 'fontSize': '18px'})
    ], style={'width': '70%', 'float': 'right'}),

    # Graphs
    html.Div([
        dcc.Graph(id='top_countries'),
        dcc.Graph(id='distribution'),
        dcc.Graph(id='death_recovery_rate')
    ], style={'width': '100%', 'float': 'right'})
])

# Callbacks
@app.callback(
    [Output('top_countries', 'figure'),
     Output('distribution', 'figure'),
     Output('death_recovery_rate', 'figure'),
     Output('kpi_cases', 'children'),
     Output('kpi_deaths', 'children'),
     Output('kpi_recovery', 'children'),
     Output('kpi_active', 'children')],
    [Input('country_filter', 'value'),
     Input('region_filter', 'value')]
)
def update_dashboard(country, region):
    # Filter by region (all countries in that WHO region)
    dfr = df[df['WHO Region'] == region]

    # KPIs for selected country
    dff = df[df['Country'] == country].iloc[0]
    total_cases = dff['Confirmed']
    total_deaths = dff['Deaths']
    total_recovered = dff['Recovered']
    active_cases = dff['Active']
    recovery_rate = round((total_recovered / total_cases) * 100, 2) if total_cases > 0 else 0

    # Top 10 countries by confirmed cases in the selected region
    top_countries = dfr.nlargest(10, 'Confirmed')
    fig1 = px.bar(top_countries, x='Country', y='Confirmed',
                  title=f"Top 10 Countries by Confirmed Cases in {region}")

    # Distribution of cases in selected country
    dist_df = pd.DataFrame({
        'Category': ['Confirmed', 'Deaths', 'Recovered', 'Active'],
        'Count': [total_cases, total_deaths, total_recovered, active_cases]
    })
    fig2 = px.pie(dist_df, names='Category', values='Count',
                  title=f"Case Distribution in {country}")

    # Death & Recovery rates (per 100 cases)
    fig3 = px.bar(dfr, x='Country',
                  y=['Deaths / 100 Cases', 'Recovered / 100 Cases'],
                  title=f"Death vs Recovery Rate per 100 Cases in {region}")

    return (
        fig1, fig2, fig3,
        f"🦠 Total Cases: {total_cases:,}",
        f"☠️ Total Deaths: {total_deaths:,}",
        f"💚 Recovery Rate: {recovery_rate}%",
        f"📌 Active Cases: {active_cases:,}"
    )

# Run app

if __name__ == '__main__':
    app.run(debug=True)
