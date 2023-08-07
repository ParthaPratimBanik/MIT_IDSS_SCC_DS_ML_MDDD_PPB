import dash
from dash import html, dcc, Patch
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

import plotly.graph_objects as go

import ctypes
from enum import Enum
import pandas as pd

class DATASET(Enum):
    PIMA_DIABETES="case_studies/pima_diabetes_analysis/diabetes.csv"
    HOTEL_BOOKING_CANCELATION="/case_studies/cht_hbcp/INNHotelsGroup.csv"
    MOVIE_RECOMMENDATION_SYSTEM="/case_studies/movie_recomm_sys/ratings.csv"


class DASH_APP:
    app=None
    height=None
    width=None
    layouts=None
    df=None
    def __init__(self):
        self.app = dash.Dash(external_stylesheets=[dbc.themes.CYBORG])
        figure_width_percent = 0.80
        figure_height_percent = 1.00
        user32 = ctypes.windll.user32
        screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        self.height = round(figure_height_percent*screensize[1])
        self.width = round(figure_width_percent*screensize[0])
        # print(screensize)
        
        self.df=pd.read_csv(DATASET.PIMA_DIABETES.value)
        print(self.df)
        self.layouts = self.pimadds_tabs()
        

    def pimadds_tabs(self):
        fig = go.Figure()
        fig.add_trace(go.Bar(x=[],y=[]))
        fig.update_xaxes(title_text="")
        fig.update_yaxes(title_text="")
        fig.update_layout(height=self.height//2, width=self.width, title_text="")

        fig1 = go.Figure()
        fig1.add_trace(go.Scatter(x=[],y=[],
                                  mode="markers",
                                  showlegend=False,
                                  visible=True,))
        fig1.update_xaxes(title_text="")
        fig1.update_yaxes(title_text="")
        fig1.update_layout(height=self.height//2, width=self.width, title_text="")

        fig2 = go.Figure()
        fig2.add_trace(go.Pie(labels=[],values=[]))

        width_order1 = {"size":"True", "order": 1}

        def tab1LO():
            app_rows = []
            html_div_text_style = {"display": True, "margin-top": "10px"}

            app_header = html.H3("Variable Distribution")
            app_rows.append(dbc.Row(dbc.Col(app_header, width={'size': "auto"},),))

            app_graph = dcc.Graph(id='bar_plot', figure=fig)
            app_rows.append(dbc.Col(app_graph, width={'size': 10, 'order': 1},))

            app_vars_dd = dcc.Dropdown(id = 'variables',
                                    multi = False,
                                    clearable = True,
                                    disabled = False,
                                    searchable = True,
                                    style = {"display": True},
                                    value = self.df.columns[0],
                                    placeholder = "Files",
                                    persistence = True,
                                    persistence_type = "memory",
                                    options = [{"label":col, "value":col}
                                            for col in self.df.columns], className = "dcc_compon")
            app_rows.append(dbc.Row(dbc.Col(app_vars_dd, width=width_order1),))

            layout = html.Div([
                app_rows[0],
                            dbc.Row([
                                app_rows[1],
                                        dbc.Col([html.Div([
                                                app_rows[2],
                                                ],),], width={'size': 2, 'order': 2}, ),
                                                ],),
                                                ])
            return layout
        
        def tab2LO():
            app_rows = []
            html_div_text_style = {"display": True, "margin-top": "10px"}

            app_header = html.H3("Scatter Plot")
            app_rows.append(dbc.Row(dbc.Col(app_header, width={'size': "auto"},),))

            app_row2_cols=[]
            app_vars1_dd = dcc.Dropdown(id = 'variables1',
                                    multi = False,
                                    clearable = True,
                                    disabled = False,
                                    searchable = True,
                                    style = {"display": True},
                                    value = self.df.columns[0],
                                    placeholder = "Files",
                                    persistence = True,
                                    persistence_type = "memory",
                                    options = [{"label":col, "value":col}
                                            for col in self.df.columns], className = "dcc_compon")
            app_row2_cols.append(dbc.Col(app_vars1_dd, width={'size': 2, 'order': 1}),)
            
            app_graph = dcc.Graph(id='scatter_plot', figure=fig1)
            app_row2_cols.append(dbc.Col(app_graph, width={'size': 8, 'order': 2},))
            
            app_row3_cols=[]
            app_row3_cols.append(dbc.Col(html.Div(), width={'size': 2, 'order': 1},),)
            app_vars2_dd = dcc.Dropdown(id = 'variables2',
                        multi = False,
                        clearable = True,
                        disabled = False,
                        searchable = True,
                        style = {"display": True},
                        value = self.df.columns[0],
                        placeholder = "Files",
                        persistence = True,
                        persistence_type = "memory",
                        options = [{"label":col, "value":col}
                                for col in self.df.columns], className = "dcc_compon")
            app_row3_cols.append(dbc.Col(app_vars2_dd, width={'size': 2, 'order': 2}),)

            

            layout = html.Div([app_rows[0],
                               dbc.Row([
                                   app_row2_cols[0],
                                   app_row2_cols[1],
                               ],),
                               dbc.Row([
                                   app_row3_cols[0],
                                   app_row3_cols[1],
                               ],),])
            return layout
        
        def tab3LO():
            app_rows = []
            html_div_text_style = {"display": True, "margin-top": "10px"}

            app_header = html.H3("Pie Chart")
            app_rows.append(dbc.Row(dbc.Col(app_header, width={'size': "auto"},),))

            app_row2_cols=[]
            app_graph = dcc.Graph(id='pie_plot', figure=fig2)
            app_row2_cols.append(dbc.Col(app_graph, width={'size': 10, 'order': 1},))

            app_vars_dd = dcc.Dropdown(id = 'variables_pc',
                                    multi = False,
                                    clearable = True,
                                    disabled = False,
                                    searchable = True,
                                    style = {"display": True},
                                    value = self.df.columns[0],
                                    placeholder = "Files",
                                    persistence = True,
                                    persistence_type = "memory",
                                    options = [{"label":col, "value":col}
                                            for col in self.df.columns], className = "dcc_compon")
            app_row2_cols.append(dbc.Col(app_vars_dd, width={'size': 2, 'order': 2}),)

            layout = html.Div([app_rows[0],
                               dbc.Row([
                                   app_row2_cols[0],
                                   app_row2_cols[1],
                               ],),])
            return layout
        
        def tab4LO():
            app_rows = []
            html_div_text_style = {"display": True, "margin-top": "10px"}

            app_header = html.H3("Violin & Box Plot")
            app_rows.append(dbc.Row(dbc.Col(app_header, width={'size': "auto"},),))

            layout = html.Div([app_rows[0]])
            return layout
        
        layouts = [tab1LO(),
                   tab2LO(),
                   tab3LO(),
                   tab4LO()]
        return layouts
    

    def hotelBookingCancel_tabs(self):
        layouts = []
        return layouts
    

    def movieRecomSys_tabs(self):
        layouts = []
        return layouts
    
    
    def run(self):
        app_dd = dcc.Dropdown(id = 'main_dataset_dd',
                            multi = False,
                            clearable = True,
                            disabled = False,
                            searchable = True,
                            style = {"display": True},
                            value = DATASET.PIMA_DIABETES.value,
                            placeholder = "Dataset",
                            persistence = True,
                            persistence_type = "memory",
                            options = [{"label":ds.name, "value":ds.value} for ds in DATASET], className = "dcc_compon")
        app_tabs = dcc.Tabs(id="tabs", value='dataset_dist', children=[
                        dcc.Tab(label='Distribution', value='dataset_dist'),
                        dcc.Tab(label='Line Plot', value='dataset_line_plot'),
                        dcc.Tab(label='Pie Chart', value='dataset_pie_chart'),
                        dcc.Tab(label='Violin & Box Plot', value='violin_box_plot'),
                    ])
        
        app_page = html.Div(id='main_page', children=self.layouts)
        main_html_layout = html.Div([html.H1('Analysis'),
                                    app_dd, app_tabs, app_page])

        self.app.layout = main_html_layout

        @self.app.callback(
        Output('main_page', 'children'),
        [Input('tabs', 'value')],
        [Input('main_dataset_dd', 'value')]
        )
        def update_tab_page(tabs, dsdir):
            self.df = pd.read_csv(dsdir)
            print(self.df)

            if dsdir == DATASET.PIMA_DIABETES.value:
                self.layouts = self.pimadds_tabs()
            elif dsdir == DATASET.HOTEL_BOOKING_CANCELATION.value:
                self.layouts = self.hotelBookingCancel_tabs()
            elif dsdir == DATASET.MOVIE_RECOMMENDATION_SYSTEM.value:
                self.layouts = self.movieRecomSys_tabs()
            
            if tabs == "dataset_dist":
                return self.layouts[0]
            elif tabs == "dataset_line_plot":
                return self.layouts[1]
            elif tabs == "dataset_pie_chart":
                return self.layouts[2]
            elif tabs == "violin_box_plot":
                return self.layouts[3]
            
        self.app.run_server(debug=True)