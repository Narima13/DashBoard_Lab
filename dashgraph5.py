import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

# Загрузка данных
df = pd.read_csv(r'I:\programs\Pycharm\pythonProject\TextFile1.csv')
df1 = pd.read_csv(r'I:\programs\Pycharm\pythonProject\TextFile2.csv')

# Создание экземпляра приложения
app = dash.Dash(__name__)

# Определение структуры дашборда
app.layout = html.Div([
    html.Div([
        html.H1('Дашборд анализа данных о посещении веб-сайта deliciousfruit.com', style={'textAlign': 'center'}),
        html.P('Этот дашборд предоставляет информацию о количестве пользователей онлайн и'
                       ' среднем времени активности на сайте в зависимости от дня и времени дня',

               style={'textAlign': 'center'}),
        html.Div([
            html.Label('Выберите дату:', style={'fontSize': 18}),
            dcc.Dropdown(
                id='date-dropdown',
                options=[{'label': date, 'value': date} for date in df1['Date']],
                value=df1['Date'].iloc[0],
                clearable=False,
                style={'width': '50%', 'margin': '0 auto'}
            ),
        ], style={'textAlign': 'center', 'marginBottom': '30px'}),
    ], style={'marginBottom': '30px'}),

    html.Div([
        # Точечный график
        dcc.Graph(id='scatter-plot'),
    ], style={'width': '48%', 'display': 'inline-block'}),

], style={'padding': '20px'})

# Определение логики дашборда
@app.callback(
    Output('scatter-plot', 'figure'),
    [Input('date-dropdown', 'value')]
)
def update_charts(selected_date):
    scatter_plot = px.scatter(df, x='Amount_of_users', y='MiddleSession(sec)',
                              title='Точечный график')
    return scatter_plot
# Запуск приложения
if __name__ == '__main__':
    app.run_server(debug=True)