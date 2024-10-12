import pandas as pd


def change_timestamp(data: pd.DataFrame, by: str = 'M', agg: str = 'last') -> pd.DataFrame:
    """Функция изменения масштаба временной шкалы"""

    data = pd.DataFrame(data)
    temporary_df = pd.DataFrame(data).copy()
    temporary_df["year"] = temporary_df.index.year.values
    temporary_df["month"] = temporary_df.index.month.values
    # temporary_df["day"] = temporary_df.index.day.values

    if by == 'M' or by == 'MS':
        start_date = temporary_df.index[0]
        end_date = temporary_df.index[-1]
        new_df = pd.DataFrame(index=pd.date_range(start=start_date,
                                                  end=end_date,
                                                  freq=by))
        # new_df = pd.DataFrame(index=pd.date_range(start=temporary_df.index[0] , end=temporary_df.index[-1] + (
        # temporary_df.index[-1] - temporary_df.index[-10] ), freq=by))
        if by == 'MS':
            for ticker in data.columns:
                new_df[ticker] = temporary_df.loc[new_df.index[0]:].groupby(by=["year", "month"])[ticker].agg(
                    agg).values
        if by == 'M':
            for ticker in data.columns:
                new_df[ticker] = temporary_df.loc[:new_df.index[-1]].groupby(by=["year", "month"])[ticker].agg(
                    agg).values

    elif by == 'Y':
        new_df = pd.DataFrame(index=pd.date_range(start=temporary_df.index[0],
                                                  end=temporary_df.index[-1] + (
                                                          temporary_df.index[-1] - temporary_df.index[-10]),
                                                  freq=by))
        for ticker in data.columns:
            new_df[ticker] = temporary_df.groupby(by=["year"])[ticker].agg(agg).values

    return new_df
