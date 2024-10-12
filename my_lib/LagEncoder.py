import pandas as pd


class LagEncoder:
    """Генерация лагов по списку"""

    def __init__(self, lags_list):
        self.lags_list = lags_list

    def get_lags(self, series):
        df_lags = pd.DataFrame(index=series.index)
        series_name = series.name
        for i in self.lags_list:
            col_name = f'{series_name}_lag({i})'
            df_lags[col_name] = series.shift(i)
        return df_lags
