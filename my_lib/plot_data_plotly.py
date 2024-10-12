import pandas as pd
import plotly.graph_objects as go


def plot_data_plotly(df, title: str = '', xaxis_title: str = '', yaxis_title: str = ''):
    """ Функция отрисовки временных рядов"""

    fig = go.Figure()
    df = pd.DataFrame(df)

    for col in df.columns:
        fig.add_trace(go.Scatter(x=df.index, y=df[col],
                                 mode='lines',
                                 name=col))
        fig.update_layout(
            title=title,
            xaxis_title=xaxis_title,
            yaxis_title=yaxis_title, )
    fig.show()
