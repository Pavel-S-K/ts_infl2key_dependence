import pandas as pd


def get_shift_list(ts: pd.Series, min_lag: int = 1, neg_lags: bool = False, shift_len_max: int = False) -> list:
    """
    Функция генерации списка допустимых лагов для LagEncoder
    """
    ts_len = ts.shape[0]

    if not shift_len_max:
        shift_len_max = int(40 * ts_len / 100)
        shift_list = [i for i in range(min_lag, shift_len_max + 1)]
    elif isinstance(shift_len_max, int):
        shift_list = [i for i in range(min_lag, shift_len_max + 1)]
    else:
        shift_list = []

    if neg_lags is True:
        neg_shift_lags = [-i for i in shift_list]
        shift_list.extend(neg_shift_lags)

    return shift_list
