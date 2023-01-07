import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from data import *
import requests
import json
import geopandas as gpd

def plot_1():
    df = read_clean_data_plot_1()

    color = df.party
    colorscale = [[0.1, 'rgb(235, 28, 36)'],
              [0.2, 'rgb(248, 234, 59)'],
              [0.3, 'rgb(22, 177, 97)'],
              [0.4, 'rgb(3, 56, 106)'],
              [0.5, 'rgb(0, 131, 207)'],
              [0.6, 'rgb(210, 212, 214)'],
              ]


    dim1 = go.parcats.Dimension(
        values=df.freehms,
        label="Gays and lesbians free to live as they wish"
    )

    dim2 = go.parcats.Dimension(
        values=df.mnrgtjb,
        label="Men have more right to job than women when jobs are scarce"
    )

    dim3 = go.parcats.Dimension(
        values=df.ccnthum,
        label="Climate change caused by"
    )

    dim0 = go.parcats.Dimension(
        values=df.party, label="Which party feel closer to", categoryarray=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, ],
        ticktext=['Partito Democratico', 'Movimento 5 Stelle', 'Lega Nord', "Fratelli d'Italia",
              "Forza Italia - PdL", "Other", 'No Answer']
    )


    fig = go.Figure(data = [go.Parcats(dimensions=[dim0, dim1, dim2, dim3],
        line={'color': color,
              'colorscale': colorscale
              },
        hoveron='color', hoverinfo='count+probability',
        #labelfont={'size': 18, 'family': 'Times'},
        #tickfont={'size': 16, 'family': 'Times'},
        arrangement='freeform')])

    return fig

def plot_2():

    df = read_clean_data_plot_2()
    fig = go.Figure()
    fig.add_trace(go.Histogram(x=df[df['party'] == 0.1]['agea'], name="Partito Democratico",
                               marker=dict(color = 'rgb(235, 28, 36)')))
    fig.add_trace(go.Histogram(x=df[df['party'] == 0.2]['agea'], name="Movimento 5 Stelle",
                               marker=dict(color = 'rgb(248, 234, 59)')))
    fig.add_trace(go.Histogram(x=df[df['party'] == 0.3]['agea'], name="Lega Nord",
                               marker=dict(color = 'rgb(22, 177, 97)')))
    fig.add_trace(go.Histogram(x=df[df['party'] == 0.4]['agea'], name="Fratelli d'Italia",
                               marker=dict(color = 'rgb(3, 56, 106)')))
    fig.add_trace(go.Histogram(x=df[df['party'] == 0.5]['agea'], name="Forza Italia - PdL",
                               marker=dict(color = 'rgb(119,173,216)')))

    fig.update_layout(barmode='overlay', template = "plotly_white")

    fig.update_traces(opacity=0.75)

    fig.update_layout(
        title="Age distribution by party",
        xaxis_title="Age",
        yaxis_title="",
        legend_title="Which party feel closer to",

    )
    fig.update_layout(
        font_family="sans-serif",
        title_font_family="sans-serif",
    )

    return fig

def plot_4():
    df = read_clean_data_plot_4()

    party_dict = {0.1: "Partito Democratico",
                  0.2: "Movimento 5 Stelle",
                  0.3: "Lega Nord",
                  0.4: "Fratelli d'Italia",
                  0.5: "Forza Italia - PdL"}

    df["party_name"] = df["party"].map(party_dict)

    df = df[["party_name", "gndr", 'emplrel']]
    df_combinations = (
        df.groupby(["party_name", "gndr", 'emplrel']).size()
            .reset_index()
            .rename(columns={0: "count"})
    )

    fig = px.sunburst(
        df_combinations,
        path=["party_name", "gndr", 'emplrel'],
        title="Gender and employment relation by political party",
        color = 'party_name',
        color_discrete_map={
            "Partito Democratico": 'rgb(235, 28, 36)',
            "Movimento 5 Stelle": 'rgb(248, 234, 59)',
            "Lega Nord": 'rgb(22, 177, 97)',
            "Fratelli d'Italia": 'rgb(3, 56, 106)',
            "Forza Italia - PdL": 'rgb(119,173,216)'},
        values = 'count',

        height=800,
    )
    fig.update_layout(
        font_family="sans-serif",
        title_font_family="sans-serif",
        template = "plotly_white"
    )
    return fig

def plot_5():

    df = read_clean_data_plot_5()

    geojson_url = 'https://raw.githubusercontent.com/AlbGri/AlbGri.github.io/master/assets/files/Openpolis/geojson/limits_IT_regions.geojson'
    italy_regions_geo = requests.get(geojson_url).json()
    regions = ['Piemonte', 'Trentino-Alto Adige/Südtirol', 'Lombardia', 'Puglia', 'Basilicata',
               'Friuli-Venezia Giulia', 'Liguria', "Valle d'Aosta/Vallée d'Aoste", 'Emilia-Romagna',
               'Molise', 'Lazio', 'Veneto', 'Sardegna', 'Sicilia', 'Abruzzo',
               'Calabria', 'Toscana', 'Umbria', 'Campania', 'Marche']

    # Create a dataframe with the region names
    df1 = pd.DataFrame(regions, columns=['reg_name'])

    df = df.merge(df1, on='reg_name', how = 'right')
    #df['name_length'] = df['reg_name'].str.len()
    fig = px.choropleth(data_frame=df,
                        geojson=italy_regions_geo,  # anche il geojson_url gli si può passare
                        locations='reg_name',  # name of dataframe column
                        featureidkey='properties.reg_name',  # feature object locations
                        color='lrscale',
                        color_continuous_scale="RdBu",
                        scope="europe",
                        height=800,
                        title = 'Placement on left right scale by region'
                        )
    fig.update_layout(
        legend_title = 'Left (0)- right (10) scale',
        font_family="sans-serif",
        title_font_family="sans-serif",

    )
    fig.update_geos(showcountries=False, showcoastlines=False, showland=False, fitbounds="locations")
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

    return fig

