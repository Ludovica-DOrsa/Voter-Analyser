import dash
from dash import dcc, State, html, dash_table
from dash.dependencies import Input, Output
from graphs import *
import dash_bootstrap_components as dbc
from dash import html
import base64


#-----------------------------------------------------------------------------------------------------------------------
# GRAPHS
#-----------------------------------------------------------------------------------------------------------------------

fig1 = plot_1()
fig2 = plot_2()
fig4 = plot_4()
fig5 = plot_5()

#-----------------------------------------------------------------------------------------------------------------------
#IMGS
#-----------------------------------------------------------------------------------------------------------------------
PD = "imgs/PD.png"
PD_base64 = base64.b64encode(open(PD, 'rb').read()).decode('ascii')

M5S = "imgs/M5S.png"
M5S_base64 = base64.b64encode(open(M5S, 'rb').read()).decode('ascii')

FI = "imgs/FI.jpg"
FI_base64 = base64.b64encode(open(FI, 'rb').read()).decode('ascii')

LN = "imgs/Lega_Nord.png"
LN_base64 = base64.b64encode(open(LN, 'rb').read()).decode('ascii')

FDI = "imgs/FDI.png"
FDI_base64 = base64.b64encode(open(FDI, 'rb').read()).decode('ascii')

#-----------------------------------------------------------------------------------------------------------------------
#CARDS
#-----------------------------------------------------------------------------------------------------------------------
pd = dbc.Card(
    [dbc.CardImg(src='data:image/png;base64,{}'.format(PD_base64), top=True),
        dbc.CardBody([
                html.H4("Partito Democratico", className="card-title"),
                dbc.Button("Read more",
                outline=True, color="light",
                           href='https://en.wikipedia.org/wiki/Democratic_Party_(Italy)'),],
        style={'background-color':'rgb(235, 28, 36)'}),]
,style={"width": "13rem",  'color': 'white', 'font-family': 'sans-serif',
},)

m5s = dbc.Card(
    [dbc.CardImg(src='data:image/png;base64,{}'.format(M5S_base64), top=True),
        dbc.CardBody([

                html.H4("Movimento 5 Stelle", className="card-title"),
                dbc.Button("Read more",
                            outline=True, color="light",
                           href='https://en.wikipedia.org/wiki/Five_Star_Movement'),],
        style={'background-color':'rgb(248, 234, 59)'}),],
    style={"width": "13rem", 'color': 'white', 'font-family': 'sans-serif',},)

fi = dbc.Card(
    [dbc.CardImg(src='data:image/png;base64,{}'.format(FI_base64), top=True),
        dbc.CardBody([
                html.H4("Forza Italia                 "
                        , className="card-title"),
            html.P(""),
                dbc.Button("Read more", outline=True, color="light",
                           href='https://en.wikipedia.org/wiki/Forza_Italia'),],
            style={'background-color': 'rgb(119,173,216)'}
        ),],style={"width": "13rem", 'color': 'white', 'font-family': 'sans-serif',},)

ln = dbc.Card(
    [dbc.CardImg(src='data:image/png;base64,{}'.format(LN_base64), top=True),
        dbc.CardBody([
                html.H4("Lega Nord                           ", className="card-title"),
                dbc.Button("Read more", outline=True, color="light",
                           href='https://en.wikipedia.org/wiki/Lega_Nord'),],
            style={'background-color': 'rgb(22,177,97)'}
        ),],style={"width": "13rem", 'color': 'white', 'font-family': 'sans-serif',},)

fdi = dbc.Card(
    [dbc.CardImg(src='data:image/png;base64,{}'.format(FDI_base64), top=True),
        dbc.CardBody([
                html.H4("Fratelli d'Italia                       ", className="card-title"),
                dbc.Button("Read more", outline=True, color="light",
                           href='https://en.wikipedia.org/wiki/Brothers_of_Italy'),],
        style={'background-color': 'rgb(3, 56, 106)'}),],
    style={"width": "13rem", 'color': 'white', 'font-family': 'sans-serif',},)

#-----------------------------------------------------------------------------------------------------------------------
# LAYOUT
#-----------------------------------------------------------------------------------------------------------------------

app = dash.Dash(external_stylesheets=[
    dbc.themes.BOOTSTRAP,
    dbc.icons.BOOTSTRAP,
    "fonts.googleapis.com/css2?family=Open+Sans:wght@300&family=Roboto&display=swap"
])

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f5f4ef",
    'font-family': 'sans-serif'
}

CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
    'font-family': 'sans-serif',
    "background-color": "white",

}

sidebar = html.Div(
    [
        html.H3("Voter attitudes analyser", className="display-4"),
        html.Hr(),
        html.P(
            "Opinions and demographics in 2018 Italy", className="lead"
        ),
        dbc.Button("Get source microdata", outline=True, color="dark",
                           href='https://ess-search.nsd.no/')
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE, children=
                   [
dbc.Row(
    [
        dbc.Col(pd, width="auto"),
        dbc.Col(m5s, width="auto"),
        dbc.Col(fi, width="auto"),
        dbc.Col(ln, width="auto"),
        dbc.Col(fdi, width="auto"),
    ]
),
html.Hr(),
html.Div(
    #dcc.Graph(figure=fig1),
    [dcc.Graph(figure=fig2)]),
html.Hr(),
html.Div(
    [
    dbc.Row([
    dbc.Col(
        html.P("View average trust in:"),
        width="25%"),
    dbc.Col(
    dcc.Dropdown(options={
        'trstlgl': 'Legal system',
        'trstplc': 'Police',
        'trstplt': 'Politicians',
        'trstep': 'European Parliament',
        'trstun': 'United Nations',
        'trstprl': 'National Parliament',
    }, value = 'trstprl', id = 'dropdown'))]
    ),
    dcc.Graph(id='fig3'),
    dcc.RangeSlider(15, 95, 1, value=[18, 30], id='range-slider',
                marks=None,
                tooltip={"placement": "bottom", "always_visible": True}
                ),]),
html.Hr(),
html.Div([
    dcc.Graph(figure=fig4)]),
html.Hr(),
html.Div([
    dcc.Graph(figure=fig5)]),
                   ])


app.layout = html.Div([sidebar, content])

#-----------------------------------------------------------------------------------------------------------------------
# CALLBACKS
#-----------------------------------------------------------------------------------------------------------------------

@app.callback(
    Output('fig3', 'figure'),
    Input('dropdown', 'value'),
    Input('range-slider', 'value'),
)
def update_graph(d_value, s_value):

    df = read_clean_data_plot_3(d_value)
    df = df[(df['agea']>=s_value[0])&(df['agea']<=s_value[1])]
    df = df.groupby(['party_name'])[d_value].mean().reset_index()
    fig = px.bar(df, x="party_name", y=d_value, color="party_name", range_y=[0, 10],
                 labels={"party_name": "Which party feel closer to"},

                 color_discrete_map={
                        "Partito Democratico":'rgb(235, 28, 36)',
                        "Movimento 5 Stelle":'rgb(248, 234, 59)',
                        "Lega Nord":'rgb(22, 177, 97)',
                        "Fratelli d'Italia":'rgb(3, 56, 106)',
                        "Forza Italia - PdL":'rgb(119,173,216)'}
                 )
    fig.update_xaxes(title="")
    fig.update_yaxes(title="Trust (10 = complete trust)")
    fig.update_layout(
        font_family="sans-serif",
        title_font_family="sans-serif",
        template="plotly_white"
    )
    return fig


if __name__ == "__main__":
    app.run_server(port=8888)