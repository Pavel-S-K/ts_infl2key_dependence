import pandas as pd

from .plot_data_plotly import plot_data_plotly


def plot_timeStamps(df: pd.Series):
    """Функция отрисовки timeStamps временного ряда"""

    a = []
    b = []
    for x in range(0, df.shape[0] - 1):
        b.append(df.index.values[x + 1])
        a.append(df.index.values[x + 1] - df.index.values[x])

    plot_data_plotly(pd.Series(a, index=b).dt.components['hours'])
