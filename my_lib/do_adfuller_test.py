import pandas as pd
import statsmodels.api as sm


def do_adfuller_test(ts: pd.Series) -> pd.DataFrame:

    """Проведение дополненного теста Дики—Фуллера для проверки ряда на стационарность"""

    ts = ts.copy()

    scores_list = []
    p_value_list = []
    scores_df = pd.DataFrame()

    ts = ts.dropna()

    test_results = sm.tsa.stattools.adfuller(ts)

    scores_list.append(test_results[0])
    p_value_list.append(test_results[1])

    scores_df['adfuller_score'] = scores_list
    scores_df['p_value'] = p_value_list
    scores_df['ts_name'] = [ts.name]

    return scores_df
